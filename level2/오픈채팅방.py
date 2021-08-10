#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(record):
    state = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    ident = {}
    actions = [] 
    answer = []
    
    for sentence in record:
        s = sentence.split(" ")
        if s[0] == "Enter" or s[0]=="Change":
            ident[s[1]] = s[2]
        actions.append([s[1], s[0]])
        
    for a in actions:
        if a[1] in state:
            answer.append(ident[a[0]]+state[a[1]])
    return answer

