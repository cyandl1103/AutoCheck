from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from FindCookie import find_cookie


# ## 자동 출첵 함수

# 쿠키로 로그인
def login(c, driver):
    try:
        driver.delete_all_cookies()
        cookies = c
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=ko-kr")   

    except:
        print("쿠키 정보가 잘못되거나 로그인 정보가 잘못되었습니다.")
        print("다시 ", end="")
        data = find_cookie()
        user = eval(data)
        login(user, driver)


# 오늘 출석일 찾아서 출석함
def check(driver):
    print("정보를 가져와 출석을 시도합니다... ...")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/p[1]/span"))
        )
    t = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/p[1]/span').text
    t = int(t) + 1
    t = str(t)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[4]/div['+t+']').click()
    print("이번 달 누적 출석체크 " + t + "일 완료!")
        
    


# ## 메인 코드 ## #

# 쿠키 읽기
f = open("cookies.txt", "r")
data = f.read()
if data == "":
    data = find_cookie()

try:
    user = eval(data)

except:
    print("잘못된 형식의 쿠키입니다.")
    print("다시 ", end="")
    data = find_cookie()
    user = eval(data)


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("headless")
driver = webdriver.Chrome(options=options)

# 로그인 페이지로 이동
driver.get("https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=ko-kr")

login(user, driver)
check(driver)
driver.quit()


