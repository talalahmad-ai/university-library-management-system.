#!/usr/bin/env python3
"""Export the approved planning source to XLSX, charts and a readable PDF report."""
import json
import math
import re
import textwrap
from datetime import date, datetime, timedelta
from html import escape
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import xlsxwriter
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
    Spacer, PageBreak, NextPageTemplate, Image, LongTable, TableStyle, KeepTogether)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parents[1]
R=ROOT/'reports'
D=json.loads((R/'planning-data.json').read_text())
T=D['tasks']; OWNER=D['student']['name']; HANDLE=D['student']['github']
COLORS={'A1':'#16648A','A2':'#316D54','A3':'#765295','A4':'#B55B28'}
START=min(date.fromisoformat(t['start']) for t in T)
END=max(date.fromisoformat(t['end']) for t in T)
DAYS=[START+timedelta(i) for i in range((END-START).days+1)]

def h(t): return sum(t['hours'])
def n(t): return (date.fromisoformat(t['end'])-date.fromisoformat(t['start'])).days+1
def dt(s): return datetime.fromisoformat(s)

def charts():
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
    fig,ax=plt.subplots(figsize=(19,11))
    fig.subplots_adjust(left=.27,right=.97,top=.86,bottom=.10)
    for day in DAYS:
        if day.weekday()>=5: ax.axvspan(mdates.date2num(day),mdates.date2num(day)+1,color='#F0F2F5',zorder=0)
    pos={t['id']:i for i,t in enumerate(T)}
    for i,t in enumerate(T):
        s=mdates.date2num(date.fromisoformat(t['start'])); e=mdates.date2num(date.fromisoformat(t['end']))+1
        ax.barh(i,e-s,left=s,height=.55,color=COLORS[t['phase']],zorder=3)
        ax.text(e+.12,i,f"{h(t):g} h",va='center',fontsize=10,color='#22374A')
        for pred in t['depends']:
            p=next(x for x in T if x['id']==pred)
            pe=mdates.date2num(date.fromisoformat(p['end']))+1
            ax.annotate('',xy=(s,i),xytext=(pe,pos[pred]),arrowprops={'arrowstyle':'->','color':'#687D90','lw':.7,'connectionstyle':'arc3,rad=0.08'},zorder=2)
    labels=[t['id']+'  '+t['name'] for t in T]
    for j,m in enumerate(D['milestones']):
        y=len(T)+j+.5
        ax.scatter(mdates.date2num(date.fromisoformat(m['date']))+.88,y,marker='D',s=65,color=COLORS[m['phase']],zorder=4)
        labels.append(m['id']+'  '+m['phase']+' proposed gate')
    ys=list(range(len(T)))+[len(T)+j+.5 for j in range(4)]
    ax.set_yticks(ys,labels,fontsize=11)
    ax.invert_yaxis()
    ax.set_xlim(mdates.date2num(START)-.3,mdates.date2num(END)+3)
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
    ax.xaxis.tick_top(); ax.tick_params(axis='x',rotation=45,labelsize=10)
    ax.grid(axis='x',color='#D5DDE6',lw=.5)
    for s in ax.spines.values(): s.set_visible(False)
    fig.suptitle('University LMS | Proposed project schedule',x=.035,ha='left',fontsize=22,fontweight='bold',color='#16334B',y=.98)
    fig.text(.035,.925,'13 November–14 December 2026  •  One student: Talal Ahmad  •  112 base person-hours',fontsize=13,color='#354E63')
    fig.text(.035,.04,'PROPOSED DATES — official deadlines not supplied. Calendar days include weekends. Arrows: finish-to-start; diamonds: end-of-day gates.\nA1 blue · A2 green · A3 purple · A4 orange. Later phases are planned only. The schedule is not a record of actual work dates.',fontsize=11,color='#354E63')
    fig.savefig(R/'gantt-chart.png',dpi=170);fig.savefig(R/'gantt-chart.pdf');plt.close(fig)

    fig,ax=plt.subplots(figsize=(18,13));ax.set(xlim=(0,18),ylim=(0,13));ax.axis('off')
    def box(x,y,w,hh,txt,fill,fs=12):
        p=FancyBboxPatch((x,y),w,hh,boxstyle='round,pad=0.08,rounding_size=.06',facecolor=fill,edgecolor='#658096',lw=.9,zorder=2)
        ax.add_patch(p);ax.text(x+w/2,y+hh/2,txt,ha='center',va='center',fontsize=fs,color='#15334A',zorder=3)
    ax.text(.2,12.7,'University LMS | Work Breakdown Structure',fontsize=23,fontweight='bold',color='#16334B')
    ax.text(.2,12.25,'16 effort-bearing packages · Talal Ahmad · Phase 1 execution; Assignments 2–4 planned only',fontsize=13,color='#354E63')
    box(5.1,10.9,7.8,.8,'0.0 University Library Management System\nAnalysis, planning, modeling and interface design','#D9EAF4',15)
    names=['1.0 Assignment 1\nPlanning and GitHub','2.0 Assignment 2\nRequirements and SRS','3.0 Assignment 3\nUML models','4.0 Assignment 4\nPrototype and submission']
    for phase in range(1,5):
        x=.2+(phase-1)*4.45; c=x+2.02
        ax.plot([9,9,c,c],[10.9,10.4,10.4,9.95],color='#8195A6',lw=1,zorder=1)
        box(x,9.05,4.05,.9,names[phase-1],'#E6EEF4',14)
        group=[t for t in T if t['phase']==f'A{phase}']
        trunk=x+.12
        last=8.05-(len(group)-1)*1.08
        ax.plot([c,c,trunk,trunk],[9.05,8.8,8.8,last+.38],color='#8195A6',lw=1,zorder=1)
        for j,t in enumerate(group):
            y=8.05-j*1.08
            ax.plot([trunk,x+.42],[y+.38,y+.38],color='#8195A6',lw=1,zorder=1)
            txt=t['id']+'\n'+'\n'.join(textwrap.wrap(t['name'],27))
            box(x+.42,y,3.62,.78,txt,'#F4F7FA',11.5)
    ax.text(.2,.25,'Editable sources: reports/wbs.drawio · reports/wbs.csv · reports/planning-data.json. Summary branches and milestones carry no extra effort.',fontsize=11,color='#354E63')
    fig.tight_layout(pad=.4);fig.savefig(R/'wbs-diagram.png',dpi=170);fig.savefig(R/'wbs-diagram.pdf');plt.close(fig)

