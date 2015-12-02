#!/usr/bin/python
from __future__ import division
import sys
import random
import time

class Channel:
    def __init__(self):
        self.sender = None
        self.col_count = 0

    def acquire(self, sender):
        '''
        acquire the channel, if it's already activated, return true
        '''
        if self.sender is not None:
            self.col_count += 1
            self.sender.notify_collision()
            self.sender = None
            return True

        self.sender = sender

    def release(self):
        self.sender = None

    def isIdle(self):
        return self.sender is None


class Node:
    def __init__(self, chan, rand_nums, packet_len, max_retries):
        self.rand_idx = 0
        self.rand_nums = rand_nums
        self.packet_len = packet_len
        self.max_retries = max_retries
        self.chan = chan
        self.r = None
        self.countdown = None
        self.counting = False
        self.sending = False
        self.dropped = 0
        self.col_count = 0
        self.transmit_time = 0

    def _deal_with_collision(self):
        self.col_count += 1
        self.rand_idx += 1
        self.counting = False
        self.sending = False

        if self.col_count == self.max_retries:
            # TODO
            # what do you do to rand_idx?
            self.col_count = 0
            self.dropped += 1
            self.rand_idx = 0
            self._send()
        else:
            self._send() 

    def notify_collision(self):
        assert self.sending
        self._deal_with_collision()

    def _send(self):
        self.r = (self.rand_nums[self.rand_idx]
                if self.rand_idx < len(self.rand_nums)
                else len(self.rand_nums) -1)

        self.countdown = random.randint(0, self.r)
        self.counting = True
        self.transmit_time = 0

    def tick(self):
        '''
        only call this method when the channel is idling
        '''
        if not self.counting and not self.sending:
            self._send() 
        
        if self.sending:
            # sending
            self.transmit_time += 1
            if self.transmit_time == self.packet_len:
                # TODO
                # what do happens to col_count and rand_idx

                # transmission is successful
                self.sending = False
                self.counting = False
                self.chan.release() 
        elif self.countdown > 0:
            # counting cown
            self.countdown -= 1
        else:
            # begin send
            self.counting = False
            collided = self.chan.acquire(self)

            if not collided: 
                self.sending = True
            else:
                self._deal_with_collision()


def create_nodes(chan, num_nodes, rand_nums, packet_len, max_retries):
    return [Node(chan, rand_nums, packet_len, max_retries)
            for _ in xrange(num_nodes)]


def simmulate(num_nodes, rand_nums, packet_size, max_retries, time):
    channel = Channel()
    node_list = create_nodes(channel,
            num_nodes,
            rand_nums,
            packet_size,
            max_retries)

    num_utilized = 0
    # Need to simulate clock
    #for i in xrange(time):
    #    if channel.isIdle():
    #        num_idled += 1
    #        for node in node_list:
    #            node.tick()
    #    else:
    #        channel.sender.tick()
    for i in xrange(time):
        if channel.isIdle():
            for node in node_list:
                node.tick() 
        else:
            channel.sender.tick()
            num_utilized += 1
                
    utilization = num_utilized / time
    avg = sum(n.col_count for n in node_list) / num_nodes
    var = sum((n.col_count-avg) ** 2 for n in node_list) / num_nodes

    with open("output.txt", "wb") as out:
        out.write("%.2f%%\n"% (utilization*100))
        out.write("%.2f%%\n"% ((1-utilization)*100))
        out.write("%d\n"% channel.col_count)
        out.write("%.2f\n"% var)

    return num_nodes, num_utilized, utilization, var, channel.col_count
    

def run(filename):
    with open(filename, 'r') as file:
        for fileline in file:
            line = fileline.split()

            if(line[0] == 'N'):
                num_nodes = int(line[1])
            elif(line[0] == 'L'):
                packet_size = int(line[1])
            elif(line[0] == 'R'):
                consec_coll = map(int, line[1:])
            elif(line[0] == 'M'):
                max_retries = int(line[1])
            elif(line[0] == 'T'):
                time = int(line[1])

    simmulate(num_nodes, consec_coll, packet_size, max_retries, time)


if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print "usage csma.py <filename>"
        sys.exit(1)
    else:
        filename = str(sys.argv[1])
        run(filename)
