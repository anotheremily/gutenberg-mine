#!/bin/bash

# Harvest files from Project Gutenberg
wget -w 2 -m http://www.gutenberg.org/robot/harvest?filetypes[]=txt&langs[]=en
