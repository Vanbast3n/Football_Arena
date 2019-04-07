###############################################################################################################
#   Author: Vanbast3n
#   Project: Football_Arena
#   File: main.py
#
#
#
#
###############################################################################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import main_page

driver = webdriver.Chrome()
driver.get("https://arenavision.us/guide")

arena_list = main_page.MainPage(driver)
arena_list.tablemgr("MINNESOTA TIMBERWOLVES")
