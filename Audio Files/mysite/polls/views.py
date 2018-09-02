# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
import subprocess
import unicodedata
import sttClient
import fnmatch
import json
import rake
# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader




def index(request):
  if request.method=="POST":
    file1 = open('C:/Python27/APACHackathon/mysite/polls/recordings.txt', "w")
    file1.truncate()
    file1.close()
    file1 = open('C:/Python27/APACHackathon/mysite/polls/recordings.txt', "a")
    for f in request.FILES.getlist('pic'):
      print f.name
      #print f.name.index('.')
      #print f.name[:f.name.index('.')]+".flac"
      print "ffmpeg" + " -i " + f.name, f.name[:f.name.index('.')]+".flac"
      subprocess.call(["ffmpeg", "-i", f.name, f.name[:f.name.index('.')]+".flac"])
      g = f.name[:f.name.index('.')]+".flac\n"
      print g
      file1.write(g.encode('utf8'))
      
    file1.close() 
    os.system('python ./polls/sttClient.py -credentials afb4e15c-a24a-4ac6-9de9-a654543fc393:BruN5SxansII -model en-US_BroadbandModel')
	
    for filename in os.listdir('./polls/output'):
      if fnmatch.fnmatch(filename, '*.json.txt'):
        with open('./polls/output/'+filename) as data_file:    
          data = json.load(data_file)
        file2 = open('./polls/output/'+filename+'Transcript.txt', "w")
        for res in data["results"]:
          if res["final"]:
            file2.write(res["alternatives"][0]["transcript"])
        
        
     
  return render(request,'index.html')
  
  
  