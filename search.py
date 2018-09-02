from os import listdir
import fnmatch
import sys

with open("./result.txt", "w") as f:
  for filename in listdir("./output"):
    if fnmatch.fnmatch(filename, '*.json.txtTranscript.txt'):
      with open('./output/' + filename) as currentFile:
        text = currentFile.read()
        if (sys.argv[1] in text):
          f.write('Word ' + sys.argv[1] +' found in ' + filename[:-4] + '\n')
        else:
          f.write('Word ' + sys.argv[1] +' not found in ' + filename[:-4] + '\n')