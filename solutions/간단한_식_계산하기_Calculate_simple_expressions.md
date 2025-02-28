# 간단한 식 계산하기 Calculate simple expressions

## 문제 설명(Problem Description)
문자열 binomial이 매개변수로 주어집니다. binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다. 주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.

## 접근 방법(Approach)
1. 변수 a, op, b 생성 및 빈 문자열로 초기화한다. 각각 음이 아닌 정수, 중간에 들어간 기호, 음이 아닌 정수 할당 예정.
2. for문으로 인덱스 i를 이용해 binomial의 한 글자씩 순회시켜 a에 추가적으로 저장한다.
3. if문 이용해서 공백 문자가 나오면(binomial[i] == ' ') i 값을 다른 변수 count에 저장하고 for문을 탈출한다.
4. binomial[count+1]을 op에 저장한다.
5. binomial[count+2]는 공백이다.
6. for문으로 인덱스 j를 이용해 binomial[count+2]부터 끝까지 순회시켜 b에 저장한다.
7. a, op, b는 모두 문자열이므로 return eval(a + op + c)

 1 2 3 + 3 4
i0 1 2 3 4 5
---

1. Create variables a, op, b and initialize them with empty strings. Each will be assigned a non-negative integer, a symbol in the middle, and a non-negative integer.
2. Use a for loop to iterate over binomial one by one using the index i and additionally store it in a.
3. Use an if statement to store the value of i in another variable count when a blank character is encountered (binomial[i] == ' ') and exit the for loop.
4. Store binomial[count+1] in op.
5. binomial[count+2] is blank.
6. Use a for loop to iterate over binomial[count+2] to the end using the index j and store it in b.
7. Since a, op, and b are all strings, return eval(a + op + c)
   
## Python 코드(Python Code)
```
def solution(binomial):
    a, op, b = '', '', ''
    for i in range(len(binomial)):
        if binomial[i] == ' ':
            count = i
            break
        a += binomial[i]
    op = binomial[count+1]
    for j in range(len(binomial[count+3:])):
        b += binomial[j+count+3]
    return eval(a + op + b)

```

## 기억할 점 (point)
SyntaxError: cannot assign to literal
-> 변수 여러 개를 한 줄에서 초기화할 때는 a, op, b = ' ', ' ', ' '

UnboundLocalError: local variable 'a' referenced before assignment
-> a = str(a)에서 a는 아직 정의되지 않음.

for j in range(len(binomial[count+2:])):
        b += binomial[j]
-> 길이를 조정했으나 더해지는 값의 인덱스는 동일하게 0부터 시작한다.

Python의 for 문에서 문자열을 순회하면 한 글자씩 접근할 수 있다.
문자열은 슬라이싱이 가능하다.
문자열은 더하기 연산자를 이용하여 연결할 수 있다.

for j in range(len(binomial[count+2:])):
        b += binomial[j+count+2]
코드 인덱스 주의하자.

슬라이싱의 마지막 요소
[start:end]에서 start부터 end-1까지 포함(즉, end 인덱스는 포함되지 않음).
[start:]처럼 end를 생략하면 start부터 끝까지 전체 포함

eval() 함수는 공백(띄어쓰기, 개행 등)을 무시하고 계산을 수행한다.
    for j in range(len(binomial[count+2:])):
        b += binomial[j+count+2]
        에서 오답 처리가 되지 않는 이유, binomial[count+2]는 공백이다.
