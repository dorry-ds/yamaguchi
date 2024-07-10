from flask import Flask, render_template , request

app = Flask(__name__, static_url_path='/static')
# @app.route('/')
# def home():
#     return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button-clicked', methods=['GET', 'POST'])
def button_clicked():
    if request.method == 'POST':
        # 处理 POST 请求的逻辑
        return 'Button clicked!'
    else:
        # 处理 GET 请求的逻辑
        return 'Please submit the form'

if __name__ == '__main__':
    app.run(debug=False)