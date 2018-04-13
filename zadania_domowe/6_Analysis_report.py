'''
Write a script which:
1. asks the user for a path to an input file,
2. reads data from this file into memory,
3. in a loop, asks the user for a word until he or she provides an empty string,
•every time the user provides a non-empty word, the percentage of lines of the input file containing this word is printed
4. finally, if at least one non-empty word was provided, asks the user for a path of an output file to write the report to:
•if the provided path is a non-empty string, write to the file,
so that every line contains one of the provided words followed by the calculated percentage.
'''

#input_path = input('Provide a path to an input file: ')
input_path = '.\\6_Analysis_report_FILES\\twinkle.txt'

list_of_words_to_find = []
list_of_percentages = []

word_to_find = input('Provide a word (or hit ENTER to finish): ')
list_of_words_to_find.append(word_to_find)

if word_to_find:
    while word_to_find:
        with open(input_path, 'r', encoding='utf-8') as f:
            lines_counter = 0
            contain_counter = 0
            for line in f:
                line = line.split()
                for word in line:
                    word = word.strip(',' '.' '!')
                    if word == word_to_find:
                        contain_counter = contain_counter + 1
                        break
                lines_counter = lines_counter + 1
            percentage = str(contain_counter/lines_counter*100)
            list_of_percentages.append(percentage)
            print(percentage + '% of lines contain this word')
        word_to_find = input('Provide a word (or hit ENTER to finish): ')
        list_of_words_to_find.append(word_to_find)

    #output_path = input('Provide a path to an output file: ')
    output_path = '.\\6_Analysis_report_FILES\\twinkle_info.txt'
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            counter = 0
            for word in list_of_words_to_find:
                if word:
                    f.write(word)
                    f.write(" ")
                    f.write(list_of_percentages[counter])
                    f.write("\n")
                    counter = counter + 1
