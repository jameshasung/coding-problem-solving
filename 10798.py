words = []
length = []
for i in range(5):
    a = input()
    words.append(a)
    length.append(len(a))
    
answer = ''
for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            answer += words[j][i]
            
print(answer)
    