import requests
import pandas as pd
import json

df = pd.read_csv("majina.csv") # some csv file with info you wanna auto mate pushing

link = "" #address to your db


def GenerateJson() -> "generates jsonObject":
	m = 0
	n = 1
	for _ in range(len(df)):
		jsonObj = df.iloc[m].to_json(orient="columns")
		m = n
		n+=1
		requests.post(link, json=json.loads(jsonObj))
	return jsonObj

GenerateJson()