def workbook():
    wb=xlsxwriter.Workbook(R/'assignment-1-planning.xlsx')
    wb.set_properties({'title':'University LMS — Assignment 1 planning','author':'Codex-assisted preparation','subject':'Proposed one-student project plan; official deadlines unconfirmed'})
    title=wb.add_format({'bold':True,'font_size':18,'font_color':'#16334B'})
    note=wb.add_format({'text_wrap':True,'font_color':'#785220','bg_color':'#FFF4D6','valign':'top'})
    head=wb.add_format({'bold':True,'font_color':'white','bg_color':'#16334B','text_wrap':True,'valign':'vcenter','border':1})
    cell=wb.add_format({'text_wrap':True,'valign':'top','border':1,'border_color':'#D9E1EA'})
    number=wb.add_format({'num_format':'0.0','border':1,'border_color':'#D9E1EA','valign':'top'})
    formula=wb.add_format({'num_format':'0.0','font_color':'#146448','bg_color':'#EFF8F1','border':1,'border_color':'#D9E1EA'})
    datefmt=wb.add_format({'num_format':'dd mmm yyyy','border':1,'border_color':'#D9E1EA','valign':'top'})
    totalfmt=wb.add_format({'bold':True,'num_format':'0.0','top':2,'bg_color':'#E5EEF6'})
    phasefmt={p:wb.add_format({'bg_color':v,'font_color':'white','align':'center'}) for p,v in COLORS.items()}
    def sheet(name,headers,widths):
        s=wb.add_worksheet(name);s.hide_gridlines(2);s.merge_range(0,0,0,len(headers)-1,name+' | University LMS',title)
        s.merge_range(2,0,3,len(headers)-1,'PROPOSED PLAN — official deadlines not supplied. Student: Talal Ahmad (@talalahmad-ai). All roles belong to one person.',note)
        for c,txt in enumerate(headers):s.write(4,c,txt,head);s.set_column(c,c,widths[c])
        s.set_row(4,34);s.freeze_panes(5,2);s.autofilter(4,0,4+len(T),len(headers)-1)
        s.set_landscape();s.set_paper(9);s.fit_to_pages(1,0);s.repeat_rows(0,4);s.set_margins(.3,.3,.45,.45)
        s.set_footer('&LUniversity LMS — proposed planning&C&P / &N&R12 Nov 2026')
        return s
    s=sheet('Overview',['Field','Value'],[32,110]);s.autofilter(4,0,4,1)
    overview=[('Student','Talal Ahmad (@talalahmad-ai), confirmed by user'),('Repository','https://github.com/'+D['repository']),('Scope','Assignment 1 preparation only; Assignments 2–4 planned'),('Calendar',D['calendar']),('Capacity assumption','6 h per calendar day across all roles combined; actual availability unconfirmed'),('Base effort','112 person-hours; Lead 30, Analyst 37.5, Designer 44.5; one person total = 112'),('Reserve','15% = 16.8 h, unallocated; planning envelope = 128.8 h'),('Official deadlines','A1/A2/A3/A4: not supplied; all targets are proposed'),('Open decision','Repository has an extra final period compared with the literal PDF name; owner/instructor confirmation needed'),('RACI','A/R = Talal for every package. No other named students; C/I not artificially assigned.'),('Source of truth','reports/planning-data.json → build_planning.py → export_planning.py. Reconcile workbook edits to JSON before regeneration.'),('Formula behavior','Green cells are formulas with cached results. Schedule duration and dependencies, person-hour totals, risk scores and capacity totals are calculated.'),('Attribution','Prepared with Codex assistance; estimates are not actual hours or claims of student participation.')]
    for r,row in enumerate(overview,5):s.set_row(r,40);s.write_row(r,0,row,cell)

    headers=['ID','Phase','Activity','Start','End','Days','FS predecessors','Assigned student','Lead role','Lead h','Analyst h','Designer h','Person-hours','Date status','Dependency check']
    s=sheet('Schedule',headers,[8,7,37,15,15,8,20,29,14,10,10,10,13,27,18])
    lookup={t['id']:i+6 for i,t in enumerate(T)}
    for r,t in enumerate(T,5):
        er=r+1;s.set_row(r,42)
        for c,v in enumerate([t['id'],t['phase'],t['name']]):s.write(r,c,v,cell)
        s.write_datetime(r,3,dt(t['start']),datefmt);s.write_datetime(r,4,dt(t['end']),datefmt)
        s.write_formula(r,5,f'=E{er}-D{er}+1',formula,n(t));s.write(r,6,', '.join(t['depends']) or 'None',cell)
        s.write(r,7,OWNER+' (@'+HANDLE+')',cell);s.write(r,8,t['role'],cell)
        for c,v in enumerate(t['hours'],9):s.write_number(r,c,v,number)
        s.write_formula(r,12,f'=SUM(J{er}:L{er})',formula,h(t));s.write(r,13,'Proposed; not official',cell)
        f='="OK"' if not t['depends'] else f'=IF(D{er}>MAX('+','.join(f'E{lookup[p]}' for p in t['depends'])+'),"OK","ERROR")'
        s.write_formula(r,14,f,cell,'OK')
    s.write(21,2,'BASE TOTAL',totalfmt)
    for c in [9,10,11,12]:s.write_formula(21,c,f'=SUM({xlsxwriter.utility.xl_col_to_name(c)}6:{xlsxwriter.utility.xl_col_to_name(c)}21)',totalfmt,sum(t['hours'][c-9] for t in T) if c<12 else 112)

    s=sheet('Milestones',['Gate','Phase','Deliverable / target','Proposed date','Predecessor','Official deadline'],[9,8,60,18,18,25]);s.autofilter(4,0,8,5)
    for r,m in enumerate(D['milestones'],5):
        s.set_row(r,40);s.write(r,0,m['id'],cell);s.write(r,1,m['phase'],cell);s.write(r,2,m['name'],cell)
        refs=','.join('Schedule!E'+str(lookup[p]) for p in m['depends'])
        s.write_formula(r,3,f'=MAX({refs})',datefmt,xlsxwriter.utility._datetime_to_excel_datetime(dt(m['date']),False,False))
        s.write(r,4,', '.join(m['depends']),cell);s.write(r,5,'Not supplied',note)

    s=sheet('WBS',['ID','Work package','Deliverable','Acceptance evidence'],[8,37,65,90])
    for r,t in enumerate(T,5):s.set_row(r,66);s.write_row(r,0,[t['id'],t['name'],t['deliverable'],t['acceptance']],cell)

    s=sheet('RACI',['ID','Work package','Talal Ahmad (@talalahmad-ai)','Functional lead role','Interpretation'],[8,45,33,18,66])
    for r,t in enumerate(T,5):s.set_row(r,36);s.write_row(r,0,[t['id'],t['name'],'A/R',t['role'],'One accountable and responsible student; C/I omitted because no additional student is confirmed.'],cell)

    s=sheet('Effort',['ID','Work package','Lead role h','Analyst role h','Designer role h','Talal total h'],[8,50,16,16,16,18])
    for r,t in enumerate(T,5):
        er=r+1;s.set_row(r,34);s.write(r,0,t['id'],cell);s.write(r,1,t['name'],cell)
        for c,v in enumerate(t['hours'],2):s.write_number(r,c,v,number)
        s.write_formula(r,5,f'=SUM(C{er}:E{er})',formula,h(t))
    s.write(21,1,'BASE TOTAL',totalfmt)
    for c in range(2,6):s.write_formula(21,c,f'=SUM({xlsxwriter.utility.xl_col_to_name(c)}6:{xlsxwriter.utility.xl_col_to_name(c)}21)',totalfmt,sum(t['hours'][c-2] for t in T) if c<5 else 112)
    s.write(23,1,'Unallocated estimate reserve (15%)',cell);s.write_formula(23,5,'=F22*15%',formula,16.8)
    s.write(24,1,'Planning envelope (base + reserve)',cell);s.write_formula(24,5,'=F22+F24',totalfmt,128.8)

    s=sheet('Risks',['ID','Risk','Likelihood 1–5','Impact 1–5','Score','Priority','Named owner','Monitoring role','Trigger','Mitigation','Contingency'],[8,40,13,13,10,14,29,16,65,75,75]);s.autofilter(4,0,4+len(D['risks']),10)
    for r,risk in enumerate(D['risks'],5):
        er=r+1;score=risk['likelihood']*risk['impact'];s.set_row(r,92)
        s.write_row(r,0,[risk['id'],risk['risk'],risk['likelihood'],risk['impact']],cell)
        s.write_formula(r,4,f'=C{er}*D{er}',formula,score)
        s.write_formula(r,5,f'=IF(E{er}>=15,"High",IF(E{er}>=6,"Medium","Low"))',cell,'High' if score>=15 else 'Medium' if score>=6 else 'Low')
        s.write_row(r,6,[OWNER+' (@'+HANDLE+')',risk['role'],risk['trigger'],risk['mitigation'],risk['contingency']],cell)
    s.data_validation(5,2,16,3,{'validate':'integer','criteria':'between','minimum':1,'maximum':5})
    s.conditional_format(5,4,16,4,{'type':'3_color_scale'})

    s=sheet('Gantt',['ID','Activity','Hours','Start','End']+[str(x.day) for x in DAYS],[8,43,9,14,14]+[3.5]*len(DAYS))
    s.set_column(3,4,None,None,{'hidden':True});s.freeze_panes(5,5);s.set_row(4,62);s.fit_to_pages(1,1)
    dayfmt=wb.add_format({'bold':True,'rotation':90,'num_format':'dd mmm','align':'center','bg_color':'#E3EBF3','border':1})
    for c,day in enumerate(DAYS,5):s.write_datetime(4,c,datetime.combine(day,datetime.min.time()),dayfmt)
    for r,t in enumerate(T,5):
        er=r+1;s.set_row(r,24);s.write(r,0,t['id'],cell);s.write(r,1,t['name'],cell);s.write_formula(r,2,f'=Schedule!M{er}',number,h(t))
        s.write_formula(r,3,f'=Schedule!D{er}',datefmt,xlsxwriter.utility._datetime_to_excel_datetime(dt(t['start']),False,False))
        s.write_formula(r,4,f'=Schedule!E{er}',datefmt,xlsxwriter.utility._datetime_to_excel_datetime(dt(t['end']),False,False))
        for c,day in enumerate(DAYS,5):
            s.write_blank(r,c,None)
        s.conditional_format(r,5,r,4+len(DAYS),{'type':'formula','criteria':f'=AND(F$5>=$D{er},F$5<=$E{er})','format':phasefmt[t['phase']]})
    for r,m in enumerate(D['milestones'],23):
        s.write(r,0,m['id'],cell);s.write(r,1,m['phase']+' proposed gate',cell)
        for c,day in enumerate(DAYS,5):
            if str(day)==m['date']:s.write(r,c,'◆',phasefmt[m['phase']])
    s.print_area(0,0,27,4+len(DAYS))

    s=sheet('Capacity',['Calendar date','Talal base hours','Assumed capacity h','Check'],[22,25,25,20]);s.autofilter(4,0,4+len(DAYS),3)
    for r,day in enumerate(DAYS,5):
        er=r+1;load=sum(h(t)/n(t) for t in T if date.fromisoformat(t['start'])<=day<=date.fromisoformat(t['end']))
        s.write_datetime(r,0,datetime.combine(day,datetime.min.time()),datefmt)
        f=f'=SUMPRODUCT(--(Schedule!$D$6:$D$21<=A{er}),--(Schedule!$E$6:$E$21>=A{er}),Schedule!$M$6:$M$21/Schedule!$F$6:$F$21)'
        s.write_formula(r,1,f,formula,load);s.write_number(r,2,D['capacity_hours_per_day'],number)
        s.write_formula(r,3,f'=IF(B{er}<=C{er},"OK","OVERLOAD")',cell,'OK')
    last=5+len(DAYS);s.write(last,0,'Allocated base total',totalfmt);s.write_formula(last,1,f'=SUM(B6:B{last})',totalfmt,112)
    wb.close()

