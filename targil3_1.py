# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 13:16:59 2022

@author: eliza
"""
import re 
n = input('please enter number: ')
file = input('please enter file name: ')

def read_line(n,file):
    try:
        if re.search('ex3_text.txt', file):
            if not n.isnumeric():
                return "invalid input detected"
            else:
                n_n = int(n)
        filehandle = open(file)
        content = filehandle.readlines()
        length = len(content)
        if n_n > length:
            return "line "+str(n_n)+" doesn't exist"
        print(content[n_n - 1])
    except:
        return "file not found"


print(read_line(n, file))