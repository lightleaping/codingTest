# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기(Find the longest partial string ending with a specific string)

## 문제 설명(Problem Description)
문자열 myString과 pat가 주어집니다. myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.

## 접근 방법(Approach)
1. myString에서 pat[0]과 동일한 문자의 인덱스를 저장할 리스트 idxZero를 생성한다.
2. myString에 pat이 속하는 경우 myString에서의 일치하는 마지막 인덱스들을 저장할 lastIdx 리스트를 생성한다.
3. for문을 이용하여 인덱스 i로 myString을 순회시킨다.
4. for문 내에서 if문을 이용하여 pat[0]와 myString 문자값이 일치하는 경우 myString 문자값의 인덱스 i를 idxZero에 추가한다.
5. 
6. while문으로 6번 문장의 if문 반복, myString[idx[k]+1]이 존재하고(idx[k]+1 < len(myString)) pat[k+1]이 존재하는(pat의 인덱스 k+1 <= len(pat)-1) 조건에만 반복한다.
7. 내부의 if문으로 myString[idxZero[k]+1] == pat[k+1]인 경우 변수 count = 1을 1 증가시킨다.
8. 
9. 9. 새로운 for문으로 k 인덱스를 이용하여 len(pat)만큼 반복한다.
10. 
11. 
12. 내부의 if문 다음 if문으로 count == len(pat)인 경우 myString이 pat과 일치하는 마지막 인덱스 idx+len(pat)-1를 lastIdx에 추가한다.
13. 모든 for문 밖에서 answer = myString[:lastIdx[-1]+1]을 리턴한다.(뒤에서 값을 추가하므로 가장 긴 값을 충족하기 위한 가장 큰 인덱스 값이 마지막에 있다.)

새로운 for문으로 first에서 원소 idx를 한 개씩 꺼낸다.
11.  문자값이 있는 경우, while문으로 다음 인덱스의 문자값들이 서로 같을 때까지(while문 조건. 하단에서 i와 j를 계속해서 1씩 증가시킨다.) 동시에 pat의 길이가 끝나기 전까지(while문 조건. 증가시키는 j가 len(pat)-1 까지) 비교하여 동일한 경우 
(다음 인덱스의 문자값들이 서로 달라지는 경우 count == len(pat)를 충족할 수 없다. pat의 길이가 끝나는 경우 충족 가능하다.)
12. 
13. while문 바깥의 if문 안에  strIdx 리스트에
14. myString[:[pat[-1]] 
15.
16. 중첩 for문으로 인덱스 j를 이용하여 pat을 순회시킨다 
17. for문으로 len(pat)를 범위로
18. pat[i+j] pat[i+len(pat)-1]
19. 의 인덱스를
20.  
21. for문으로 strIdx 리스트의 원소들이 pat[1]과 일치하는지 확인
22.  4. pat 문자가 있는지 확인
23.  pat의 문자를 순회시키며
24. 
25. 

---

1. 
   
## Python 코드(Python Code)
```

```

## 기억할 점 (point)

[뒤로 가기](../README.md)(Go back)
