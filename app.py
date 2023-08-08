from flask import Flask, render_template, request, jsonify
import json
#import gpt
import prompts.dodaf as dodaf
import prompts.sv1

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", title='Home')


@app.route('/upload', methods=['POST'])
def upload_file():
    # 检查是否有文件被上传
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # 如果用户没有选择文件，浏览器也会提交一个空的部分，所以需要检查文件是否存在名字
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 读取文件内容
    content = file.read().decode('utf-8')

    content = content.replace("\n", "")
    content = content.replace("\r", "")
    content = content.replace("-", "")
    content = content.replace("=", "")
    print("="*10+"正在询问gpt"+"="*10)
    # json_data = gpt.GetJson(content)
    # json_data = gpt.get_completion(dodaf.getSvClasses(content))
    json_data = prompts.sv1.getSvClasses(content)
    print("="*10+"询问完毕"+"="*10)
    print(json_data)
    return json_data


if __name__ == '__main__':
    app.run(debug=True)
