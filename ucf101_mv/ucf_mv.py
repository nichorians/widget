import os
import shutil

# 当前目录
root = '/data12t/ucf101/frames/'

dirs = [os.path.join(root,p) for p in os.listdir(root) if os.path.isdir(os.path.join(root,p))]

# 遍历当前目录下的所有文件

for file_dir in dirs:

    for filename in os.listdir(file_dir):
        # 检查是否是文件
        if os.path.isfile(os.path.join(file_dir, filename)):
            # 解析文件名，确定目标子目录
            # 假设文件名格式为：v_Mixing_g13_c04pic0016.jpg，我们要把它移动到v_Mixing_g13_c04
            parts = filename.split('pic')
            if len(parts) > 1:
                subdir_name = parts[0]
                subdir_path = os.path.join(file_dir, subdir_name)
                
                # 检查目标子目录是否存在，如果不存在则创建
                if not os.path.exists(subdir_path):
                    os.makedirs(subdir_path)
                source_path = os.path.join(file_dir, filename)
                target_path = os.path.join(subdir_path,'image_0'+parts[1])
                # 移动文件
                shutil.move(os.path.join(file_dir, filename), subdir_path)

print("文件整理完成。")
