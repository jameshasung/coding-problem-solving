def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    # 01356
    for i in range(n):
        hindex = n - i
        if citations[i] >= hindex:
            answer = hindex
            break

    
    return answer