import json
import sys

with open('C:/Python27/speech-to-text-websockets-python-master/output/0.json') as data_file:    
  data = json.load(data_file)
  
text_file = open("Output.txt", "w")

for res in data["results"]:
	if res["final"]:
		text_file.write(res["alternatives"][0]["transcript"])
text_file.close()
			