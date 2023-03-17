import test_sample
from selenium.webdriver import Chrome
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from config_auto import toonationconfig

#------------------------------------------------------------------------------------------#
    
class Donation_testcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.toon = toonationconfig.init(browser)

    def test_textDonation(self):
        self.assertTrue(test_sample.text_donation(browser, text, cash),
         "Text_DonationError")

    def test_miniDonation(self):
        self.assertTrue(test_sample.mini_donation(browser, text, cash), 
        "Mini_DonationError")
    
    def test_videoDonation(self):
        self.assertTrue(test_sample.video_donation(browser, text, cash),
        "Youtube_donationError")
    
    def test_rouletteDonation(self):
        self.assertTrue(test_sample.roulette_donation(browser, text),
        "roulette_donationError")

    def test_questDonation(self):
        self.assertTrue(test_sample.quset_donation(browser, text, cash),
        "quest_donationError")



    # def test_miniDonation(self):
    #     self.assertTrue(test_origin.mini_donation(browser,text, cash))

   

# 메인 실행
if __name__ == '__main__':
    # browser = webdriver.Chrome('C:/chromedriver.exe')
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")
    browser = webdriver.Chrome('C:/chromedriver.exe', options=options)
    
    text = '테스트메시지_입니다'
    cash = 5000

    # unittest.main()
    suite = unittest.TestSuite([
        Donation_testcase('test_textDonation')
        # Donation_testcase('test_miniDonation'),
        # Donation_testcase('test_videoDonation'),
        # Donation_testcase('test_rouletteDonation'),
        # Donation_testcase('test_questDonation')



        # Donation_testcase('test_questDonation')
    ])
    unittest.TextTestRunner(verbosity=2).run(suite)

    

 




