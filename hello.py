# 천하 제일 코드 자랑
# print("Hello, World!")  # 전준형

# 오영환 test_pull_request : 랜덤메뉴뽑기
import random as rd
import time as t

li = ["서브웨이", "이가네한식뷔페", "서강대쌈밥"]

n = 1
while n <= 3:
    t.sleep(1)
    print(f"{4 - n}{'..' * n}")
    n += 1

t.sleep(1)
print(f"메뉴 : {rd.choice(li)}")
