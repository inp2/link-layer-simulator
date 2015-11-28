#!/usr/bin/python

import sys
import random

time = 0
occupied = 0

def simulate(node_A, node_B)
    for i in range(0, time):
        countdown(node_A)

def countdown(node):
    while node > 0:
        node = node - 1

def create_nodes(rand_num_range):
    node_A = random.randint(0, int(rand_num_range))
    node_B = random.randint(0, int(rand_num_range))
    simulate(node_A, node_B)
    

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
    create_nodes(rand_num_range, time)

if __name__ == "__main__":

    if(len(sys.argv) < 2):
       print "Please enter filename"
    else:
       filename = str(sys.argv[1])
       open_file(filename)
