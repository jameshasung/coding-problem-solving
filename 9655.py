# 1개일 때 sk 승
# 2개일 때 cy 승
# 3개일 때 sk 승
# 4개일 때 cy 승
# 5개일 때 sk 승
# 6개일 때 cy 승
import sys

n = int(sys.stdin.readline().strip())
if n % 2 == 0:
    print("CY")
else:
    print("SK")
