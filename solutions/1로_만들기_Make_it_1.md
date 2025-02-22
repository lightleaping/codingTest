# 1로 만들기(Make it 1)

## 문제 설명(Problem Description)
정수가 있을 때, 짝수라면 반으로 나누고, 홀수라면 1을 뺀 뒤 반으로 나누면, 마지막엔 1이 됩니다. 예를 들어 10이 있다면 다음과 같은 과정으로 1이 됩니다.

10 / 2 = 5
(5 - 1) / 2 = 2
2 / 2 = 1
위와 같이 3번의 나누기 연산으로 1이 되었습니다.

정수들이 담긴 리스트 num_list가 주어질 때, num_list의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 return하도록 solution 함수를 완성해주세요.

## 접근 방법(Approach)
1. num_list의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 저장할 변수 count를 생성 및 0으로 초기화한다.
2. num_list의 모든 원소를 인덱스로 순환하기 위해 for문을 이용한다.
3. if문을 이용하여 num_list의 원소가 짝수라면 반으로 나누고, 홀수라면 1을 뺀 뒤 반으로 나눈다. 이때 나누기 연산 시마다 count를 1 증가시킨다.
4. while문을 이용하여 해당하는 num_list의 원소가 1인 경우 반복문을 탈출한다.
5. return count

---

1. Create a variable count to store the number of division operations required to make all elements of num_list 1, and initialize it to 0.
2. Use a for loop to iterate through all elements of num_list by index.
3. Use an if statement to divide num_list by half if it is even, and divide by half if it is odd. At this time, increase count by 1 for each division operation.
4. Use a while loop to exit the loop if the corresponding element of num_list is 1.
5. return count
   
## Python 코드(Python Code)
```
def solution(num_list):
    count = 0
    for i in range(len(num_list)):
        while num_list[i] != 1:
            if num_list[i] % 2 == 0:
                num_list[i] /= 2
                count += 1
            else:
                num_list[i] = (num_list[i] - 1) / 2
                count += 1
    return count
```

## 기억할 점 (point)


[뒤로 가기](../README.md)(Go back)
