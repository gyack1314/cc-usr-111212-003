"""清点基表原行和变更批，不连接或聚合。"""
from .io import unique

def summarize(v,root):
    unique(v['left'],'row_id');unique(v['right'],'row_id')
    for b in v['batches']:
        for x in b['changes']:
            if x['table'] not in ('L','R') or x['op'] not in ('insert','delete','update'):raise ValueError('变更目标或操作非法')
    return {'left_rows':len(v['left']),'right_rows':len(v['right']),'batches':len(v['batches'])}
