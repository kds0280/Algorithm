#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(a, b):
    month = {1:31, 2:29, 3:31, 4:30,  5:31, 6:30, 
             7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    #1. a를 보고 이전 달들의 날짜를 더한다.
    for key, value in month.items():
        if key < a:
            b += value
        
    #2. b를 7로 나눈 나머지에 따라 요일을 반환한다.
    answer = {
        0: "THU",
        1: "FRI",
        2: "SAT",
        3: "SUN",
        4: "MON",
        5: "TUE",
        6: "WED"
    }.get(b%7)
    
    return answer

