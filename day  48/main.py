from selenium import webdriver

chrome_driver_path = "C:/Development/chromedriver-win64/chromedriver.exe"
driver = webdriver.ChromiumEdge(executable_path=chrome_driver_path)
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}
driver.get(url="https://www.amazon.com/Google-Pixel-Unlocked-Smartphone-Advanced/dp/B0CGT6RLT7?ref_=Oct_DLandingS_D_cf754241_2&th=1")

