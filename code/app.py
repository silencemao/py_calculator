# app.py

from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data['expression']
    print(data)
    print(expression)
    try:
        result = eval(expression)  # 使用eval函数计算表达式，这里需要注意安全性
        return jsonify({ "result": result })
    except Exception as e:
        return jsonify({ "error": str(e) })


if __name__ == '__main__':
    app.run(debug=True)

