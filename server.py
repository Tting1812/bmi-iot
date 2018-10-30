from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def server():
    return "Hello World!"

@app.route('/scan', methods = ['POST'])
def scan():
    # data = request.form 
    print(request.form)
    return "scan"

if __name__ == "__main__":
    app.run()
