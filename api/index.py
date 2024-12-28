# from flask import Flask
import gradio as gr
# app = Flask(__name__)

# @app.route("/api/python")
# def hello_world():
#     return "<p>Hello, World!</p>"





# from flask import Flask
# import gradio as gr
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)
# @app.route("/python_server/healthchecker")
# def healthchecker():
#     # Définir la fonction que l'interface va utiliser
#     def to_uppercase(text):
#         return text.upper()

#     # # Créer l'interface Gradio
#     # iface = gr.Interface(
#     #     fn=to_uppercase,  # La fonction à utiliser
#     #     inputs="text",    # Le type d'entrée
#     #     outputs="text"    # Le type de sortie
#     # )
#     # import threading
#     # threading.Thread(target=iface.launch, kwargs={"server_port": 8080}, daemon=True).start()
#     return "Gradio interface launched"