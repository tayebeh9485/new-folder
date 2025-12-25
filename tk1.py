import os

# مسیر فولدر روی دسکتاپ

new_folder_path = os.path.join(
    os.path.expanduser("~"), "desktop", "folder")

# ساختن پوشه
os.mkdir(new_folder_path)
print("creat new folder", new_folder_path)
