import pdfplumber
import os
import pandas as pd

print("💰 发票收割机启动...")

input_folder = "Invoices"
data_list = []

# 1. 遍历文件夹里所有的 PDF
for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        file_path = os.path.join(input_folder, filename)
        print(f"📄 正在读取: {filename}...")
        
        # 2. 打开 PDF
        with pdfplumber.open(file_path) as pdf:
            # 获取第一页的文字
            first_page = pdf.pages[0]
            text = first_page.extract_text()
            
            # --- 核心逻辑：像切蛋糕一样提取数据 ---
            # 我们知道数据长这样： "Total Amount: $1234.00"
            # 所以我们要按行分析
            
            invoice_num = "未知"
            amount = "0"
            
            for line in text.split('\n'):
                # 抓取订单号
                if "Invoice Number:" in line:
                    # 把 "Invoice Number: " 替换为空，剩下的就是号码
                    invoice_num = line.replace("Invoice Number:", "").strip()
                
                # 抓取金额
                if "Total Amount:" in line:
                    # 把 "Total Amount: $" 替换为空
                    amount = line.replace("Total Amount:", "").replace("$", "").strip()
            
            print(f"   👉 提取成功: 单号 {invoice_num} | 金额 ${amount}")
            
            # 存入列表
            data_list.append({
                "文件名": filename,
                "发票单号": invoice_num,
                "总金额($)": float(amount) # 转成数字，方便算总账
            })

# 3. 保存到 Excel
print("-" * 30)
df = pd.DataFrame(data_list)

# 算个总账 (给客户的小惊喜)
total_sum = df["总金额($)"].sum()
print(f"💎 所有发票总额: ${total_sum:,.2f}")

df.to_excel("Invoice_Summary_Report.xlsx", index=False)
print("✅ 汇总报表已生成: [Invoice_Summary_Report.xlsx]")