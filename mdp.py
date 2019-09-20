from cfg_parser import parse_cfg 
from stack import Symstack

src_path = 'f.mdp'
cfg_path = 'f.cfg'

stack = Symstack()
txt = ''

blocks = parse_cfg(cfg_path)
with open(src_path, 'r') as inp:
    for line in inp:
        els = []
        for b in blocks:
            #TODO: rough here
            n = line.find(b['mdp'])
            while n != -1:
                els.append((n, b))
                n = line.find(b['mdp'], n+1)
        els.sort(key=lambda x: x[0])
        nl = ''
        last = 0
        for n, b in els:
            s = stack.add(b)            
            if n != 0:
                nl += line[last:n]
            nl += s
            last = n + len(b['mdp'])
        nl += line[last:]
        txt += nl
if stack.len != 0:
    raise Exception('Error: blocks do not close')

print(txt)
            

