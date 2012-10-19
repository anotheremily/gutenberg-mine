#!/usr/bin/env python
"""
loads a graph 

author: Zach Young <young.zach@gmail.com>
"""

import db

def get_node(node_id):
    """ get the information about the current node """
    global rdb
    node = rdb.hgetall(node_id)
    return node


def get_edges(node_id):
    """ get the edges of a graph starting with node n """
    global rdb
    edges = rdb.keys("edge:" + node_id + "*")
    return edges


def get_super_edges(node_id):
    """ get the super edge starting with node n """
    global rdb

    se_ids = rdb.keys("super_edge:" + node_id + "*")
    super_edges = []
    
    if se_ids:
        for se_id in se_ids:
            super_edges.append(rdb.hgetall(se_id))
    
    return super_edges


def get_children(node_id):
    """ get the children of a current node """

    global rdb

    se_ids = rdb.keys("super_edge:" + node_id + ":*")
    children_ids = []
    
    if se_ids:
        for se_id in se_ids:
            se = rdb.hgetall(se_id)
            children_ids.append(se['dest_node_id'])
    
    return children_ids

### output

class Grapher(object):
    """ Object for handling graph display """

    printed = None
    graph = None
    cur_graph = None

    def __init__(self):
        self.printed = []
        self.graph = {}
        self.cur_graph = {}

    def print_level(self, node_ids, depth = 0, max_depth = 1):
        """ print the next level of the graph """
        if depth > max_depth:
            return 

        if depth == 0:
            pass
            # self.cur_graph.append(self.graph)
        else:
            pass

        for node_id in node_ids:
            node = get_node(node_id)

            try:
                self.printed.index(node['text'])
            except:
            
                self.indent(depth * 4)
                print node['text'], "(" + node['occurences'] + ")"
                self.printed.append(node['text'])
                self.print_level(get_children(node_id), depth + 1, max_depth)

        return
            
    def indent(self, spaces):
        """ indent text with n spaces """
        for i in range(spaces):
            print "",

### driver code

node_1 = 1042
node_2 = 138
max_depth = 1 

try:
    rdb = db.connect()

except:
    print "Cound not connect do database. Cannot process."

graph = Grapher()

graph.print_level(["node:" + str(node_1)])
