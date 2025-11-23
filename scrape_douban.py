import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

print("🚀 豆瓣电影爬虫启动...")

# 1. 制作“马甲” (请求头)
# 这行代码是欺骗服务器的关键，假装我们是 Windows 上的 Chrome 浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

movie_list = []

# 2. 循环抓取前 3 页 (每页 25 部)
# 0, 25, 50...
for i in range(0, 75, 25):
    print(f"正在抓取第 {i//25 + 1} 页...")
    
    url = f"https://movie.douban.com/top250?start={i}"
    
    # 发送请求时，带上 headers (穿上马甲)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("div", class_="item")
        
        for item in items:
            # 提取电影名 (第一个 span)
            title = item.find("span", class_="title").text
            
            # 提取评分
            rating = item.find("span", class_="rating_num").text
            
            # 提取评价人数 (去掉 '人评价' 这三个字，方便以后计算)
            people_num = item.find_all("span")[-2].text.replace("人评价", "")
            
            print(f"🎬 {title} | ⭐ {rating} | 🗣️ {people_num}")
            
            movie_list.append({
                "电影名": title,
                "评分": rating,
                "评价人数": people_num
            })
    else:
        print("❌ 被发现了！请求失败。")
    
    # 随机休息 1-3 秒，模拟人类的浏览速度，防止被封 IP
    time.sleep(random.randint(1, 3))

print("-" * 30)
print("正在保存到 Excel...")

df = pd.DataFrame(movie_list)
df.to_excel("douban_top75.xlsx", index=False)

print("🎉 搞定！文件 [douban_top75.xlsx] 已生成。")