from flask import Flask, request
 
app = Flask(__name__)
 
@app.route("/getname", methods=['GET'])
def say_hello():
    name = request.args.get('name')
    return "Hello "+name
 
if __name__ == '__main__':
    app.run()