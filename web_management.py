from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome();

#def match_finder(team):
driver.get("http://arenavision.us/guide")
team = "GIRONA"

#cosa = driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/table/tbody/tr[{i}]/td[5]".format(i=2))
#texto_cosa = cosa.text

for i in range(2,81):
    if (i == 9 ):
        print ("Publi")
    else:
        match = driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/table/tbody/tr[{}]/td[5]".format(i))
        match_tittle = match.text
        if (match_tittle.find(team) != -1):
            channels = driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/table/tbody/tr[{}]/td[6]".format(i))
            print(channels.text)
            driver.quit()

"""if (texto_cosa.find(team) != -1):
    print(cosa.text)
else:
    print("Nop")"""









