def solution(numbers):
    #시간 줄일 때, 만약 맨 첫번째 숫자보다 두 번째 숫자가 작으면 길이 짧은 것이 유리
    first_num_dict = {}
    arr_len = len(numbers)
    for i in numbers:
        i = str(i) #형 변환
        first_num_dict[i] = i[0]
    first_num_dict = sorted(first_num_dict.items(), key=lambda x: x[1], reverse=True)
    
    new_arr = []
    for i in first_num_dict:
        new_arr.append(i[0])
    # ---- 새로운 배열에 첫 숫자가 큰 것들 부터 넣어주었다. ---
    arr_len = len(new_arr)
    for i in range(arr_len):
        for j in range(i+1, arr_len):
            if new_arr[i][0] == new_arr[j][0]:      
                #첫번째 숫자가 같을 때, 이렇게 비교해주기
                if int(str(new_arr[i])+str(new_arr[j])) < int(str(new_arr[j])+str(new_arr[i])):
                    j_num = new_arr[j]
                    new_arr[j] = new_arr[i]
                    new_arr[i] = j_num
            else:
                break
    
    string_ints = [str(num) for num in new_arr]
    answer = ''.join(string_ints)
    return answer