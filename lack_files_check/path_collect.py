def extract_directories_from_log(log_file_path, output_file_path):
    # 使用集合来避免记录重复的目录
    directories = set()

    # 读取日志文件并提取目录
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            if line.startswith("INFO:root:/data12t"):
                # 提取文件路径并解析其所在的目录
                file_path = line.split(': ')[-1].strip()
                directory = '/'.join(file_path.split('/')[:-1])
                directories.add(directory)

    # 将提取的目录写入新文件
    with open(output_file_path, 'w') as output_file:
        for directory in sorted(directories):
            output_file.write(f"{directory}\n")

# 示例用法
log_file_path = '/home/njn/work1-Transfer-Attack/ZVOS/frames_mask.log'  # 日志文件路径
output_file_path = 'ucf_remake.txt'  # 输出文件路径
extract_directories_from_log(log_file_path, output_file_path)
