from flask import Flask

# appという名前でFlaskのインスタンスを作成
app = Flask(__name__)

# どこで実行するか指定
@app.route('/')
def hello_world():
    
    message = "Hello World\n"
    
    return message

# どこで実行するか指定
@app.route('/bye')
def bye_earth():
    
    message = "Bye Earth\n"
    
    return message

if __name__ == '__main__':
    # 作成したappを起動
    app.run()