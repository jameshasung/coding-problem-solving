# 이진 탐색은 위치를 나타내는 변수 3개를 사용한다.
# 시작점, 끝점, 중간점
# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 방법
# 시간 복잡도는 O(logN)이다.
import sys

# 인덱스 반환


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, sys.stdin.readline().split()))
# 전체 원소 입력받기
array = list(map(int, sys.stdin.readline().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
