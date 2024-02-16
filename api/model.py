from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

@app.post("/api")
def getinput(input):
	print(input)
	
	# Use a pipeline as a high-level helper
	# pipe = pipeline("text-classification", model="./model")
	pipe = pipeline("text-classification", model="martin-ha/toxic-comment-model")
	
	response = pipe(input)[0]
	print(response)
	#return prediction
	return response
