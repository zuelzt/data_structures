#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 15:28:25 2018

@author: Rorschach
@mail: 188581221@qq.com
"""
import warnings
warnings.filterwarnings('ignore')

def BinTree(data, left=None, right=None):
    return [data, left, right]

def is_empty(btree):
    return btree is None

def root(btree):
    return btree[0]

def left(btree):
    return btree[1]

def right(btree):
    return btree[2]

def set_root(btree, data):
    btree[0] = data
    
def set_left(btree, left):
    btree[1] = left
    
def set_right(btree, right):
    btree[2] = right

def num_nodes(btree): 
    def num(btree, count=0):
        if btree is None:
            pass
        else:
            for i in btree:
                if i is None:
                    pass
                else:
                    count += 1
            left = btree[1]
            count = num(left, count) 
            right = btree[2]
            count = num(right, count) 
        return count
    count = num(btree)
    return int((count+1)/2)  # 除了根结点，每个结点被计数两次
            
    


























