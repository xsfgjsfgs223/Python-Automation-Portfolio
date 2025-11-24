import pyautogui
import time
import os

print("🚀 桌面机器人即将启动...")
print("⚠️ 注意：程序运行期间请不要触碰鼠标和键盘！")
print("👉 紧急停止方法：把鼠标迅速甩到屏幕【左上角】")

# 1. 打开记事本 (Notepad)
# 我们用系统命令打开它
print("正在打开记事本...")
os.system("start notepad")
time.sleep(2) # 等它打开

try:
    # 2. 自动打字
    # interval=0.1 意思是每个字间隔 0.1 秒，模拟真人打字速度
    print("🤖 开始自动打字...")
    
    message = "Hello Fiverr Client!\n"
    message += "This message was typed by my Python Bot.\n"
    message += "I can automate ANY desktop application for you.\n"
    message += "Let's save 100 hours of your life!\n\n"
    message += "- Best, Yang"
    
    pyautogui.write(message, interval=0.1)
    
    # 3. 模拟按下快捷键保存 (Ctrl + S)
    print("💾 正在自动保存...")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    
    # 4. 输入文件名
    # 此时记事本弹出了保存框，我们直接打字
    pyautogui.write("robot_note.txt")
    time.sleep(1)
    
    # 5. 按回车确认
    pyautogui.press('enter')
    
    print("🎉 任务完成！文件已保存。")

except pyautogui.FailSafeException:
    print("🛑 紧急停止！你触发了故障保护。")