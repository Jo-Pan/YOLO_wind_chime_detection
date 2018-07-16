#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:45:45 2018

@author: Pan
"""

import os

imdir = 'images'
if not os.path.isdir(imdir):
    os.mkdir(imdir)

bell_folders = [name for name in os.listdir('.') if 'wind' in name]

n = 0
for folder in bell_folders:
    for imfile in os.scandir(folder):
        if 'jpg' in imfile.path: 
            os.rename(imfile.path, os.path.join(imdir, '{:06}.jpg'.format(n)))
            n += 1