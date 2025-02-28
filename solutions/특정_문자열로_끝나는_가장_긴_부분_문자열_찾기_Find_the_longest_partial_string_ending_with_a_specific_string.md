# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기(Find the longest partial string ending with a specific string)

## 문제 설명(Problem Description)
문자열 myString과 pat가 주어집니다. myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.

## 접근 방법(Approach)
1. myString에서 pat[0]과 동일한 문자의 인덱스를 저장할 리스트 first를 생성한다.
2. for문을 이용하여 인덱스 i로 myString을 순회시킨다.
3. for문 내에서 if문을 이용하여 pat[0]와 myString 문자값이 일치하는 경우 myString 문자값의 인덱스 i를 first에 추가한다.
4. 새로운 for문으로 first에서 원소 idx를 한 개씩 꺼낸다.
5. 내부의 if문으로 
6.  문자값이 있는 경우, while문으로 다음 인덱스의 문자값들이 서로 같을 때까지(while문 조건. 하단에서 i와 j를 계속해서 1씩 증가시킨다.) 동시에 pat의 길이가 끝나기 전까지(while문 조건. 증가시키는 j가 len(pat)-1 까지) 비교하여 동일한 경우 변수 count = 0를 1 증가시킨다.
(다음 인덱스의 문자값들이 서로 달라지는 경우 count == len(pat)를 충족할 수 없다. pat의 길이가 끝나는 경우 충족 가능하다.)
7. 
8. while문 바깥의 if문 안에 if문으로 count == len(pat)인 경우 strIdx 리스트에
9. myString[:[pat[-1]] 
10. myString에 pat이 속하는 경우들을 저장할 strIdx 리스트 생성 및 추가한다.(모든 반복문 외부에서 생성)
11. 중첩 for문으로 인덱스 j를 이용하여 pat을 순회시킨다 
12. for문으로 len(pat)를 범위로
13. pat[i+j] pat[i+len(pat)-1]
14. 의 인덱스를
15.  
16. for문으로 strIdx 리스트의 원소들이 pat[1]과 일치하는지 확인
17.  4. pat 문자가 있는지 확인
18.  pat의 문자를 순회시키며
19. 
20. 

---

1. 
   
## Python 코드(Python Code)
```

```

## 기억할 점 (point)

[뒤로 가기](../README.md)(Go back)
