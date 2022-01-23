def solution(phone_book):
    #일단 짧은 것 순서대로 dict사용해서 sorting하기
    #split해서 비교 길이대로 자르기 & 비교 (뒤에 있는 것만 비교 하면 됨!)
    answer = True
    phone_book = list(map(int, phone_book))
    phone_book.sort()
    phone_book = list(map(str, phone_book))
    phone_book_len = len(phone_book)
    for i in range(len(phone_book)):
        if answer == False:
            break
        length = len(phone_book[i])
        for j in range(i+1,phone_book_len):
            if phone_book[i] == phone_book[j][:length]:
                answer = False
                break

    return answer