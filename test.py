# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:09:14 2020

@author: xuhuaren
"""

from selenium import webdriver
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path='./drivers/chromedriver_win.exe')
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
driver.get('http://exercise.kingname.info')

