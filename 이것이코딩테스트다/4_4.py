import sys 

n, m = map(int, sys.stdin.readline().split())
x, y, direction = map(int, sys.stdin.readline().split())

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

visited = [[0] * m for _ in range(n)]
visited[x][y] = 1 # 현재 좌표 방문 처리

maps = []
for i in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))
    
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]   

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if visited[nx][ny] == 0 and maps[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else :
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if maps[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우 종료 
        else:
            break
        turn_time = 0
    
print(count)
    
    



