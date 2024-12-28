from flask import Flask
app = Flask(__name__)
import gradio as gr

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"