def inject(attributes, temp_path):
    txt = ''
    with open(temp_path, 'r') as temp:
        for line in temp:
            for att in attributes:
                s = '\\inj{'
                s += att
                s += '}'
                line = line.replace(s, attributes[att])
            txt += line
    return txt
