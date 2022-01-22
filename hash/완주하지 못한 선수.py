from collections import deque
import numpy as np

def solution(participant, completion):
    answer = ''
    participant_dict = {}
    
    # 순서대로 participant dict에 담고 value에는 합 담는다.
    # completion 돌면서 그 key에 하나씩 뺀다. 
    # value가 1인 값!
    for i in participant:
        if i in participant_dict.keys():
            participant_dict[i] += 1
        else: 
            participant_dict[i] = 1
            
    for i in completion:
        participant_dict[i] = participant_dict[i] - 1
        
    for key, value in participant_dict.items(): 
        if value == 1:
            answer = key
            break 
    return answer