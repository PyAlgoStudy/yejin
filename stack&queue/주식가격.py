# n초간 떨어지지 않았음을 보여라.
# 뒤에 몇 개가 더 오며, 몇 개가 더 올 때 까지 안 떨어지는지
# 1번 보다 작은게 오면, 1번 값 구함. 2번 보다 작은 값까지 돌려서 2번 값 구함. 
def solution(prices):
    answer = []
    len_prices = len(prices) #!!len함수도 시간을 많이 잡아먹는다! len함수 많이 안 쓰게 주의해야한다.
    for i in range(len_prices):
        cnt = 0
        if i == len_prices -1: #마지막일 때
            answer.append(0)
            break
        else:
            len_new_prices = len_prices - (i+1)
            val = prices[i+1] # 비교할 값
            for j in range(len_new_prices): #!! 이 때 prices[i+1:] 이런식으로 배열을 끊어주면, 시간소요 증가한다! 주의하기
                cnt += 1
                if prices[i] <= val: # val값보다 작으면, val값 다음 값으로!
                    if j != len_new_prices -1:
                        val = prices[j+i+2]
                    else: 
                        answer.append(cnt)
                        break
                else: #value값보다 크면 더하고 break, cnt 초기화
                    answer.append(cnt) 
                    break
    return answer