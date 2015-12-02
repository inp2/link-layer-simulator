#!/usr/bin/python

import sys
import random
import time

class Channel:
    def __init__(self):
        self.idle = True

    def activate(self):
        self.idle = False

    def isIdle(self):
        return self.idle
class Node:
    def __init__(self, count, packet_len):
        self.count = count
        self.packet_len = packet_len

def create_nodes(num_nodes, rand_num, packet):
    node_list = []
    for i in range(num_nodes):
        x = Node(random.randint(0, rand_num), packet)
        node_list.append(x)
    return node_list

def init_simulator(num_nodes, rand_num, packet_size, time):
    channel = Channel()
    node_list = create_nodes(num_nodes, rand_num, packet_size)

    # Need to simulate clock
    for i in range(time):
        for node in node_list:
            if(channel.isIdle()):
                print node.count
                if(node.count > 0):
                    node.count = node.count - 1
                else:
                    channel.activate()
                    # Need to transmit packet
                    # Double collision count for everyone else
                    node.count 
            else:
                print 'collision'
                break

def open_file(filename):
    with open(filename, 'r') as file:
        for fileline in file:
            line = fileline.split()

            if(line[0] == 'N'):
                num_nodes = int(line[1])
            elif(line[0] == 'L'):
                packet_size = int(line[1])
            elif(line[0] == 'R'):
                rand_num_range = int(line[1])
                consec_coll = []
                for i in range(2, len(line)):
                    consec_coll.append(line[i])
            elif(line[0] == 'M'):
                max_retrans = int(line[1])
            elif(line[0] == 'T'):
                time = int(line[1])
    init_simulator(num_nodes, rand_num_range, packet_size, time)

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print "usage csma.py <filename>"
    else:
        filename = str(sys.argv[1])
        open_file(filename)
