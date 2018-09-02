import json
import sys

with open('C:/Python27/speech-to-text-websockets-python-master/output/0.json.txt') as data_file:    
  data = json.load(data_file)
  

f = open('C:/Python27/speech-to-text-websockets-python-master/output/Rahul.txt', "w")
for res in data["results"]:
  if res["final"]:
    f.write(res["alternatives"][0]["transcript"])