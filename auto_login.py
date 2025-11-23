from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print("🚀 登录机器人启动...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 1. 访问登录页面
url = "https://practicetestautomation.com/practice-test-login/"
driver.get(url)
print("✅ 已打开登录页面")
time.sleep(2)

try:
    # 2. 定位用户名框，并输入
    # (我们在浏览器按F12看到，用户名框的 id 是 'username')
    print("⌨️ 输入用户名...")
    user_box = driver.find_element(By.ID, "username")
    user_box.send_keys("student")
    
    # 3. 定位密码框，并输入
    # (密码框的 id 是 'password')
    print("🔑 输入密码...")
    pass_box = driver.find_element(By.ID, "password")
    pass_box.send_keys("Password123")
    
    # 4. 找到登录按钮，并点击
    # (按钮的 id 是 'submit')
    print("🖱️ 点击登录...")
    btn = driver.find_element(By.ID, "submit")
    btn.click()
    
    # 5. 验证是否成功
    time.sleep(3)
    # 登录成功后，网址会变，或者页面会出现 "Logged In Successfully"
    if "logged-in-successfully" in driver.current_url:
        print("🎉🎉🎉 登录成功！进入后台！")
        
        # 截图留念
        driver.save_screenshot("login_success.png")
        print("📸 成功截图已保存")
        
    else:
        print("❌ 登录失败，请检查账号密码")

except Exception as e:
    print(f"❌ 出错: {e}")

time.sleep(10)
driver.quit()