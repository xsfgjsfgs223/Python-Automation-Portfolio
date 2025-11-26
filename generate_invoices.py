from reportlab.pdfgen import canvas
import os
import random

print("🚀 正在伪造发票...")

# 创建存放发票的文件夹
folder = "Invoices"
if not os.path.exists(folder):
    os.makedirs(folder)

# 模拟 5 个客户数据
customers = ["Apple", "Tesla", "SpaceX", "Nvidia", "Microsoft"]

for i, client in enumerate(customers):
    # 生成随机金额
    amount = random.randint(1000, 9999)
    invoice_num = f"INV-2025-{100+i}"
    filename = f"{folder}/Invoice_{client}.pdf"
    
    # 画 PDF
    c = canvas.Canvas(filename)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, 800, "INVOICE") # 标题
    
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, f"Bill To: {client}")
    c.drawString(100, 730, f"Date: 2025-11-26")
    
    c.drawString(100, 680, "Description: Python Development Services")
    
    # 【关键数据】我们一会儿要抓取这两个东西：
    c.drawString(100, 650, f"Invoice Number: {invoice_num}")
    c.drawString(100, 630, f"Total Amount: ${amount}.00")
    
    c.save()
    print(f"✅ 已生成: {filename}")

print("素材准备完毕！")