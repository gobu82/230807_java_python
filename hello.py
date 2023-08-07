# 천하 제일 코드 자랑
print("Hello, World!")  # 전준형

# 오영환 test_pull_request : 랜덤메뉴뽑기
import random as rd
import time as t

# 메뉴 리스트
menu_li = ["서브웨이", "이가네한식뷔페", "서강대쌈밥"]

# 함수 정의
def today_menu() :
    n = 1
    while n <= 3:
        t.sleep(1)
        print(f"{4 - n}{'..' * n}")
        n += 1

    t.sleep(1)
    print(f"메뉴 : {rd.choice(menu_li)}")

# 함수 실행
today_menu()

print("Hello, Python!")  # 오형동

print("안녕하세요. 이제는 밥먹을 시간입니다.")
url = "https://www.naver.com"
page = urlopen(url)
soup = BeautifulSoup(page, "lxml")
print("ok")

# 오도윤
print("Difficult!!")
