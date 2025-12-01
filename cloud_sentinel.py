import requests
import random
from datetime import datetime
import os

print("☁️ 云端哨兵启动...")

# --- 1. 配置区域 ---
TARGET_ASSET = "BTC-USD"
# 设定一个报警阈值 (假设比特币跌破 98000)
ALERT_PRICE = 98000

# --- 2. 核心功能 ---
def get_price():
    # 模拟获取价格 (因为 GitHub 服务器有时候访问 Yahoo 也会受限，我们用随机数模拟最稳)
    # 真实项目中可以用 requests 访问 API
    price = random.uniform(95000, 100000)
    return round(price, 2)

def run_check():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_price = get_price()
    
    print(f"[{now}] 检查目标: {TARGET_ASSET}")
    print(f"当前价格: ${current_price:,.2f}")
    
    # 逻辑判断
    if current_price < ALERT_PRICE:
        print("🚨 触发警报！价格过低！")
        # 在真实项目中，这里会调用发邮件的代码
        # 为了演示，我们把警报写入一个文件，作为证据
        with open("alert_log.txt", "a") as f:
            f.write(f"[{now}] ALERT! {TARGET_ASSET} dropped to ${current_price}\n")
    else:
        print("✅ 价格正常。")

if __name__ == "__main__":
    run_check()