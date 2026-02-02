from flask import Flask

app = Flask("__alok__")

@app.route('/')
def home():
    return "hello from cloud pass!"

if __name__ == "__main__":
    app.run()
