# company

1. 코드 작성시 Xpath는 대책이 없을때만 사용하고, CSS_SELECTOR 사용하길 바랍니다.
2. find_element() 에서 By. 를 활용하여 Xpath, Css_selector 사용하시길 바랍니다.<br>
---X  browser.find_element_by_xpath('//div[contains(text(), '룰렛')]')<br>
---O  browser.find_element(By.XPATH, "//div[contains(text(), '룰렛')]")<br>
