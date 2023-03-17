from asyncio import sleep
from calendar import c
from io import BufferedRWPair
from msilib.schema import Class
import string
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import telegram
from selenium.webdriver.chrome.options import Options

#------------------------------------------------------------------------------------------#

def text_donation(browser: Chrome, text, cash: int):
    browser.find_element(By.XPATH, "//div[contains(text(), '텍스트')]").click()
    try:
        money = browser.find_element(By.CSS_SELECTOR, 'div._Content_3nqq5_76._Bold_3nqq5_49').text.replace(",", "")
        before_money =+ int(money)
        # name_input = browser.find_element(By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div[2]/div/div/div/div/div[1]/input')
        name_input = (By.CSS_SELECTOR, 'span.hidden:nth-child(2)')
        cash_input = browser.find_element(By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div[3]/div/div/div/div/div/input')
        content_input = browser.find_element(By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div[4]/div/div/textarea')
        donation_button = browser.find_element(By.XPATH, "//button[contains(text(), '후원하기')]")

        if before_money < cash:
            print("캐시가 부족해요옹")
            
        time.sleep(0.3)
        browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)
        try:
            name_input.clear()
            time.sleep(0.3)
            name_input.send_keys(text)
            time.sleep(1)
        except:
            pass
        cash_input.clear()
        time.sleep(0.5)
        cash_input.send_keys(cash)
        time.sleep(0.5)
        content_input.send_keys(text)
        time.sleep(0.5)
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(0.5)
        donation_button.click()
        time.sleep(1)

        after = browser.find_element(By.CSS_SELECTOR, 'div._Content_3nqq5_76._Bold_3nqq5_49').text.replace(",", "")
        after_money = int(after)
        if before_money - cash == after_money:
            print('캐시차감 확인.')
        else:
            print('캐시차감 안됨.')
    except Exception as e:
        print("???", e)
        return False
    return True

def mini_donation(browser: Chrome, text, cash: int):
    browser.find_element(By.XPATH, "//div[contains(text(), '미니후원')]").click()

    try:
        money = browser.find_element(By.CSS_SELECTOR, 'div._Content_3nqq5_76._Bold_3nqq5_49').text.replace(",", "")
        before_money =+ int(money)
        name_input = browser.find_element(By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div[2]/div/div/div/div/div[1]/input')
        cash_input = browser.find_element(By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div[3]/div/div/div/div/div/input')
        mini_contents = browser.find_element(By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div[4]/div/div/div/div/div/input')
        text_color = browser.find_element(By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div[5]/div[2]/div/div/div[2]/div[1]/div/div/div/input')
        text_color_value = browser.find_element(By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div[5]/div[2]/div/div/div[2]/div[1]/div/div/div/input')
        donation_button = browser.find_element(By.XPATH, "//button[contains(text(), '후원하기')]")

        time.sleep(0.3) 
        try:
            name_input.clear()
            time.sleep(0.3)
            name_input.send_keys(text)
            time.sleep(1)
        except:
            pass
        cash_input.clear()
        time.sleep(0.5)
        cash_input.send_keys(cash)
        time.sleep(0.5)
        mini_contents.send_keys(text)
        time.sleep(0.5)
        text_color.click()
        time.sleep(0.3)
        text_color_value.clear()
        text_color_value.send_keys('#7F2828')
        time.sleep(0.3)
        donation_button.click()
        time.sleep(1) 
        
        after = browser.find_element(By.CSS_SELECTOR, 'div._Content_3nqq5_76._Bold_3nqq5_49').text.replace(",", "")
        after_money = int(after)
        if before_money - cash == after_money:
            print('캐시차감 확인.')
        else:
            print('캐시차감 안됨.')
    except Exception as e:
        print("???", e)
        return False
    return True

def video_donation(browser: Chrome, text, cash: int):
    browser.find_element(By.XPATH, "//div[contains(text(), '영상 후원')]").click()
    youtube_url = {
        0 : 'https://www.youtube.com/watch?v=Gj3ETxehJc8',#유튜브 유료 영상
        1 : 'https://youtu.be/DqHfozzG1uI', #퍼가기 금지
        2 : 'https://www.youtube.com/watch?v=8o4Zj98FeX4', #성인영상(나이제한)
        3 : 'https://www.youtube.com/watch?v=wAsBta25OGQ', #지역락
        4 : 'https://www.youtube.com/watch?v=sLTEsCYQqkI', #비공개 영상
        5 : 'https://www.youtube.com/watch?v=oplDWPrtOOI', #유튜브 뮤직 프리미엄 전용 영상
        6 : 'https://www.youtube.com/watch?v=9ioQ5gf8atU', #채널 맴버십 가입자 전용 영상
        7 : 'https://www.youtube.com/watch?v=czRbOKANAss' #정상
    }
    try:
        money = browser.find_element(By.CSS_SELECTOR, 'div._Content_3nqq5_76._Bold_3nqq5_49').text.replace(",", "")
        before_money =+ int(money)
        browser.find_element(By.XPATH, "//div[contains(text(), '영상 후원')]").click()
        name_input = browser.find_element(By.XPATH,'//*[@id="baselayout"]/div[1]/div/div/main/div[2]/div/div/div/div/div[1]/input')
        cash_input = browser.find_element(By.XPATH,'//*[@id="baselayout"]/div[1]/div/div/main/div[3]/div/div/div/div/div/input')
        video_url = browser.find_element(By.XPATH,'//*[@id="baselayout"]/div[1]/div/div/main/div[4]/div[1]/div[1]/div/div/div[1]/div/div/input')
        donation_button = browser.find_element(By.XPATH, "//button[contains(text(), '후원하기')]")

        time.sleep(0.3) 
        try:
            name_input.clear()
            time.sleep(0.3)
            name_input.send_keys(text)
            time.sleep(1)
        except:
            pass
        cash_input.clear()
        cash_input.send_keys(cash)
        time.sleep(0.5)
        for i in range(len(youtube_url)):
            video_url.send_keys(youtube_url[i])
            time.sleep(1)
            donation_button.click()
            if i <= len(youtube_url) - 2:
                browser.implicitly_wait(4)
                browser.find_element(By.XPATH,'/html/body/div/div[2]/div/div[3]/button').click()
                time.sleep(0.3)
                video_url.clear()
        time.sleep(2)
        after = browser.find_element(By.CSS_SELECTOR, 'div._Content_3nqq5_76._Bold_3nqq5_49').text.replace(",", "")
        after_money = int(after)
        if before_money - cash == after_money:
            print('캐시차감 확인.')
        else:
            print('캐시차감 안됨.')
    except Exception as e:
        print("???", e)
        return False
    return True

def roulette_donation(browser: Chrome, text):
    browser.find_element(By.XPATH, "//div[contains(text(), '룰렛')]").click()
    try:
        money = browser.find_element(By.CSS_SELECTOR, 'div._Content_3nqq5_76._Bold_3nqq5_49').text.replace(",", "")
        before_money =+ int(money)
        name_input = browser.find_element(By.XPATH,'//*[@id="baselayout"]/div[1]/div/div/main/div[2]/div/div/div/div/div[1]/input')
        # cash = browser.find_element(By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div[5]/div/div/div/div/div/span/span[1]').text.replace(",", "")
        time.sleep(0.3) 
        try:
            name_input.clear()
            time.sleep(0.3)
            name_input.send_keys(text)
            time.sleep(1)
        except:
            pass
        browser.find_element(By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div[3]/div/div/div[1]/span[2]').click()
        time.sleep(0.3)
        browser.find_element(By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div[3]/div/div/div[2]').click()
        time.sleep(0.3)
        donation_button = browser.find_element(By.XPATH, "//button[contains(text(), '후원하기')]")
        donation_button.click()
        time.sleep(2)

        after = browser.find_element(By.CSS_SELECTOR, 'div._Content_3nqq5_76._Bold_3nqq5_49').text.replace(",", "")
        after_money = int(after)
        if before_money - 1000 == after_money:
            print('캐시차감 확인.')
        else:
            print('캐시차감 안됨.')
    except Exception as e:
        print("???", e)
        return False
    return True

def quset_donation(browser: Chrome, text, cash):
    streamer_remote = "https://toon.at/widget/controller/fda64c746fedd52aabcc1263745897f2"
    browser.find_element(By.XPATH, "//div[contains(text(), '퀘스트')]").click()
    try:
        money = browser.find_element(By.CSS_SELECTOR, 'div._Content_3nqq5_76._Bold_3nqq5_49').text.replace(",", "")
        before_money =+ int(money)
        streamer_fail = browser.find_element\
        (By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div/div[1]/div[5]/div/div/div/div/div/span/span[1]/span').text.replace(",", "")
        donator_fail = browser.find_element\
        (By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div/div[1]/div[6]/div/div/div/div/div/span/span[1]/span').text.replace(",", "")
        donator_cancel = browser.find_element\
        (By. XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div/div[1]/div[7]/div/div/div/div/div/span/span[1]/span').text.replace(",", "")
        name_input = browser.find_element(By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div/div[1]/div[2]/div/div/div/div/div[1]/input')
        quest_title = browser.find_element(By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div/div[1]/div[3]/div/div/div/div/div[1]/input')
        quest_cash = browser.find_element(By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div/div[1]/div[4]/div/div/div/div/div/input')
        # quest_time_min = browser.find_element(By.XPATH, '//*[@id="baselayout"]/div[1]/div/div/main/div/div[1]/div[8]/div/div/div/input[2]')
        donation_button = browser.find_element(By.XPATH, "//button[contains(text(), '후원하기')]")
        quest_apply = browser.find_element(By.CSS_SELECTOR, 'span.CheckboxContent')
        time.sleep(0.3) 
        for i in range(6):
            try:
                name_input.clear()
                time.sleep(0.6)
                name_input.send_keys(text)
                time.sleep(0.6)
            except:
                pass
            quest_title.send_keys(text)
            time.sleep(0.6)
            quest_cash.clear()
            time.sleep(0.6)
            quest_cash.send_keys(cash + i)
            time.sleep(0.6)
            quest_cash.click()
            if i == 0:
                quest_apply.click()
            time.sleep(0.6)
            donation_button.click()

        '''스트리머 리모컨 수락'''
        browser.execute_script(f'window.open("{streamer_remote}");')
        browser.implicitly_wait(2)
        browser.switch_to.window(browser.window_handles[2])
        browser.implicitly_wait(2)
        try:
            close_botton = browser.find_element(By.XPATH, '//*[@id="delivery-popup"]/div/div/div[1]')
            close_botton.click()
        except:
            pass
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[contains(text(), '퀘스트')]").click()
        time.sleep(0.3)
        for s in range(5):
            browser.find_element(By.XPATH, "//button[contains(text(), '수락')]").click()
            time.sleep(0.5)
        browser.find_element(By.XPATH, "//button[contains(text(), '거절')]").click()
        time.sleep(0.5)
        browser.find_element(By.XPATH, "//button[contains(text(), '성공')]").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "//button[contains(text(), '실패')]").click()
        time.sleep(1)
        browser.switch_to.window(browser.window_handles[0])
        browser.implicitly_wait(2)
        browser.find_element(By.CSS_SELECTOR, 'div.float-right').click()
        time.sleep(1)
        browser.find_element(By.XPATH, "//button[contains(text(), '성공')]").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "//button[contains(text(), '실패')]").click()
        time.sleep(1)
        browser.refresh()
        time.sleep(5)
        after = browser.find_element(By.CSS_SELECTOR, 'div._Content_3nqq5_76._Bold_3nqq5_49').text.replace(",", "")
        after_money = int(after)
        if before_money - (cash * 2) - int(streamer_fail) - int(donator_fail) - int(donator_cancel) + 5000 == after_money:
            print('캐시차감 확인.')
        else:
            print('캐시차감 안됨.')
    except Exception as e:
        print("???", e)
        return False
    return True


# 메인 실행
# if __name__ == '__main__':
#     browser = webdriver.Chrome('C:/chromedriver.exe')
#     text = '테스트메시지_입니다'
#     cash = 5000
#     text_donation(browser, text,cash)
    

 




