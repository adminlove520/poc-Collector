import os
import shutil
import sys

# 设置项目根目录为scripts目录的父目录
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 列出所有1999-2019年的文件夹
years_to_remove = list(range(1999, 2020))
folders_to_remove = []

for year in years_to_remove:
    folder_path = os.path.join(base_dir, str(year))
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        folders_to_remove.append(folder_path)

# 显示要删除的文件夹
print(f"找到以下需要删除的文件夹 ({len(folders_to_remove)}个):")
for folder in folders_to_remove:
    print(f"- {folder}")

# 确认删除
if folders_to_remove:
    confirm = input("确认要删除这些文件夹吗？(y/n): ")
    if confirm.lower() == 'y':
        for folder in folders_to_remove:
            try:
                shutil.rmtree(folder)
                print(f"已删除: {folder}")
            except Exception as e:
                print(f"删除 {folder} 时出错: {e}")
        print("删除完成!")
    else:
        print("取消删除操作。")
else:
    print("没有找到需要删除的文件夹。")