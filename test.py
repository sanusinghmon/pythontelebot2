
#! C:/Users/lenovo/AppData/Local/Programs/Python/Python310/python.exe
#test.py
# coding: utf-8
#!/usr/bin/env python
# In[ ]:
print("Content-Type: text/html")   
import cgitb 
import requests
from random import randint
import time




messages =[ 'pls refer what is the tokenomics details of skyvrse.',
            'infinite possibilities to explore in skyverse.',
            'tell me something new in skyverse project.',
            'guys new website of skyverse is interesting guys go and check.',
            'how can i explore shopping mall in skyverse project .',
            'it is a grate projct i will seen ever.']

i = 0

while i <= 6:
  if(i==6):
     i=0

  base_url = 'https://api.telegram.org/bot5413394611:AAFE_SLHcKs4orJrL3KrKBqOzlIdwEDI0nM/sendMessage?chat_id=-1001613285632&text={} '.format(messages[i])
  string="'messages'"
  output=eval(string)
  requests.get(base_url,output) 
  time.sleep(randint(60,120))
  i+=1
  
 