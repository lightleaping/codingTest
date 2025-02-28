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
