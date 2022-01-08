from collections import deque

def solution(bridge_length, weight, truck_weights):
    on_brg_deq = deque()
    # 몇 개 단위로 끊을 수 있는지 부터 구하기
    # (7), (4) (4,5), (5), (6)
    # (2,3,4,5,2) 라고 하고 건너는데 다리 길이 3이다.
    # (2), (2,3), (2,3,4), (3,4), (4,5), (5,2), (5,2), (2) 
    # while문 활용 = deque의 length가 0 이 되면 멈춤
    # deque배열로 만들기 하나씩 넣어주는데, weight 가 꽉 찬 상태이면 0을 넣어주기
    cnt = 0
    on_brg_deq.append(truck_weights[0])
    nxt_truck_loc = 1
    while nxt_truck_loc < len(truck_weights) and len(truck_weights) != 1:
        if len(on_brg_deq) >= bridge_length: #시간 다 된 애들은 하나씩 계속 빼주기
            on_brg_deq.popleft()
        if nxt_truck_loc < len(truck_weights):
            if sum(on_brg_deq) + truck_weights[nxt_truck_loc] > weight:
                on_brg_deq.append(0)
                cnt += 1
            else:
                on_brg_deq.append(truck_weights[nxt_truck_loc])
                nxt_truck_loc += 1 #트럭 하나 추가
                cnt += 1
    return cnt + bridge_length +1