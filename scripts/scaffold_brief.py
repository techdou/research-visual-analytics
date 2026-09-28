#!/usr/bin/env python3
"""Copy the canonical brief template without overwriting an existing file."""
import argparse
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('output',nargs='?',type=Path,default=Path('research-visual-analytics-brief.md'))
    a=p.parse_args();root=Path(__file__).resolve().parents[1]
    text=(root/'assets'/'project-brief-template.md').read_text(encoding='utf-8')
    
    try:
        with a.output.open('x',encoding='utf-8') as f: f.write(text)
    except OSError as e: p.error(str(e))
    print(a.output.resolve())
if __name__=='__main__':main()
