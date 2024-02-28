from bottle import Bottle, run, template

app = Bottle()

@app.route('/')
def index():
    return "Hello, Web3py!"

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
