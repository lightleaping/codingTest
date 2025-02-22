## A 강조하기(Emphasizing A)

주어진 문자열이 모두 대문자인지 확인: isupper()
주어진 문자열이 모두 소문자인지 확인: islower()
- 문자열에 숫자나 특수문자가 포함된 경우 무시된다.

개별 문자 대소문자 검증 코드

for char in word:
    print(f"{char}: {char.isupper()}")
