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


for filename in os.listdir('./output'):
      if fnmatch.fnmatch(filename, '*.json.txt'):
        print 'python rake.py ./output/'+ filename+'Transcript.txt'
#        execfile('python ./polls/rake.py ./polls/output/'+ filename+'Transcript.txt')
        rake.load_data('./output/'+ filename+'Transcript.txt')