import re
'''
中文分句
'''
if __name__ == '__main__':
    input_path = r'C:\Users\Administrator\Desktop\abs.txt'  # 源文件
    output_path = r'C:\Users\Administrator\Desktop\ddd.txt'  # 输出文件 
    fwd = open(output_path,'w+',encoding = 'utf-8')  
    with open(input_path,'r+',encoding = 'utf-8') as f:  # 打开文件
        for line in f:
            if ('ѿ') not in line and re.sub('\[\d+\].*\n', '', line):  # 如果不是分割行或论文文献引用格式开头的
                line = line.strip()  # 去掉首尾空格符或换行符
                line = re.sub('\u3000|\r|\t|\xa0', '', line)  # 缩进，回车，换行符 替换成''
                line = re.sub('？”|！”|。”', '”', line)  # 将？”等换成”
                line = re.sub("([。！？……])", r'\1\n', line) # 将。！？等换成换行符
                fwd.write(line) # 写入文件
    fwd.close() 关闭文件
