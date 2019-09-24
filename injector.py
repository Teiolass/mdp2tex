def inject(intro, main, temp_path):
    txt = ''
    with open(temp_path, 'r') as temp:
        for line in temp:
            line = line.replace('{INTRO}', intro)
            line = line.replace('{MAIN}', main)
            txt += line
    return txt
