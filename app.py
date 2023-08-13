from flask import Flask, render_template, request, jsonify
from prompts import av1, sv1

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

    result = {}

    print("="*10+" 步骤 1：正在生成 AV-1 ")
    av1_fields = av1.get_av1_fields(content, True)
    print("="*10+" 步骤 1 成功 ")
    print(av1_fields)
    result['av1Fields'] = av1_fields

    print("="*10+" 步骤 2：正在生成 SV-1 ")
    sv_classes = sv1.get_sv_classes(content)
    print("="*10+" 步骤 2 成功 ")
    print(sv_classes)

    result['svClasses'] = sv_classes

    return result


if __name__ == '__main__':
    app.run(debug=True)
