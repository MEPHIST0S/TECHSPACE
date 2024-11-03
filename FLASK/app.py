from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return "Hello"

@app.route('/about/')
def about_page():
    return "Page_INFO"

@app.route('/blogs/')
def page_blogs():
    blogs = [
        {"ID": 1}, 
        {"ID": 2},
        {"ID": 3}
    ]
    return blogs

if __name__ == "__main__":
    app.run(debug=True)