n = int(input())  # 설탕의 무게

max_five = n // 5  # 5킬로그램 봉지 최대 개수

for i in range(max_five, -1, -1):
    remainder = n - (5 * i)  # 5킬로그램 봉지를 i개 사용하고 남은 설탕 무게

    if remainder % 3 == 0:  # 3킬로그램 봉지로 남은 설탕을 다 담을 수 있는 경우
        print(i + remainder // 3)  # 봉지의 개수 출력
        break

else:  # 조합이 불가능한 경우
    print(-1)
