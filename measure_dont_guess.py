# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 14:14:07 2017

@author: stev
"""

1 + 1

def add(a, b):
    return(a + b)
add(4,5)

import time

def fast():
    time.sleep(0.0001)

def slow():
    time.sleep(0.1)
    
def use(func):
    for _ in range(100):
        func()

import cProfile 

profiler = cProfile.Profile()

profiler.runcall(use, fast)
profiler.print_stats()

cProfile.run('use(slow)', 'fast_stats.txt')
# 'slow' takes up very much time, makes sense to improve

