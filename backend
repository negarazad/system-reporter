import psutil

# بدست آوردن اطلاعات مربوط به حافظه
memory = psutil.virtual_memory()

# ایجاد یک لیست برای نمایش اطلاعات
memory_info = [
    f"حافظه خالی: {memory.available}",
    f"حافظه استفاده شده: {memory.used}",
    f"مجموع حافظه: {memory.total}"
]

# چاپ اطلاعات
for info in memory_info:
    print(info)
