import os
import shutil
# 要整理的文件夹，比如你的下载文件夹
download_path = r"C:\Users\你的用户名\Downloads"

# 定义文件类型和对应的目标文件夹
file_types = {
    "图片": [".jpg", ".png", ".jpeg", ".gif"],
    "文档": [".pdf", ".docx", ".txt", ".xlsx"],
    "视频": [".mp4", ".avi", ".mov"],
    "压缩包": [".zip", ".rar", ".7z"]
}
# 遍历文件夹里的所有文件
for filename in os.listdir(download_path):
    file_path = os.path.join(download_path, filename)
    # 跳过文件夹，只处理文件
    if os.path.isfile(file_path):
        # 获取文件后缀
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        # 找到对应的分类
        for folder, exts in file_types.items():
            if ext in exts:
                target_folder = os.path.join(download_path, folder)
              # 如果目标文件夹不存在，就创建它
                if not os.path.exists(target_folder):
                    os.mkdir(target_folder)
# 移动文件
                shutil.move(file_path, os.path.join(target_folder, filename))
                break
#窝来钓鱼的~
