#!/usr/bin/python

import sys
import random

class Channel:
    def __init__(self):
        self.idle = True

    def activate(self):
        self.idle = False

    def isIdle(self):
        return self.idle
class Node:
    def __init__(self, count):
        self.count = count

def create_nodes(num_nodes, rand_num):
    node_list = []
    for i in range(int(num_nodes)):
        x = Node(random.randint(0, int(rand_num)))
        node_list.append(x)
    return node_list

def init_simulator(num_nodes, rand_num, time):
    channel = Channel()
    list = create_nodes(num_nodes, rand_num)

    for i in range(int(time)):
        if(channel.isIdle):
            print 'Yes'
            
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
    init_simulator(num_nodes, rand_num_range, time)

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print "usage csma.py <filename>"
    else:
        filename = str(sys.argv[1])
        open_file(filename)
