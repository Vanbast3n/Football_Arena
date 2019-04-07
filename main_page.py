from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasicPage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasicPage):

    def get_tittle(self):
        print(self.driver.title)

    #def channelSelector(self):

    def tablemgr(self,team):
        """Extract information about matches and channels
        Input: Team you want to see
        Output: Match & channels where you can see it
        Table Rows Range --> 2-55
        Columns used --> 5 & 6"""
        for i in range(2,56):    #
            if (i != 5):
                match_element = self.driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/table/tbody/tr[{}]/td[5]".format(i))
                if(match.find(team) != -1):
                    channel_element = self.driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/table/tbody/tr[{}]/td[6]".format(i))
                    print("{m} {c}".format(m = match_element.text, c = channel_element.text))
                    #self.driver.close()



