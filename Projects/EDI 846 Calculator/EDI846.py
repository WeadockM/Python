import re
import tkinter as tk
from tkinter import filedialog

def select_document_path():
    # Opens file explorer to select document
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def calculate():
  # Running regex replaces (subs) on the document
  regex = r'^(?!Q).*'
  result = re.sub(regex, '', file, flags=re.MULTILINE)
  regex = r'(?:QTY\*V2\*|QTY\*29\*)'
  result = re.sub(regex, '', result, flags=re.MULTILINE)
  regex = r'~'
  result = re.sub(regex, '', result, flags=re.MULTILINE)
  regex = r'^\s*$\n?'
  result = re.sub(regex, '', result, flags=re.MULTILINE)
  # Split the string into a list with a delimiter of \n
  final = result.split('\n')
  # The split recognizes the trailing line and inputs a blank string into the list. Removes that blank string.
  if final[-1] == '':
     del final[-1]
  # Adds all items in the list
  sum = 0
  for item in final:
      sum += int(item)
  print(f'The total of all quantities is: {sum}')
  input('Press Enter to exit....')


path = select_document_path()

# Check if the EDI document is single or muli line
with open(path, 'r') as file:
    for i, l in enumerate(file):
      pass
    if i >= 2:
      document = open(path)
      file = document.read()
      line = document.readline()
      calculate()
    else:
      document = open(path)
      file = document.read()
      line = document.readline()
      file = file.replace('~', '~\n')
      calculate()