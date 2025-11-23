import requests
from bs4 import BeautifulSoup
import os  # 用来管理文件夹

print("🚀 图片下载器启动...")

# 1. 创建一个文件夹专门存图片
folder_name = "Book_Covers"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"✅ 已创建文件夹: {folder_name}")

# 2. 访问网站
url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 3. 找到所有书的封面图片
# 在 HTML 里，图片是 <img> 标签，它的 class 是 "thumbnail"
images = soup.find_all("img", class_="thumbnail")

print(f"🔍 找到了 {len(images)} 张图片，开始下载...")

# 4. 循环下载每一张
count = 1
for img in images:
    # 获取图片的相对路径 (例如: media/cache/...)
    img_src = img['src']
    
    # 拼接成完整的网址
    # 原网站的 src 是相对路径，我们需要把它拼在主域名后面
    full_img_url = url + img_src
    
    print(f"⬇️ 正在下载第 {count} 张: {full_img_url}")
    
    # 【核心知识点】请求图片数据 (注意是 .content 也就是二进制数据)
    img_data = requests.get(full_img_url).content
    
    # 【核心知识点】保存文件
    # 'wb' 的意思是 Write Binary (写入二进制)，专门用来存图片/视频
    with open(f"{folder_name}/cover_{count}.jpg", "wb") as f:
        f.write(img_data)
        
    count += 1

print("-" * 30)
print(f"🎉 任务完成！请去 [{folder_name}] 文件夹查看战利品。")