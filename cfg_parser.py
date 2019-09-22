needed_att = ['name', 'mode', 'mdp', 'lat_begin', 'lat_end']

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
                if val == 'void':
                    val = ''
                val = val.replace('\\n', '\n')
                val = val.replace('\\space', ' ')

                b[att] = val
        if len(b) != 0:
            b = validate_block(b)
            blocks.append(b)
        return blocks


def validate_block(b):
    for att in needed_att:
        if att not in b:
            raise Exception('{} not in block {}'.format(att, b))
    return b

