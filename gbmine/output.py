#!/usr/bin/env python
"""
loads in data from text files

author: zach young <me@zachyoung.org>
"""

#
# source: http://codingmess.blogspot.com/2009/05/conversion-of-wavelength-in-nanometers.html
# TODO: Rewrite
def wav2RGB(wavelength):
    w = int(wavelength)

    # colour
    if w >= 380 and w < 440:
        R = -(w - 440.) / (440. - 350.)
        G = 0.0
        B = 1.0
    elif w >= 440 and w < 490:
        R = 0.0
        G = (w - 440.) / (490. - 440.)
        B = 1.0
    elif w >= 490 and w < 510:
        R = 0.0
        G = 1.0
        B = -(w - 510.) / (510. - 490.)
    elif w >= 510 and w < 580:
        R = (w - 510.) / (580. - 510.)
        G = 1.0
        B = 0.0
    elif w >= 580 and w < 645:
        R = 1.0
        G = -(w - 645.) / (645. - 580.)
        B = 0.0
    elif w >= 645 and w <= 780:
        R = 1.0
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0

    # intensity correction
    if w >= 380 and w < 420:
        SSS = 0.3 + 0.7*(w - 350) / (420 - 350)
    elif w >= 420 and w <= 700:
        SSS = 1.0
    elif w > 700 and w <= 780:
        SSS = 0.3 + 0.7*(780 - w) / (780 - 700)
    else:
        SSS = 0.0
    SSS *= 255

    return [int(SSS*R), int(SSS*G), int(SSS*B)]

import db
from datetime import date
import random
import math

# get database connection
try:
    rdb = db.connect()
except:
    print "Cound not connect do database. Cannot process."
    sys.exit()

# print the gexf introduction
print "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
print "<gexf xmlns=\"http://www.gephi.org/gexf\" xmlns:viz=\"http://www.gephi.org/gexf/viz\">"

# print graph meta
print "<meta lastmodifieddate=\"%s\">" % date.today()
print "\t<creator>Zach Young</creator>"
print "\t<description>GEXF File generated for Gutenberg Mine Project</description>"
print "</meta>"

# print graph data
print "<graph>" 
print "<attributes class=\"node\">" 
print "\t<attribute id=\"0\" title=\"nodedef\" type=\"string\"/>"
print "\t<attribute id=\"1\" title=\"label\" type=\"string\"/>"
print "\t<attribute id=\"2\" title=\"occurrences\" type=\"integer\"/>"
print "</attributes>"

# print the nodes
print "<nodes>"

threshhold = 0 # 10
idx = 0
occ_max = 70000
occ_div = 400 / math.log10(occ_max)

while True and idx < 2500:
    idx += 1
    try:
        data = rdb.hgetall("node:" + str(idx))
        if int(data['occurences']) > threshhold:

            n_occ = float(data['occurences'])
            if n_occ > occ_max:
                n_occ = occ_max

            # previous attempts
            r, g, b = wav2RGB(400 - math.log10(n_occ) * occ_div + 380)
            size = math.log(n_occ)

            print "\t<node id=\"%s\" label=\"%s\">" % (idx, data['text'])

            print "\t\t<viz:size value=\"%s\"/>" % size
            print "\t\t<viz:color b=\"%s\" g=\"%s\" r=\"%s\"/>" % (r, g, b)

            print "\t\t<attvalues>"
            print "\t\t\t<attvalue id=\"0\" value=\"node:%s\"/>" % idx
            print "\t\t\t<attvalue id=\"1\" value=\"%s\"/>" % data['text']
            print "\t\t\t<attvalue id=\"2\" value=\"%s\"/>" % data['occurences']
            print "\t\t</attvalues>"

            print "\t</node>"
        else:
            pass
    except Exception, err:
        break

print "</nodes>"

# print the edges
print "<edges>"

max_node = idx
idx = 0
edge_id = 0

while idx < max_node:
    idx += 1

    edges = rdb.keys("super_edge:node:" + str(idx) + ":node:*")

    if not edges:
        continue

    for e in range(len(edges)):
        parts = edges[e].split(":")
        # start is parts[2], end is parts[4]

        # we only need to print the node if this is in the subset we generated
        if int(parts[4]) <= max_node:
            print "\t<edge id=\"%s\" source=\"%s\" target=\"%s\"/>" % (edge_id, parts[2], parts[4])
            edge_id += 1

print "</edges>"

# close off graph and gexf
print "</graph>"
print "</gexf>"
