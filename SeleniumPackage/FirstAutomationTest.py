from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
#from webdriver_manager.microsoft import IEDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
#driver = webdriver.Ie(executable_path=IEDriverManager().install())
driver.get("https://www.diywebsite.net.au/")
driver.maximize_window()
print("Title of the page: "+driver.title)
driver.close()
