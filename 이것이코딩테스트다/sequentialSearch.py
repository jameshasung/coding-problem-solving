# Title: 순차 탐색
# 리스트 안에 있는 특정 데이터를 찾기위해 앞에서부터 데이터를 하나씩 확인하는 방법
import sys

# 찾고자하는 위치 반환 함수


def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1


print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = sys.stdin.readline().strip().split()
n = int(input_data[0])  # 원소의 개수
target = input_data[1]  # 찾고자 하는 문자열

print("앞서 적은 원소의 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = sys.stdin.readline().strip().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
