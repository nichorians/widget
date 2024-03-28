使用Isomer模型提取模型背景时，发现漏了一部分视频帧

data_cmp.py用于比较两个目录，并将缺失的视频帧记录在
frames_mask.log

path_collect.py用于读取frames_mask.log并提取其中帧的目录地址，记录在
ucf_remake.txt

path_extract.py将ucf_remake.txt中的前缀部分（INFO:）去除，获得ucf_selected_path.txt

path_num.py用于确认当前目录下包含多少个子目录