def process_log_file(input_file_path, output_file_path):
    """
    读取日志文件，并将处理后的内容保存到新文件中。
    
    参数:
    - input_file_path: 日志文件的路径。
    - output_file_path: 输出文件的路径。
    """
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            # 查找以"INFO:root:"开头的行
            if line.startswith("INFO:root:"):
                # 去除前缀，获取剩余部分
                content = line[len("INFO:root:"):].strip()
                # 将处理后的内容写入到新文件中
                outfile.write(content + '\n')

# 调用函数，替换以下路径为你的文件路径
input_file_path = 'ucf_remake.txt'
output_file_path = 'ucf_selected_path.txt'
process_log_file(input_file_path, output_file_path)
