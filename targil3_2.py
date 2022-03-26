# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:08:07 2022

@author: eliza
"""

import re
import operator
file = input('please enter file name: ')
def longest_words(file):
    try:
        if re.search('ex3_text.txt', file):
            file = open(file)
            long_word = dict()
            for line in file:
                no_dot = line.replace('.', ' ')
                no_hyphen = no_dot.replace('-', ' ')
                no_comma = no_hyphen.replace(',', ' ')
                no_open = no_comma.replace('(', ' ')
                no_close = no_open.replace(')', ' ')
                words = no_close.split()
                for word in words:
                    if word in long_word.keys():
                        continue
                    long_word[word] = long_word.get(word, 0) + len(word)

        sorted_long_word = sorted(long_word.items(), key=operator.itemgetter(1), reverse=True)
        top_5 = sorted_long_word[:5]
        list_top_5 = []
        for element in top_5:
            list_top_5.append(element[0])

        return list_top_5
    except:
        lst = []
        print("Empty list: ",lst)
        return "file not found"
         


print(longest_words(file))
      