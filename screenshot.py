from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()

# headless 옵션 설정
options.add_argument('headless')
options.add_argument("no-sandbox")

# 브라우저 윈도우 사이즈
options.add_argument('window-size=1920x1080')

# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

# 드라이버 위치 경로 입력
driver = webdriver.Chrome('/Users/user/Downloads/chromedriver')

# url을 이용하여 브라우저로 접속
url='https://splunk.linecorp.com/ko-KR/app/search/csirt_ddos_status?form.zone=*&form.message=*&form.ip=*&form.field3.earliest=-4h%40m&form.field3.latest=now'
driver.get(url)
driver.implicitly_wait(6)

# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('username').send_keys('lp12845')
driver.find_element_by_name('password').send_keys('na6994!@')

# 로그인 버튼 클릭
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/form/fieldset/input[1]').click()


# 화면 캡쳐
sleep(60)
driver.get_screenshot_as_file('/Users/user/Downloads/ddos.png')
driver.quit()


