from glob import glob

chapter_filenames = glob("Tom_Sawyer/chapters/*.txt")
chapter_counter = 0
sorted_chapter_names = sorted(chapter_filenames)
for filename in sorted_chapter_names:
    with open(filename) as f:
        raw_text = f.read()
    by_lines = raw_text.split('\n')
    new_first = f'<chapter_number>{chapter_counter}</chapter_number>\n'
    new_second = f'<title>{by_lines[0]}</title>\n'
    body_one = '<body>\n'
    body_two = '</body>\n'
    out_text = new_first + new_second + body_one + '\n'.join(by_lines[1:]) + body_two
    # print(out_text)
    with open(f'{filename}', 'w') as f:
        f.write(out_text)
    chapter_counter += 1
