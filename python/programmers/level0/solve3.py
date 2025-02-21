def solution(strArr):
    answer = []
    convert = ''
    for i in range(len(strArr)):
        if i % 2 == 1:
            for j in range(len(strArr[i])):
                convert += strArr[i][j].upper()
            answer.append(convert)
            convert = ''
        else:
            for j in range(len(strArr[i])):
                convert += strArr[i][j].lower()
            answer.append(convert)
            convert = ''
    return answer
