from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parent
LEGACY=ROOT/'legacy_v31'
for path in (LEGACY,LEGACY/'v3_base'):
    if str(path) not in sys.path:sys.path.insert(0,str(path))
