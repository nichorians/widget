from pathlib import Path

def count_second_level_directories(dir_path):
    dir_path = Path(dir_path)
    # 确保给定的路径是一个目录
    if not dir_path.is_dir():
        return 0

    second_level_directories = []

    # 遍历给定目录下的一级子目录
    for first_level_dir in dir_path.iterdir():
        if first_level_dir.is_dir():
            # 现在遍历一级子目录中的所有内容，寻找二级子目录
            for second_level_dir in first_level_dir.iterdir():
                if second_level_dir.is_dir():
                    second_level_directories.append(second_level_dir)

    # 返回二级子目录的数量
    return len(second_level_directories), second_level_directories

# 示例用法
dir_path = '/data12t/ucf101/frames'  # 当前目录
count, directories = count_second_level_directories(dir_path)

for d in directories:
    print(d)
    
print(f"Number of second level directories: {count}")
