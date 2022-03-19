from selenium import webdriver
from selenium.webdriver.common.by import By

# 쿠키 찾기
def find_cookie():
    while True:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        d = webdriver.Chrome(options=options)

        d.get("https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=ko-kr")

        print("쿠키를 얻기 위해 다음의 정보를 입력해주세요:")

        id = input("ID: ")
        pw = input("PW: ")
        
        # 로그인 시도
        d.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[1]').click()

        d.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/form/div[1]/div/input').send_keys(id)
        d.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/form/div[2]/div/input').send_keys(pw)
        d.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/form/div[3]/button').submit()

        captcha = input("웹 상에서 캡챠를 완료한 후 'y'를 입력해주세요. [y]: ")
        if captcha == 'y':
            print()
            print()
            cookies = d.get_cookies()

            cookies_str = str(cookies)
            f = open("cookies.txt", "w")
            f.write(cookies_str)
            f.close()
            d.quit()
            return cookies_str
