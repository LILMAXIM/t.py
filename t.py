from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading

# Selenium Hub URL
hub_url = "http://216.238.78.183:4444/wd/hub"

# Test function for Chrome
def test_chrome(test_number):
    chrome_options = Options()
    # Keep browser visible (not headless)
    driver = webdriver.Remote(command_executor=hub_url, options=chrome_options)
    driver.get("https://www.google.com")
    print(f"[Chrome Test {test_number}] Page title:", driver.title)
    driver.quit()

# Create threads for 3 simultaneous Chrome tests
threads = []
for i in range(1, 4):
    t = threading.Thread(target=test_chrome, args=(i,))
    threads.append(t)

# Start all threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("All Chrome tests completed!")
