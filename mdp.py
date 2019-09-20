from cfg_parser import parse_cfg 
from stack import Symstack
import re

src_path = 'f.mdp'
cfg_path = 'f.cfg'

stack = Symstack()
txt = ''

blocks = parse_cfg(cfg_path)
with open(src_path, 'r') as inp:
    for line in inp:
        els = []
        for b in blocks:
            x = [(m.start(0), m.end(0), b) for m in re.finditer(b['mdp'], line)]
        els += x
        els.sort(key=lambda x: x[0])
        nl = ''
        last = 0
        for n, e, b in els:
            s = stack.add(b)            
            if n != 0:
                nl += line[last:n]
            nl += s
            last = e
        nl += line[last:]
        txt += nl
if stack.len != 0:
    raise Exception('Error: blocks do not close')

print(txt)
            

