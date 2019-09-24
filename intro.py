import re

def intro_read(lines):
    attributes = {}
    for line in lines:
        if 9*'-' in line:
            return attributes
        att = re.findall(r'^.*(?=:)', line)
        val = re.findall(r'(?<=").*(?=")', line)
        if len(att) != 0 and len(val) != 0:
            attributes[att[0]] = val[0]


def parse_atts(atts):
    txt = ''
    for att in atts:
        if att == 'title':
            txt += '\\title{'
            txt += atts[att]
            txt += '}\n'
        if att == 'author':
            txt += '\\author{'
            txt += atts[att]
            txt += '}\n'
    return txt
