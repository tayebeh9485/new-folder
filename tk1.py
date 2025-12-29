import os

# مسیر فولدر روی دسکتاپ

new_folder_path = os.path.join(
    os.path.expanduser("~"), "desktop", "folder")
# به جای کلمه ی فولدر (folder)در خط بالا  اسم پوشه ی مورد نظرتون رو بنویسید 
# ساختن پوشه
os.mkdir(new_folder_path)
print("creat new folder", new_folder_path)

