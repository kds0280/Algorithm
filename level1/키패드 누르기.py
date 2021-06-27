#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def distance(pos, num, hand, L_memory, R_memory):
    L_distance = abs(pos[num][0]-pos[L_memory][0]) + abs(pos[num][1]-pos[L_memory][1])
    R_distance = abs(pos[num][0]-pos[R_memory][0]) + abs(pos[num][1]-pos[R_memory][1])
    if L_distance == R_distance:
        return 'L' if hand == "left" else 'R'
    return 'L' if L_distance < R_distance else 'R'

def solution(numbers, hand):
    position = {1:[0,0],2:[0,1],3:[0,2],
                   4:[1,0],5:[1,1],6:[1,2],
                   7:[2,0],8:[2,1],9:[2,2],
                   '*':[3,0],0:[3,1],'#':[3,2],}
    L_memory = '*'
    R_memory = '#'
    answer = ""
    
    for num in numbers:
        if num in [1,4,7]:
            answer += "L"
            L_memory = num
        elif num in [3,6,9]:
            answer += "R"
            R_memory = num
        else:
            answer += distance(position, num, hand, L_memory, R_memory)
            if answer[-1] == 'L':
                L_memory = num
            else:
                R_memory = num

    return answer

