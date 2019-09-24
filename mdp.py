from cfg_parser import parse_cfg
from stack import Symstack
import re

src_path = 'f.mdp'
cfg_path = 'f.cfg'


def simple_read(lines, blocks):
    stack = Symstack()
    for line in inp:
        els = []
        for b in blocks:
            if b['mode'] == 'brack':
                x = [(m.start(0), m.end(0), b) for m in
                        re.finditer(b['mdp'], line)]
                els += x
            if b['mode'] == 'line':
                x = [(m.start(0), m.end(0), b) for m in
                        re.finditer(b['mdp'], line)]
                if len(x) != 0:
                    last = len(line) - 1
                    x.append((last, last, b))
                els += x
            if b['mode'] == 'block':
                regex = r'\'\'\'{}\s'.format(b['mdp'])
                if re.match(regex, line):
                    els.append((0, len(line)-1, b))
        if re.match(r'\'\'\'$', line):
            els.append((0, len(line)-1, 'ENDBLOCK'))

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
        yield nl
    if stack.len != 0:
        raise Exception('Error: blocks do not close')


blocks = parse_cfg(cfg_path)
with open(src_path, 'r') as inp:
    for nl in simple_read(inp, blocks):
        print(nl, end='')
