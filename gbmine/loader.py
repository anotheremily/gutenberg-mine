#!/usr/bin/env python
"""
loads in data from text files

author: zach young <me@zachyoung.org>
"""

import os
import db
import re
import sys
import logging

def add_text(t_fn, t_title):
    """ 
    Add a text/work to the database. 
    """
    global rdb

    # look for the text in the database. if it doesn't exist add 
    # and return the new id
    t_data = rdb.hgetall("text:" + t_fn)

    if t_data and t_data['graph_id']:
        graph_id = t_data['graph_id']
    else:
        graph_id = rdb.incr("graph_inc")
        rdb.hmset("text:" + t_fn, { 
            "graph_id": graph_id,
            "title": t_title 
        })

    return graph_id


def add_graph(g_id, g_title, g_first_edge):
    """ 
    Add a graph to the database 
    """
    global rdb

    graph_id = "graph:" + str(g_id)

    rdb.hmset(graph_id, {
        'title': g_title,
        'first_edge_id': g_first_edge
    })
    return g_id


def add_word(w_text):
    """ 
    Add a word to the database 
    """
    global rdb

    # fetch word. if it doesn't exist add and return the new id
    word_id = rdb.hgetall("word:" + w_text)

    if word_id:
        word_id = word_id['word_id']
    else:
        word_id = rdb.incr("word_inc")
        rdb.hmset("word:" + w_text, {
            "word_id": word_id
        })

    return word_id


def add_node(t_id, t_text):
    """
    Add a node/node to the database 
    Accepts one node id and the node's text. 
    Returns the node id
    """
    global rdb

    node_id = "node:" + str(t_id)

    # try to get the node. if it exists, just add 1 to occurences.
    # if it doesn't exist, create and set occurences to 1.
    data = rdb.hgetall(node_id)
    if data:
        data['occurences'] = int(data['occurences']) + 1
    else: 
        data = {
            'text': t_text,
            'occurences': 1
        }

    # try to add the edge to the database
    rdb.hmset(node_id, data)
    
    return node_id

def add_edge(graph_id, t1_id, t2_id, previous_edge = None, next_edge = None):
    """ 
    Add an edge to the database 
    Accepts two node ids. 
    Returns edge data (dictionary).
    """
    global rdb

    edge_id = "edge:" + t1_id + ":" + t2_id + ":" + str(rdb.incr("edge_inc"))

    # try to add the edge to the database
    rdb.hmset(edge_id, {
        'graph_id': graph_id,
        'src_node_id': t1_id,
        'dest_node_id': t2_id,
        'prev_edge_id': previous_edge,
        'next_edge_id': next_edge
    })
    
    return edge_id


def update_edge(e_id, next_edge):
    """
    Updates an edge with the next edge
    """
    global rdb

    data = rdb.hgetall(e_id)
    if data:
        data['next_edge_id'] = next_edge
        rdb.hmset(e_id, data)
    else:
        pass


def add_super_edge(t1_id, t2_id):
    """ 
    Add an super edge to the database 
    Accepts two node ids. 
    Returns edge data (dictionary).
    """
    global rdb

    edge_id = "super_edge:" + t1_id + ":" + t2_id 

    # try to get the edge. if it exists, just add 1 to occurences.
    # if it doesn't exist, create and set occurences to 1.
    data = rdb.hgetall(edge_id)
    if data:
        data['occurences'] = int(data['occurences']) + 1
    else: 
        data = {
            'src_node_id': t1_id,
            'dest_node_id': t2_id,
            'occurences': 1
        }

    # try to add the edge to the database
    rdb.hmset(edge_id, data)
    
    return edge_id


#
# driver code
#

base_dir = "../assets/texts/downloads/"
ext = ".txt"
regex = "A-Za-z0-9"

# get database connection
try:
    rdb = db.connect()
except:
    print "Cound not connect do database. Cannot process."
    sys.exit()

# get all the files in the search directory and loop over them.
files = os.listdir(base_dir)
file_count = 0
file_max = 1

for fn in files:
    
    # check the extension. we only want to import files of the correct type
    if len(fn) < 4 or fn[-4:] != ext:
        continue

    print "Reading:", fn

    # open file and read in data (split on whitespace)
    fh = open(base_dir + fn)
    fd = fh.read()
    
    # Strip out everything before and after:
    # *** START OF THIS PROJECT GUTENBERG EBOOK MOBY DICK ***
    # *** END OF THIS PROJECT GUTENBERG EBOOK MOBY DICK ***
    # Extract title from one of these   

    b_start = fd.find("*** START OF THIS PROJECT GUTENBERG EBOOK")
    b_end = fd.find('*** END OF THIS PROJECT GUTENBERG EBOOK')

    if b_start == -1:
        b_start = fd.find("***START OF THE PROJECT GUTENBERG EBOOK")
    if b_end == -1:
        b_end = fd.find('***END OF THE PROJECT GUTENBERG EBOOK')

    # this cuts out everything from the end and up to the very start of the *** notice
    # find the title. separate the title and the rest of the book 
    fd = fd[b_start:b_end]

    # get the title of the work
    title_end = fd.find('***', 4) + 3
    graph_title = fd[:title_end]
    graph_title = graph_title[(graph_title.find('EBOOK') + 5):-3].strip()

    # trim up the text
    fd = fd[title_end:]
    fd = fd.split("\n")

    # get the graph id
    graph_id = add_text(fn, graph_title)

    # don't get the graph. we'll overwrite it each time with the newest version
    graph = []
    prev_node = None
    node_id = None
    edge_id = None
    prev_edge_id = None
    first_edge_id = None
    node_count = 0

    # go over lines
    for line in fd:
        lp = line.split()
        
        if not lp:
            continue
        
        first = lp.pop(0)
        if re.search('[0-9]+:[0-9]+', first) == False:
            continue
        
        # go over nodes
        for node in lp:

            if not node:
                continue

            # trim the node
            node = re.sub(r'\W+', '', node.lower())

            # add node and get back the id
            node_id = add_node(add_word(node), node)

            # add edge
            if not prev_node == None:

                if not edge_id == None:
                    prev_edge_id = edge_id

                edge_id = add_edge(graph_id, prev_node, node_id, prev_edge_id)
                update_edge(prev_edge_id, edge_id)

                if first_edge_id == None:
                    first_edge_id = edge_id

                add_super_edge(prev_node, node_id)

                graph.append(edge_id)

            prev_node = node_id
            node_count += 1

            if node_count % 1000 == 0:
                print node_count, "nodes processed in file", fn

    # add the updated graph to the database
    add_graph(graph_id, graph_title, first_edge_id)

    print "graph:", graph_id, "of text", fn, "complete"

    # mark the fn as processed
    os.rename(base_dir + fn, base_dir + fn + '.processed')
    file_count += 1

    if file_count >= file_max:
        print "maximum number of files reached, exiting."
        break

print "done!", file_count, "files processed."


