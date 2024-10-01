
node = {
   "text": "Is it a snake?", 
   "yes": {
      "text": "It is a Python!"
   }, 
   "no": {
      "text": "It is not a Python"
   }
}

finished = False

while not finished:
    print(node['text'])
    #if len(node) == 1:
    if node =='no' or node == 'yes':
        finished = True
    else:
      answer = input()
      if answer.lower() in ['yes', 'y']:
         node = node['yes']
      else:
         node = node['no']