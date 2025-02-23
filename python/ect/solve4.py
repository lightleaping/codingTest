## 조건에 맞게 수열 변환하기 2(Converting a sequence to fit a condition 2)

두 배열이 같은지 비교
- == 연산자 사용.
두 리스트의 길이가 같고, 각 요소가 같은 순서로 동일해야 True를 반환.
리스트 안에 또 다른 리스트가 중첩된 경우에도 비교 가능.

- for문을 이용
  def arrays_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

- numpy 배열 비교
np.array_equal()

TypeError: 'int' object is not iterable
-> 배열에 항목 추가 시 append를 사용. += 연산자는 리스트와 리스트끼리만 가능.
리스트 형태로 값 추가 가능.(list += [4])

TypeError: unsupported operand type(s) for /: 'list' and 'int' -> [i] 인덱스 빠트림
리스트와 정수 간에 나누기 연산을 할 수 없다.
