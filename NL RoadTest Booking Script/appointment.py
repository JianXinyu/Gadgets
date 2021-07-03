from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

import time

from playsound import playsound

def fill(driver):
    first_name = driver.find_element_by_id('firstNameControl')
    first_name.send_keys('XXX')
    first_name.send_keys(Keys.ENTER)

    last_name = driver.find_element_by_id('lastNameControl')
    last_name.send_keys('XXX')
    last_name.send_keys(Keys.ENTER)
    
    email = driver.find_element_by_id('emailControl')
    email.send_keys('XXX@gmail.com')
    email.send_keys(Keys.ENTER)

    cemail = driver.find_element_by_id('confirmEmailControl')
    cemail.send_keys('XXX@gmail.com')
    cemail.send_keys(Keys.ENTER)

    phone = driver.find_element_by_id('phoneControl')
    phone.send_keys('XXX')
    phone.send_keys(Keys.ENTER)

    book_button_xpath = "//*[@id='pageScheduleDetails']/table/tbody/tr[17]/td[2]/div/a"
    book_button = driver.find_element_by_xpath(book_button_xpath)
    book_button.click()

def check(driver, location):
    # switch to iframe
    iframe = driver.find_elements_by_tag_name('iframe')[0]
    driver.switch_to.frame(iframe)
    # start booking
    button = driver.find_element_by_id("bookOrFindBook")
    button.click()

    # https://seleniumwithjavapython.wordpress.com/selenium-with-python/basics-of-webdriver/handling-dropdowns/
    s1 = Select(driver.find_element_by_id('firstSelectControl'))
    s1.select_by_visible_text(location)

    s2 = Select(driver.find_element_by_id('secondSelectControl'))
    time.sleep(1)
    try:

        s2.select_by_visible_text('Road Test - Passenger (Class 05)')

        # go to calender area
        # https://www.lambdatest.com/blog/how-to-automate-calendar-using-selenium-webdriver-for-testing/
        calender = driver.find_element_by_class_name('ui-datepicker-calendar')
        # get month
        month = driver.find_element_by_class_name('ui-datepicker-month')
    
    
        # find the first avaliable day
        day = calender.find_element_by_xpath('//td[@data-handler="selectDay"]')

        print('location: %s, time: %s %s' % (location, month.text, day.text))

        # add your own condition to auto book 
        if month.text == 'June' or (month.text == 'July' and int(day.text) <= 20):
            playsound('bell.wav')
            # don't know why I have to scroll down to click the day
            calender.location_once_scrolled_into_view
            day.click()
            # select the first avaliable time
            dtime = Select(driver.find_element_by_id('timeControl'))
            dtime.select_by_index(1)

            # Next button, not sure why other methods don't work
            next_button_xpath = "//*[@id='pageScheduleTime']/table/tbody/tr[8]/td[2]/div/a"
            next_button = driver.find_element_by_xpath(next_button_xpath)
            next_button.click()

            # fill text boxes
            fill(driver)
            time.sleep(10)

    except Exception:
        pass
    
    driver.get(driver.current_url)
    time.sleep(1)
    driver.refresh()

if __name__ == "__main__":

    driver = webdriver.Firefox(executable_path='/home/xy/Desktop/geckodriver')
    driver.get("https://www.mrdappointments.gov.nl.ca/qwebbook/index.html")

    while True:
        check(driver, 'Clarenville MRD')
        check(driver, 'Harbour Grace MRD')
        check(driver, 'Mount Pearl MRD')
        time.sleep(60)
    
    driver.close()
    
    