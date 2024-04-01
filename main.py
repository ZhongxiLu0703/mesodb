# pip install Flask tensorflow numpy Pillow PIL

from flask import Flask, request, render_template
import numpy as np
import io

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # 返回一个上传表单
    return render_template('index.html')

if __name__ == '__main__':
    # app.run(host='10.0.0.16',port=5000,debug=True)
    app.run()
