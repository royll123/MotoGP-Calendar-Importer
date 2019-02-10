import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

dict_month = {
    "MAR" : "03",
    "APR" : "04",
    "MAY" : "05",
    "JUN" : "06",
    "JUL" : "07",
    "AUG" : "08",
    "SEP" : "09",
    "OCT" : "10",
    "NOV" : "11"
}

driver = webdriver.Chrome(executable_path="/mnt/d/Workspace/MotoGP/chromedriver.exe")
actions = ActionChains(driver)

driver.get('http://www.motogp.com/en/calendar')

time.sleep(3)
actions.move_to_element(driver.find_element_by_xpath('//*[@id="banner_big"]/nav/div[1]')).perform()
driver.find_element_by_xpath('//*[@id="banner_big"]/nav/div[1]/span/ul/li[2]/a').click()

time.sleep(1)

events = driver.find_elements_by_css_selector('.event_container.col-xs-12.col-sm-6.col-md-4.col-lg-3')
output = 'Subject,Start Date\n'

for event in events:
    day = event.find_element_by_class_name("event_day").text
    month = event.find_element_by_class_name("event_month").text
    title = event.find_element_by_class_name("event_name").text
    if title != "":
        output += 'MotoGP'+title+','+ dict_month[month] + '/' + day +'/2019\n'

with open('motogp_calendar.csv', mode="w") as f:
    f.write(output)

driver.quit()

