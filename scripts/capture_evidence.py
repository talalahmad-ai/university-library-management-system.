#!/usr/bin/env python3
"""Capture real public GitHub pages and clearly labeled local artifact renderings."""
import csv
import html
import json
import os
from datetime import datetime,timezone
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1];R=ROOT/'reports';E=R/'evidence';E.mkdir(exist_ok=True)
D=json.loads((R/'planning-data.json').read_text());base='https://github.com/'+D['repository']
records=[]
def now():return datetime.now(timezone.utc).isoformat()
def record(name,source,kind,**extra):records.append({'file':name,'source':source,'kind':kind,'captured_at_utc':now(),**extra})
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    context=browser.new_context(viewport={'width':1600,'height':1100},device_scale_factor=1)
    page=context.new_page()
    targets=[('github-repository.png',base),('github-commits.png',base+'/commits/main/'),('github-issues.png',base+'/issues')]
    for name,url in targets:
        try:
            response=page.goto(url,wait_until='domcontentloaded',timeout=60000)
            page.wait_for_timeout(1500)
            if response is None or response.status!=200:raise RuntimeError('HTTP '+str(response.status if response else None))
            page.screenshot(path=str(E/name),full_page=True)
            record(name,page.url,'Actual public GitHub page; browser not authenticated',http_status=response.status,title=page.title(),viewport={'width':1600,'height':1100})
            if name=='github-repository.png':
                article=page.locator('article.markdown-body').first
                if article.count():article.screenshot(path=str(E/'github-readme.png'));record('github-readme.png',page.url,'Actual GitHub-rendered README element',http_status=200)
        except Exception as exc:record(name,url,'Capture failed',error=str(exc))
    remote=E/'remote-verification.json'
    if remote.exists():
        data=json.loads(remote.read_text());issues=data.get('issues',[])
        if issues:
            issue=issues[0];url=issue.get('url') or issue.get('html_url')
            if url:
                response=page.goto(url,wait_until='domcontentloaded',timeout=60000);page.wait_for_timeout(1200)
                page.screenshot(path=str(E/'github-assigned-issue.png'),full_page=True)
                record('github-assigned-issue.png',page.url,'Actual GitHub Issue page',http_status=response.status)
    for filename,source,title in [('local-raci.png','responsibility-matrix.csv','Named responsibility matrix'),('local-effort.png','effort-estimates.csv','Task and student effort estimates'),('local-risks.png','risk-register.csv','Risk register: scored risks and responses')]:
        with (R/source).open(newline='') as f:rows=list(csv.reader(f))
        table='<thead><tr>'+''.join('<th>'+html.escape(x)+'</th>' for x in rows[0])+'</tr></thead><tbody>'
        table+=''.join('<tr>'+''.join('<td>'+html.escape(x)+'</td>' for x in row)+'</tr>' for row in rows[1:])+'</tbody>'
        doc='<!doctype html><html><meta charset="utf-8"><style>body{font:15px/1.45 Arial;color:#16334b;margin:35px}h1{font-size:28px}table{border-collapse:collapse;width:100%;table-layout:auto}th,td{border:1px solid #cdd8e2;padding:10px;text-align:left;vertical-align:top}th{background:#dfeaf3}tr:nth-child(even){background:#f5f8fa}.note{padding:14px;background:#fff4d6;margin:20px 0}</style><h1>'+html.escape(title)+'</h1><p>University LMS · Talal Ahmad (@talalahmad-ai) · Prepared 12 November 2026</p><div class="note">LOCAL ARTIFACT RENDERING · Source: reports/'+source+' · Proposed plan; official deadlines unconfirmed. This is not a GitHub screenshot.</div><table>'+table+'</table></html>'
        page.set_viewport_size({'width':2100 if 'risks' in filename else 1600,'height':1100})
        page.set_content(doc);page.screenshot(path=str(E/filename),full_page=True)
        record(filename,'reports/'+source,'Actual browser rendering of local CSV artifact')
    browser.close()
(E/'capture-manifest.json').write_text(json.dumps({'captured_at_utc':now(),'captures':records},indent=2)+'\n')
print(json.dumps([{'file':x['file'],'kind':x['kind'],'error':x.get('error')} for x in records],indent=2))
