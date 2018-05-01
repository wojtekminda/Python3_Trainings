directory = '.\\files\\'

file_src = 'zadanie_29_30.txt'
file_cop = 'zadanie_30_copy_no_repeatings.txt'

with open(directory + file_src, 'r') as f_src:
    with open(directory + file_cop, 'w') as f_cop:
        saved_line = ""
        for line_src in f_src:
            if line_src.rstrip('\n') != saved_line:
                f_cop.write(line_src)
            saved_line = line_src.rstrip('\n')
