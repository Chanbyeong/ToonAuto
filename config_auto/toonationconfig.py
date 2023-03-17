from selenium.webdriver import Chrome
from selenium import webdriver
import time

def init(browser: Chrome):
    try:
        toon_id = ''
        '''도네이터 바이패스 입력'''
        toon_url = 'https://toon.at/donate/victoriaspakcd'
        toon_streamer_id = ''
        '''스트리머 바이패스 입력'''

        #open Bypass (vlslxm454545)
        browser.get(toon_id)
        time.sleep(1)
        browser.execute_script(f'window.open("{toon_streamer_id}");')
        time.sleep(0.5)
        browser.switch_to.window(browser.window_handles[0])
        time.sleep(1)

        browser.get(toon_url)
        time.sleep(1)
        browser.maximize_window()
    except Exception as e:
        print("아이피 화이트리스트 등록 되어있는지 확인하세요", e)
        return False
    return True


if __name__ == '__main__':
    browser = webdriver.Chrome('C:/chromedriver.exe')