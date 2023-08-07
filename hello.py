# 천하 제일 코드 자랑
print("Hello, World!")  # 전준형
print("안녕하세요. 이제는 밥먹을 시간입니다.")
url = "https://www.naver.com"
page = urlopen(url)
soup = BeautifulSoup(page, "lxml")
