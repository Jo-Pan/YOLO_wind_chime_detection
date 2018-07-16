#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:16:58 2018
source: https://pypi.org/project/icrawler/
@author: Pan
"""
import os
from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': './wind_chime_hanging'})
google_crawler.crawl(keyword='wind chime hanging', max_num=200)