def report():
    fonts=Path('/usr/share/fonts/truetype/dejavu')
    pdfmetrics.registerFont(TTFont('DejaVu',str(fonts/'DejaVuSans.ttf')))
    pdfmetrics.registerFont(TTFont('DejaVu-Bold',str(fonts/'DejaVuSans-Bold.ttf')))
    styles=getSampleStyleSheet()
    for style in styles.byName.values():
        if hasattr(style,'fontName'):style.fontName='DejaVu-Bold' if 'Bold' in style.fontName else 'DejaVu'
    styles['Normal'].fontName='DejaVu';styles['Normal'].fontSize=9.5;styles['Normal'].leading=14
    styles['Heading1'].textColor=colors.HexColor('#16334B');styles['Heading1'].spaceBefore=14
    styles['Heading2'].textColor=colors.HexColor('#16648A');styles['Heading2'].spaceBefore=12
    styles.add(ParagraphStyle('SmallTable',fontName='DejaVu',fontSize=8,leading=11,spaceAfter=0))
    styles.add(ParagraphStyle('CoverTitle',fontName='DejaVu-Bold',fontSize=31,leading=37,textColor=colors.HexColor('#16334B'),spaceAfter=22))
    styles.add(ParagraphStyle('CoverSub',fontName='DejaVu',fontSize=15,leading=23,textColor=colors.HexColor('#354E63'),spaceAfter=18))
    styles.add(ParagraphStyle('Caption',fontName='DejaVu',fontSize=9,leading=13,textColor=colors.HexColor('#354E63'),spaceAfter=10))
    class Doc(BaseDocTemplate):
        def afterFlowable(self,flow):
            if isinstance(flow,Paragraph) and getattr(flow,'toc',False):self.notify('TOCEntry',(0,flow.getPlainText(),self.page))
    def foot(canvas,doc):
        w,hh=canvas._pagesize;canvas.saveState();canvas.setStrokeColor(colors.HexColor('#C6D2DE'));canvas.line(40,36,w-40,36)
        canvas.setFont('DejaVu',8);canvas.setFillColor(colors.HexColor('#53697E'))
        canvas.drawString(40,24,'University LMS | Assignment 1 | Proposed plan | 12 November 2026')
        canvas.drawRightString(w-40,24,str(doc.page));canvas.restoreState()
    doc=Doc(str(R/'assignment-1-plan.pdf'),pagesize=A4,title='University LMS — Assignment 1 planning report',author='Codex-assisted preparation for Talal Ahmad')
    pw,ph=A4;lw,lh=landscape(A4)
    doc.addPageTemplates([PageTemplate(id='Portrait',frames=[Frame(42,48,pw-84,ph-90,id='portrait',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=foot,pagesize=A4),
                          PageTemplate(id='Landscape',frames=[Frame(35,48,lw-70,lh-84,id='landscape',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=foot,pagesize=landscape(A4))])
    story=[]
    def p(s,sty='Normal'):
        return Paragraph(escape(s).replace('\n','<br/>'),styles[sty])
    def heading(s):
        q=p(s,'Heading1');q.toc=True;story.append(q)
    def tbl(headers,rows,widths=None):
        clean=lambda x:p(str(x),'SmallTable')
        data=[[clean(x) for x in headers]]+[[clean(x) for x in row] for row in rows]
        tb=LongTable(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
        tb.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E4EDF5')),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),.7,colors.HexColor('#658096')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F5F7FA')]),('GRID',(0,1),(-1,-1),.3,colors.HexColor('#D7E0E8')),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
        story.extend([tb,Spacer(1,12)])
    story.extend([Spacer(1,70),p('University Library\nManagement System','CoverTitle'),p('Assignment 1\nProject planning and GitHub','CoverSub'),Spacer(1,25),p('Talal Ahmad · @talalahmad-ai','Heading2'),p('Version 1.0 | Prepared 12 November 2026 | Asia/Karachi'),Spacer(1,20),p('Proposed planning window: 13 November–14 December 2026. Official submission deadlines and university/department details have not been supplied. All later phases are planned only.'),Spacer(1,18),p('112 base person-hours · 16 work packages · 12 risks\nOne named student; three functional roles'),Spacer(1,18),p('Repository: https://github.com/'+D['repository'],'Caption'),p('The repository has a literal final period, unlike the exact name in the PDF. Owner/instructor confirmation is required before submission. Prepared with Codex assistance; no student participation, interviews or testing results are fabricated.'),PageBreak()])
    heading('Contents and document status')
    toc=TableOfContents();toc.levelStyles=[ParagraphStyle('TOC',fontSize=10,leading=18,leftIndent=0,firstLineIndent=0)];story.append(toc)
    story.extend([Spacer(1,25),p('The Markdown documents and planning-data.json are the editable sources. XLSX formulas include cached results. Standalone vector Gantt/WBS PDFs and PNGs are supplied for readable viewing at full size. The evidence index and compliance matrix record final remote verification separately.'),PageBreak()])
    heading('1. Project definition and scope')
    story.extend([p('The case scenario describes a university library using manual or outdated records for borrowing, returns, membership and overdue books. The academic project analyzes and designs an LMS; complete implementation is not required. Phase 1 produces planning and GitHub evidence.'),Spacer(1,10)])
    tbl(['Capability','Planned analysis/design boundary'],[['Catalog and copies','Searchable books and copy availability; no live inventory import.'],['Membership','Student/faculty membership and librarian/admin roles; policies unconfirmed.'],['Borrowing and returns','Member validation, available-copy loans, due dates, return and overdue handling.'],['Reservations','Search/detail/reserve interaction; queue precedence and expiry need confirmation.'],['Overdue notifications','Notification information and triggers as design concepts; delivery rules unconfirmed.']],[130,381])
    story.append(p('Excluded: production backend/frontend, live messaging, payment processing, SSO, hosting, real record migration and fabricated human evidence. Success is a coherent, traceable and reviewable coursework package. See reports/project-charter.md for full assumptions, governance and acceptance measures.'))
    story.append(p('Confirmed student: Talal Ahmad. All planned packages are assigned to him. Hamza-Khaalid is the authenticated helper; preparation commits are attributed to Codex. University/department and official deadlines remain unknown. Capacity of six hours per calendar day is an estimate requiring student confirmation.'))
    tbl(['Gate','Planned measurable outcome'],[['A1','Planning artifacts, README/folders, assigned task Issues, at least three meaningful new remote commits and genuine screenshots.'],['A2 — future','Stakeholder analysis, required FR/NFR/stories/criteria, AI-review decisions and structured SRS/traceability.'],['A3 — future','Four editable UML models with exports/explanations consistent with SRS.'],['A4 — future','Five connected screens, two workflows, real feedback from two classmates and two evidenced improvements.']],[90,421])
    story.append(PageBreak());heading('2. Work Breakdown Structure')
    story.append(p('Root 0.0 contains four assignment branches. The following 16 leaf packages are effort-bearing; summary branches and milestone gates add no duplicate effort. Editable diagram: reports/wbs.drawio.'))
    tbl(['ID','Package','Deliverable'],[[t['id'],t['name'],t['deliverable']] for t in T],[36,180,295])
    story.append(NextPageTemplate('Landscape'));story.append(PageBreak());heading('3. WBS visual')
    story.append(Image(str(R/'wbs-diagram.png'),width=630,height=455))
    story.append(NextPageTemplate('Portrait'));story.append(PageBreak());heading('4. Schedule and dependencies')
    story.append(p('Proposed calendar-day plan, including weekends. Every dependency is finish-to-start: a successor begins after its predecessor ends. Dates are targets, not official deadlines or actual work records. All tasks are assigned to Talal.'))
    tbl(['ID','Activity','Start → End (2026)','Days','Depends on','Hours'],[[t['id'],t['name'],dt(t['start']).strftime('%d %b')+' → '+dt(t['end']).strftime('%d %b'),n(t),', '.join(t['depends']) or 'None',f'{h(t):g}'] for t in T],[33,159,105,34,137,43])
    tbl(['Gate','Proposed target','Official deadline'],[[m['id']+' / '+m['phase'],m['date'],'Not supplied'] for m in D['milestones']],[100,150,261])
    story.append(p('Critical dependency chain: 1.1 → 1.3 → 1.4 → 1.5 → 1.6 → 1.7 → 2.1 → 2.2 → 2.3 → 3.1 → 3.2 → 4.2 → 4.3 → 4.4, 32 calendar days. Task 1.2 has four days of float; task 4.1 has two. Rebaseline when real deadlines or availability are known.'))
    story.append(NextPageTemplate('Landscape'));story.append(PageBreak());heading('5. Proposed Gantt chart')
    story.append(Image(str(R/'gantt-chart.png'),width=770,height=446))
    story.append(NextPageTemplate('Portrait'));story.append(PageBreak());heading('6. Responsibility and effort')
    story.append(p('Talal Ahmad (@talalahmad-ai) is A/R on every row: Accountable for acceptance and Responsible for execution. No additional student is named for Consulted or Informed duties. Functional role allocations describe one person’s types of work, not three people. Estimates are not actual hours or evidence of participation.'))
    tbl(['ID','Functional lead','Talal RACI','Lead h','Analyst h','Designer h','Talal total h'],[[t['id'],t['role'],'A/R',*t['hours'],h(t)] for t in T]+[['TOTAL','One student','',30,37.5,44.5,112]],[35,100,60,70,75,85,86])
    story.append(p('Phase totals: A1 34 h; A2 31 h; A3 18 h; A4 29 h. Base = 112 h. Unallocated 15% estimate reserve = 16.8 h; envelope = 128.8 h. Reserve is not scheduled task effort or guaranteed calendar float. Combined daily load uses every concurrent task across all roles and does not exceed the assumed six-hour capacity; the overlapping UML/UI tasks peak below that cap.'))
    story.append(p('Review actuals at each gate, reassess any >20% variance and revise dates when capacity is lower or a trigger occurs. sources: effort-estimates.csv, responsibility-matrix.csv and workbook Effort/Capacity sheets.'))
    story.append(PageBreak());heading('7. Risks, mitigation and contingency')
    story.append(p('Likelihood: 1 rare, 2 unlikely, 3 possible, 4 likely, 5 almost certain. Impact: 1 negligible, 2 minor rework, 3 material task delay, 4 phase-gate threat, 5 mandatory submission at risk. Score = L × I. Low 1–5; Medium 6–14; High 15–25. These are qualitative judgments. Talal owns every risk. Review high risks each work session and all risks at every gate.'))
    story.append(p('Highest priorities: R01 ambiguous policies and R05 unknown official deadlines (16 each). The initial URL issue was resolved; the repository-name exception remains a disclosed decision.'))
    for risk in D['risks']:
        score=risk['likelihood']*risk['impact']
        block=[p(risk['id']+' — '+risk['risk'],'Heading2'),p(f"Likelihood {risk['likelihood']} · Impact {risk['impact']} · Score {score} · Monitoring role {risk['role']} · Owner Talal Ahmad"),p('Trigger: '+risk['trigger']),p('Mitigation: '+risk['mitigation']),p('Contingency: '+risk['contingency']),Spacer(1,8)]
        story.append(KeepTogether(block))
    heading('8. GitHub evidence and final review')
    story.append(p('The exact trailing-dot repository was cloned and inspected before integration. Initial commit d6eb076 and its README are preserved in history. Initial checks found Write permission, an unprotected main branch, no rulesets and zero Issues. talalahmad-ai is an eligible assignee. No new remote repository was created.'))
    story.append(p('Genuine incremental preparation commits use the Codex identity and current timestamps. Issue definitions name Talal as the planned assignee. Initial live Issue creation returned HTTP 403, Resource not accessible by integration; do not treat drafts as real Issues. Consult the final evidence index for any later permission resolution and actual counts. Later-phase Issues, if created, do not mean those assignments were executed. Final live counts, commit SHAs, URLs and capture times are recorded in reports/evidence/remote-verification.json and capture-manifest.json after publication.'))
    tbl(['Submission item','Where to inspect'],[['Repository URL / README','README.md; actual GitHub root screenshot'],['Remote commit history','reports/evidence/remote-verification.json and GitHub commits screenshot'],['Assigned task Issues','reports/issue-map.md and genuine Issues/individual-Issue screenshots'],['Gantt / schedule','project-schedule.csv, assignment-1-planning.xlsx, gantt-chart.pdf / PNG'],['WBS / responsibilities','wbs.drawio / CSV / PDF; responsibility-matrix.csv; effort-estimates.csv'],['Risk assessment','risk-register.md / CSV and workbook Risks sheet'],['Final audit','compliance-matrix.md; quality-review.md; evidence/README.md']],[150,361])
    story.append(p('Before submission: obtain official deadlines, confirm Talal’s availability and resolve whether the repository’s final period is permitted. The owner already controls the existing repository; no ownership transfer is needed. Do not begin Assignment 2 without the user’s instruction.'))
    story.append(p('Revision 1.0 — 12 November 2026. Sources: instructor PDF (Assignment 1, page 1); uploaded README, starter ZIP and pasted text (supporting context); user-confirmed student and corrected URL. The active request limits execution to Phase 1.'))
    doc.multiBuild(story)

if __name__=='__main__':
    charts();workbook();report()
    print('Exported XLSX, report PDF, Gantt PNG/PDF and WBS PNG/PDF.')
