#!/usr/bin/python

import sys

def open_file(f):
    with open(f, 'r') as file:
        for fileline in file:
            line = fileline.split()

            if(line[0] == 'N'):
                num_nodes = line[1]
            elif(line[0] == 'L'):
                packet_size = line[1]
            elif(line[0] == 'R'):
                rand_num_range = line[1]
                consec_coll = []
                for i in range(2, len(line)):
                    consec_coll.append(line[i])
            elif(line[0] == 'M'):
                max_retrans = line[1]
            elif(line[0] == 'T'):
                time = line[1]
    print num_nodes
    print packet_size
    print rand_num_range
    print consec_coll
    print max_retrans
    print time
    
if __name__ == "__main__":

    if(len(sys.argv) < 2):
       print "Please enter filename"
    else:
       filename = str(sys.argv[1])
       open_file(filename)
