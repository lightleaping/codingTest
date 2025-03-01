def solution(myString, pat):
    idxZero = []
    lastIdx = []
    for i in range(len(myString)):
        if pat[0] == myString[i]:
            idxZero.append(i)
    for j in range(len(idxZero)):
        count = 1
        for k in range(len(pat)-1):
            if 0 <= idxZero[j]+1+k < len(myString) and myString[idxZero[j]+1+k] == pat[k+1]:
                count += 1
        if count == len(pat):
            lastIdx.append(idxZero[j]+len(pat)-1)
    answer = myString[:lastIdx[-1]+1]
    return answer
