from flask import Flask
 
app = Flask(__name__)
 
 
@app.route('/')
def fnc_a():
    return "rootページです"
 
 
@app.route('/sub')
def fnc_1():
    return "subページです"
 
 
if __name__ == '__main__':
    app.run()