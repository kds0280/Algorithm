#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T':3}
    option = {'': 1, '*':2, '#':-1}
    
    rgx = re.compile('(\d+)([SDT])([*#]?)')
    dart = rgx.findall(dartResult)
    
    for i in range(len(dart)):
        if i>0 and dart[i][2] == "*":
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    answer = sum(dart)
    return answer

