import gradio as gr
import requests

def show_prediction(result):
	url=f"http://host.docker.internal:8000/api?input={result}"
	response=requests.post(url).json()
	label = response.get("label")
	score = response.get("score")
	return "There is a " + f"{score:.2%}" + " probability that it is a " + label + " comment."

with gr.Blocks() as demo:
    comment = gr.Textbox(label="Please input comment here to predict if it is toxic")
    greet_btn = gr.Button("Predict")

    output = gr.Textbox(label="Result")
    
    greet_btn.click(fn=show_prediction, inputs=comment, outputs=output)


if __name__ == "__main__":
    demo.launch(server_port=7860, server_name = "0.0.0.0")