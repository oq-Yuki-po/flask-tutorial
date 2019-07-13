from flask import Flask, render_template, request

# appという名前でFlaskのインスタンスを作成
app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
    # urlから直接パラメータを受け取る
    return render_template("hello.html", name=name, method="URLパラメータ")

@app.route('/param', methods=["GET","POST"])
def hello_world_with_parameter():
    
    if request.method == 'POST':
        # postのパラメータの受け取る
        name = request.form['name']
    else:
        # getのパラメータの受け取る
        name = request.args.get('name')

    return render_template("hello.html", name=name, method=request.method)


if __name__ == '__main__':
    app.run()
