#!/usr/bin/python

import sys
import random

class Node:
    def __init__(self, flag, backoff):
        self.flag = 0
        self.backoff = 0
        
def create_nodes(num_nodes, packet_size, rand_num_range, consec_coll, max_retrans, timew):
    print consec_coll

def open_file(filename):
    with open(filename, 'r') as file:
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
        create_nodes(num_nodes, packet_size, rand_num_range, consec_coll, max_retrans, time)

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print "usage csma.py <filename>"
    else:
        filename = str(sys.argv[1])
        open_file(filename)
