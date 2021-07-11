#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = re.sub('[^a-z0-9-_\.]', '', new_id)
    # 3단계
    new_id = re.sub('\.{2,}', '.', new_id)
    # 4단계
    new_id = re.sub('^\.|\.$', '', new_id)
    # 5단계
    if new_id == "":
        new_id = "a"
    # 6단계
    if len(new_id) > 15:
        new_id = new_id[0:15]
        if new_id[14] == '.':
            new_id = new_id[0:14]
    # 7단계
    elif len(new_id) < 3:
        add = new_id[-1]
        while len(new_id) < 3:
            new_id += add
    return new_id

