from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="C:/Users/User/Desktop/chromedriver.exe")
driver.get("https://10fastfingers.com/advanced-typing-test/english")

sleep(30)

# Main logic of the code
word_list = driver.execute_script("return document.getElementById('wordlist').innerHTML")
words = word_list.split("|")

for word in words:
    driver.find_element_by_id("inputfield").send_keys(word +" ")
