def solution(number, k):
    answer = ''
    number = list(number)
    result = []
    for n in number:
        while result and result[-1] < n and k > 0:
            result.pop()
            k -= 1
        result.append(n)
    answer = ''.join(result[:len(result) - k])  
    return answer

