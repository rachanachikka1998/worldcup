from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#opts = Options()
#opts.set_headless()
#assert opts.headless  # Operating in headless mode

driver = webdriver.Firefox()
driver.get("http://www.espncricinfo.com/icc-cricket-world-cup-2015/content/series/509587.html?template=fixtures")
elem= Select(driver.find_element_by_xpath('//*[@id="team"]'))
elem.select_by_visible_text("India")
match=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[4]/div/div[1]/div[3]/ul/li[4]/div[2]/span[1]/a")
print(match)
wait = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div[4]/div/div[1]/div[3]/ul/li[4]/div[2]/span[1]/a"))
    )
#element = wait.until(EC.element_to_be_clickable())
match.click()
#match.click()
#driver.close()