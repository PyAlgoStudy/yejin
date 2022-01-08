# n초간 떨어지지 않았음을 보여라.
# 뒤에 몇 개가 더 오며, 몇 개가 더 올 때 까지 안 떨어지는지
# 1번 보다 작은게 오면, 1번 값 구함. 2번 보다 작은 값까지 돌려서 2번 값 구함. 
def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        if i == len(prices) -1: #마지막일 때
            answer.append(0)
            break
        else:
            new_prices = prices[i+1:]
            val = prices[i+1] # 비교할 값
            for j in range(len(new_prices)):
                cnt += 1
                if prices[i] <= val: # val값보다 작으면, val값 다음 값으로!
                    if j != len(new_prices)-1:
                        val = new_prices[j+1]
                    else: 
                        answer.append(cnt)
                        break
                else: #value값보다 크면 더하고 break, cnt 초기화
                    answer.append(cnt) 
                    break
    return answer