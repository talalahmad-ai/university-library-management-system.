#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python scripts/build_planning.py
python scripts/prepare_issue_drafts.py
python scripts/export_planning.py
python scripts/validate_package.py
