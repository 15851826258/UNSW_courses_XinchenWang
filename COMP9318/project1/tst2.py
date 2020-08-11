# import section
import re


def viterbi_algorithm(State_File, Symbol_File, Query_File):
    # open section-state file
    # state_file = open("State_File");
    # open section-symbol file
    # symbol_file = open("Symbol_File");

    # start open section-query file
    query_file = open("Query_File");
    query_file_content = []
    for line in query_file:
        line = line.strip()  # remove space
        list = re.split(r"([ \- ,()/& ])", line)  # set the divisor
        # start remove the space and the empty element
        while ' ' in list:
            list.remove(' ')
        while '' in list:
            list.remove('')
        # end remove the space and the empty element
        print(list)  # print the ele of each line
        # end remove the space and the empty element
        query_file_content.append(list)
        # end open section-query file
    return 0;


# call the function
viterbi_algorithm(1, 1, 1);