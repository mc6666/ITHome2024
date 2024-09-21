from flask import Flask, request, redirect, url_for, render_template, session
import functools, os
 
app = Flask(__name__)

# 設定 session 的金鑰
app.config['SECRET_KEY'] = os.urandom(24)

# 合格的使用者及密碼
user_store = {'michael':'1234', 'john':'12345'}

# Decorator：檢查使用者是否已經登入
def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if session.get('user', None) is None: # 使用者未登入
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required
    
@app.route("/", methods=['GET'])
@login_required
def index(): # 首頁
    return "Home Page"
    
@app.route("/hello", methods=['GET'])
@login_required
def say_hello(): # 登入後重導至本頁
    return "Hello " + session.get('user')
    
# 登入頁面及帳密檢查
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # 登入檢查
        if (request.form['username'] not in user_store.keys() or
            request.form['password'] != user_store[request.form['username']]):
            error = '帳密錯誤.'
        else: # 登入成功
            session['user'] = request.form['username']
            return redirect(url_for('say_hello')) # 重導至 say_hello 函數
    return render_template('login.html', error=error)    
 
if __name__ == '__main__':
    app.run()