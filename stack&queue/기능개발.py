def solution(progresses, speeds):
    # 일단, 최소 단위를 구한 뒤에 뒤에 숫자가 더 커질 때까지 그 숫자를 담고, 
    # 숫자들이 다 담기면 끝! 맨 마지막에 두 개 담을 수도 있으니 주의!
    answer = []
    answer_date = []
    for i in range(len(progresses)):
        diff = 100 - progresses[i]
        if diff % speeds[i] == 0:
            answer_date.append(diff//speeds[i])
        else:
            answer_date.append(diff//speeds[i] + 1)
            
    num = 0
    add_answer_num = 1
    std_num = 0
    
    if 1 == len(answer_date):
        answer=[1]
    elif 0 == len(answer_date):
        answer=[]
    else: 
        for i in range(len(answer_date)):
            if i == 0: 
                std_num = answer_date[0]
            if i != 0:
                # 전의 값보다 작거나 같을 때는 숫자를 더해준다.
                if answer_date[i] <= std_num:
                    add_answer_num += 1
                    if i+1 == len(answer_date):
                        answer.append(add_answer_num)
                else:
                    # 전의 값보다 클 때는 배열에 값을 추가한다.
                    # 여기서 허점이 있다! 꼭 여러개 누적이 된다면, 전 값보다는 클 수가 있구나!!!
                    # 즉 그 전 값만 고려해주는게 아니라 가장 작은 것이랑 비교해주어야함.
                    answer.append(add_answer_num)
                    add_answer_num = 1
                    if i+1 == len(answer_date): 
                        answer.append(1)
                    else: 
                        std_num = answer_date[i]
                
    return answer