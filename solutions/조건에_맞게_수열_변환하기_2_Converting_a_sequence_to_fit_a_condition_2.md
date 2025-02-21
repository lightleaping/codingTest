# 조건에 맞게 수열 변환하기 2(Converting a sequence to fit a condition 2)

## 문제 설명(Problem Description)
정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.

이러한 작업을 x번 반복한 결과인 배열을 arr(x)라고 표현했을 때, arr(x) = arr(x + 1)인 x가 항상 존재합니다. 이러한 x 중 가장 작은 값을 return 하는 solution 함수를 완성해 주세요.

단, 두 배열에 대한 "="는 두 배열의 크기가 서로 같으며, 같은 인덱스의 원소가 각각 서로 같음을 의미합니다.

## 접근 방법(Approach)
1. 반복한 횟수를 저장할 count 변수를 생성 및 0으로 초기화, 새로운 정수 배열을 저장할 new_arr 배열을 생성한다.
2. for문으로 정수 배열 arr의 인덱스를 순환한다.
3. if문을 이용해 arr의 각 원소에 대해 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하고 다시 1을 더한다.
4. 나머지 원소들은 그대로.
5. 이를 new_arr에 추가하고 for문 바깥에서 count를 1 증가시킨다.
6. if문을 이용하여 arr과 new_arr이 일치하는지 확인한다.
7. 일치하는 경우 count-1을 리턴하고, 일치하지 않는 경우 arr에 new_arr을 대입하고 다음 배열을 담기 위해 new_arr을 빈 배열로 초기화한다.
9. 전체를 반복시키기 위해 while문을 사용한다.
---

1. Create a count variable to store the number of repetitions and initialize it to 0, and create a new_arr array to store a new integer array.
2. Loop through the indices of the integer array arr with a for loop.
3. Use an if statement to divide each element of arr by 2 if it is an even number greater than or equal to 50, and multiply it by 2 if it is an odd number less than 50, and then add 1 again.
4. Leave the remaining elements as they are.
5. Add this to new_arr and increase count by 1 outside the for loop.
6. Use an if statement to check if arr and new_arr match.
7. If they match, return count-1, and if they do not, assign new_arr to arr and initialize new_arr to an empty array to store the next array.
9. Use a while statement to repeat the entire process.
   
## Python 코드(Python Code)
```
def solution(arr):
    count = 0
    new_arr = []
    while True:
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                new_arr.append(arr[i] / 2)
            elif arr[i] < 50 and arr[i] % 2 == 1:
                new_arr.append(arr[i] * 2 + 1)
            else:
                new_arr.append(arr[i])
        count += 1
        if arr == new_arr:
            return count - 1
        else:
            arr = new_arr
            new_arr = []
    
```

## 기억할 점 (point)
파이썬에서는 == 연산자를 사용하여 두 배열(리스트, 튜플 등)이 같은지 직접 비교할 수 있다.
TypeError: 'int' object is not iterable -> 배열에 항목 추가 시 append를 사용하여야 하는데 +=을 사용하였다.
TypeError: unsupported operand type(s) for /: 'list' and 'int' -> [i] 인덱스 빠트림


[뒤로 가기](../README.md)(Go back)
