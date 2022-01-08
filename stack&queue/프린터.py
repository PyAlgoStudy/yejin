# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 이렇게 돌려가며 순서를 바꿔주라는 문제는 대놓고 deque를 사용하라는 의미인듯...

from collections import defaultdict, deque
import itertools   
import numpy as np

def solution(priorities, location):
    
    answer = 0 
    deq = deque(priorities)
    loc = deque(list(range(len(priorities))))
    ans = []
    for i in range(len(priorities)):
        deq_slice = deque(itertools.islice(deq, i))
        if len(deq) > 0: 
            max_num = max(deq)
            for j in deq_slice: 
                if max_num == j:
                    deq.popleft()
                    ans.append(loc.popleft())
                    break
                else:
                    deq.rotate(-1)
                    loc.rotate(-1)
                    
    for i in range(len(priorities)):
        if np.concatenate([ans, loc])[i] == location: 
            answer = 1+i    
    return answer