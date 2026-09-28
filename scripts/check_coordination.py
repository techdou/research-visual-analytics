#!/usr/bin/env python3
"""Lint coordination contract v1 structure only; does not execute or validate the application."""
import argparse,json,sys
from pathlib import Path

def lint(data):
    errors=[]
    def require(obj,keys,where):
        if not isinstance(obj,dict): errors.append(where+': expected object');return False
        for key in keys:
            value=obj.get(key)
            if value is None or value=='' or value==[] or value=={}: errors.append(where+': missing '+key)
        return True
    if not require(data,['schema_version','data_version','views','links'],'contract'):return errors
    if data.get('schema_version')!='1.0':errors.append('Unsupported schema_version')
    views=data.get('views');links=data.get('links')
    if not isinstance(views,list) or not isinstance(links,list):return errors+['views/links must be arrays']
    ids=[]
    for n,v in enumerate(views):
        if require(v,['id','grain','key'],f'view {n}'):
            if not isinstance(v.get('id'),str):errors.append(f'view {n}: ID must be string')
            else:ids.append(v['id'])
    if len(ids)!=len(set(ids)):errors.append('Duplicate view IDs')
    link_ids=[]
    for n,l in enumerate(links):
        where=f'link {n}'
        keys=['id','intent','source','target','kind','selection','mapping','operator','combine','population','invariants','empty_policy','feedback','undo','event_policy','async_policy','computation','tests']
        if not require(l,keys,where):continue
        if not isinstance(l.get('id'),str):errors.append(where+': ID must be string')
        else:link_ids.append(l['id'])
        for k in ['source','target']:
            if l.get(k) not in ids:errors.append(where+': unknown '+k)
        enums={'kind':{'identity','condition','comparison','derivation','parameter','history'},'operator':{'highlight','filter','aggregate','compare','derive','recompute'},'combine':{'replace','union','intersection','difference'},'computation':{'none','stored-query','simulation','model-execution'}}
        for k,allowed in enums.items():
            if not isinstance(l.get(k),str) or l[k] not in allowed:errors.append(where+': invalid '+k)
        selection=l.get('selection')
        if require(selection,['type','grain','key'],where+'.selection'):
            if not isinstance(selection.get('type'),str) or selection['type'] not in {'none','empty','ids','predicate','range','geometry'}:errors.append(where+': invalid selection type')
        require(l.get('mapping'),['cardinality','rule','missing'],where+'.mapping')
        require(l.get('population'),['base','denominator','self_filter'],where+'.population')
        if not isinstance(l.get('invariants'),list) or not l['invariants'] or not all(isinstance(v,str) and v.strip() for v in l['invariants']):errors.append(where+': invariants need nonempty strings')
        tests=l.get('tests')
        if not isinstance(tests,list) or not tests:errors.append(where+': tests need nonempty array')
        else:
            for j,t in enumerate(tests):require(t,['action','expected'],where+f'.test{j}')
    if len(link_ids)!=len(set(link_ids)):errors.append('Duplicate link IDs')
    return errors

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('file',type=Path);a=p.parse_args()
    try:errors=lint(json.loads(a.file.read_text(encoding='utf-8')))
    except (OSError,ValueError,TypeError) as e:errors=[str(e)]
    print(json.dumps({'structural_errors':errors,'semantic_validation':'NOT PERFORMED'},ensure_ascii=False,indent=2));return int(bool(errors))
if __name__=='__main__':sys.exit(main())
