import streamlit as st
import requests
from datetime import datetime

# --- 页面配置 ---
st.set_page_config(page_title="全球天气雷达", page_icon="🌤️")

# 标题
st.title("🌍 全球实时天气雷达")
st.caption("Powered by OpenWeatherMap API | Developed by Yang")

# --- 侧边栏：输入区 ---
st.sidebar.header("⚙️ 控制台")
city = st.sidebar.text_input("请输入城市拼音 (如 Beijing):", "Shanghai")
check_btn = st.sidebar.button("🚀 立即查询")

# --- 核心逻辑 ---
api_key = "103104f0c64435943e54807674a02704" # 你的 Key
base_url = "http://api.openweathermap.org/data/2.5/weather"

if check_btn:
    with st.spinner('正在连接卫星...'):
        try:
            # 发送请求
            url = f"{base_url}?q={city}&appid={api_key}&units=metric&lang=zh_cn"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                
                # 提取数据
                temp = data['main']['temp']
                feels_like = data['main']['feels_like']
                desc = data['weather'][0]['description']
                humidity = data['main']['humidity']
                wind = data['wind']['speed']
                icon_code = data['weather'][0]['icon'] # 获取天气图标代码
                
                # --- 展示数据 ---
                
                # 1. 显示天气图标 (从官方获取图片)
                icon_url = f"http://openweathermap.org/img/wn/{icon_code}@4x.png"
                st.image(icon_url, width=100)
                
                # 2. 显示大数字
                col1, col2, col3 = st.columns(3)
                col1.metric("当前温度", f"{temp}°C", f"体感 {feels_like}°C")
                col2.metric("湿度", f"{humidity}%")
                col3.metric("风速", f"{wind} m/s")
                
                # 3. 显示天气描述
                st.success(f"当前 {city} 的天气状况：**{desc}**")
                
                # 4. 显示原始数据 (给极客看)
                with st.expander("查看原始 JSON 数据"):
                    st.json(data)
                    
            else:
                st.error("❌ 找不到该城市，请检查拼音！")
                
        except Exception as e:
            st.error(f"网络错误: {e}")

else:
    st.info("👈 请在左侧输入城市名并点击查询")