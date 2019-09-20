needed_att = ['name', 'md_begin', 'md_end', 'lat_begin',
                'lat_end']

def parse_cfg(file_path):
    with open(file_path, 'r') as inp:
        blocks = []
        b = {}
        for line in inp:
            if line[0] == '#':
                continue
            elif line[0] == '[' and ']' in line:
                if len(b) != 0:
                    b = validate_block(b)
                    blocks.append(b)
                b = {}
                b['name'] = line.split(']')[0][1:]
            elif ':' in line:
                line = line.split(':')
                att = line[0]
                val = line[1]
                val = val.replace(' ', '')
                val = val.replace('\n', '')
                b[att] = val
        if len(b) != 0:
            b = validate_block(b)
            blocks.append(b)
        return blocks


def validate_block(b):
    for att in needed_att:
        if att not in b:
            raise Exception('{} not in block {}'.format(att, b))
    if 'nestable' in b:
        if b['nestable'] == 'yes':
            b['nestable'] = True
        elif b['nestable'] == 'flase':
            b['nestable'] = False
        else:
            raise Exception('In block {}, nested has not a yes/no value'.format(b[name]))
    return b


a = parse_cfg('f.cfg')
print(a)

