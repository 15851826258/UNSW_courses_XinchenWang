#import section
import csv

def viterbi_algorithm(State_File, Symbol_File, Query_File):

    #open section-state file
    state_file=open("State_File");
    #state_file_reader = [each for each in csv.DictReader(state_file, delimiter=';')]  # 这里设置分号为分隔符

    # open section-symbol file
    symbol_file = open("Symbol_File");

    # open section-query file
    query_file= open("Query_File");
    query_file_content=[]
    for line in query_file:
        line=line.strip()#remove space
        query_file_content.append(line)#append to a list that contains every line

    return 0;





#call the function
viterbi_algorithm(1,1,1);