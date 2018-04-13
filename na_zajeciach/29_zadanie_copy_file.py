directory = '.\\files\\'

file_src = 'zadanie_29_30.txt'
file_cop = 'zadanie_29_copy.txt'

with open(directory + file_src, 'r') as f_src:
    with open(directory + file_cop, 'w') as f_cop:
        for line_src in f_src:
            f_cop.write(line_src)
