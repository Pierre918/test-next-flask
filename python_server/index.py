from flask import Flask
import gradio as gr
app = Flask(__name__)

@app.route("/python_server/python")
def hello_world():
    

    def to_uppercase(text):
        return text.upper()

    # Créer l'interface Gradio
    iface = gr.Interface(
        fn=to_uppercase,  # La fonction à utiliser
        inputs="text",    # Le type d'entrée
        outputs="text"    # Le type de sortie
    )
    import threading
    threading.Thread(target=iface.launch, kwargs={"server_port": 7860}, daemon=True).start()
    return "Gradio interface launched"