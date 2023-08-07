# 천하 제일 코드 자랑
print("Hello, World!")  # 전준형

# 사용자로부터 피라미드의 높이를 입력받아 피라미드를 출력하는 Python 코드
height = int(input("피라미드의 높이를 입력하세요: "))

for i in range(1, height + 1):
    spaces = " " * (height - i)  # 공백 생성
    stars = "*" * (2 * i - 1)    # 별 생성
    print(spaces + stars)
