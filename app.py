from flask import Flask, request,send_file,render_template
import os
import hashlib
import datetime
import csv
import pandas as pd

def read_csv_and_get_unique_values(file_path, column_name):
    unique_values = set()  # 使用集合来保存唯一值

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # 假设 CSV 文件的列名为 'a' 和 'b'，可以根据实际情况调整
            value = row[column_name]
            unique_values.add(value)

    return list(unique_values)


app = Flask(__name__)

@app.route('/')
def index():
    # 读取CSV文件
    df = pd.read_csv('data.csv',encoding='gbk')  # 请替换为你的CSV文件路径

    # 将数据转换为HTML表格
    table_html = df.to_html(classes='table table-bordered table-striped', index=False)

    with open('data.csv', 'r', encoding='gbk') as file:
    # 使用readlines()方法读取所有行，并使用len()函数获取行数
        lines = file.readlines()
        num_lines = len(lines)
    unique_values_b = read_csv_and_get_unique_values('data.csv', 'MAC地址')

    # 渲染模板并传递表格HTML
    return render_template('index.html', table=table_html,num=int(num_lines)-1,shixian=len(unique_values_b))


@app.route('/upload', methods=['POST'])
def upload_text():
    text_data = request.data.decode('utf-8')  # 解码接收到的数据
    print(text_data)
    
    # 用分号分割字符串
    split_data = text_data.split(';')

    # 将分割后的数据写入CSV文件
    with open('data.csv', 'a') as file:
        # 将数据连接为CSV格式的字符串
        csv_line = ';'.join(split_data)
        # 写入文件
        file.write(csv_line)
        file.write('\n')


    return 'Text data saved successfully'



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
