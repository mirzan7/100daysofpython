from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exceptions
from selenium.webdriver.edge.options import Options

edge_option = Options()
User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
Accept_Language = "en-US,en;q=0.9"
edge_option.add_argument(f"--user-get={User_Agent}")
edge_option.add_argument(f"--user-get={Accept_Language}")
driver = webdriver.ChromiumEdge()
driver.get("https://www.python.org/")
events = {}
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time ')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
for n in range(len(event_times)):
    events[n] = {
        "date":event_times[n].text,
        "event_name":event_names[n].text
    }
print(events)

