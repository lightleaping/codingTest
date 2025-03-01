# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기(Find the longest partial string ending with a specific string)

## 문제 설명(Problem Description)
문자열 myString과 pat가 주어집니다. myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.

## 접근 방법(Approach)
1. myString에서 pat[0]과 동일한 문자의 인덱스를 저장할 리스트 idxZero를 생성한다.
2. myString에 pat이 속하는 경우 myString에서의 일치하는 마지막 인덱스들을 저장할 lastIdx 리스트를 생성한다.
3. for문을 이용하여 인덱스 i로 myString을 순회시킨다.
4. for문 내에서 if문을 이용하여 pat[0]와 myString[i]이 일치하는 경우 myString 문자값의 인덱스 i를 idxZero에 추가한다.
5. 새로운 for문을 이용하여 인덱스 j를 0부터 len(idxZero)-1까지 반복시킨다.
6. for문 내에서 인덱스 k를 0부터 len(pat)-2까지 반복시킨다.
7. for문 내에서 if문으로 idxZero[j]+1+k >= 0 and myString[idxZero[j]+1+k] == pat[k+1]이면 변수 count = 1을 1 증가시킨다.(myString의 인덱스가 0이상인지 확인, myString에 pat이 일치하는 횟수 확인)(count = 1은 가장 바깥의 for문 안에 작성. idxZero[j]가 바뀔 때 초기화되어야 한다.)
8. 인덱스 k for문 바깥, 인덱스 j for문 내부에서 if문으로 count == len(pat)이면 idxZero[j]+len(pat)-1을 lastIdx에 추가한다.
9. 모든 for문 밖에서 answer = myString[:lastIdx[-1]+1]을 리턴한다.(뒤에서 값을 추가하므로 가장 긴 값을 충족하기 위한 가장 큰 인덱스 값이 마지막에 있다.)

---
1. Create a list idxZero to store the indices of characters in myString that match pat[0].
2. Create a list lastIdx to store the last indices of matching occurrences of pat in myString.
3. Use a for loop to iterate through myString with index i.
4. Inside the loop, use an if statement to check if pat[0] matches myString[i]. If they match, append index i to idxZero.
5. Use another for loop to iterate through idxZero with index j from 0 to len(idxZero) - 1.
6. Inside this loop, use another for loop to iterate through index k from 0 to len(pat) - 7. Inside this loop, use an if statement to check if idxZero[j] + 1 + k >= 0 and myString[idxZero[j] + 1 + k] == pat[k + 1]. If true, increment the variable count = 1 by 1 (ensuring that myString index is non-negative and counting the number of matching occurrences of pat in myString). (count = 1 should be declared inside the outermost loop so that it resets when idxZero[j] changes.)
8. Outside the k loop but inside the j loop, use an if statement to check if count == len(pat). If true, append idxZero[j] + len(pat) - 1 to lastIdx.
9. Outside all loops, return answer = myString[:lastIdx[-1] + 1] (since values are appended sequentially, the largest index is the last element, ensuring the longest match).

## Python 코드(Python Code)
```
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
```

## 기억할 점 (point)
런타임 에러 -> idxZero[j]+1+k 값이 myString의 길이를 넘어가면 IndexError가 발생 가능.
idxZero[j]+1+k < len(myString) 조건 추가.
if 0 <= idxZero[j]+1+k < len(myString) and myString[idxZero[j]+1+k] == pat[k+1]:
파이썬 양쪽 부등호 사용가능.

[뒤로 가기](../README.md)(Go back)
