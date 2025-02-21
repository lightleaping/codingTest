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
    
