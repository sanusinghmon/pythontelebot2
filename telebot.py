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
  base_url = 'https://api.telegram.org/()/sendMessage?chat_id=()&text={} '.format(messages[i])
  string="'messages'"
  output=eval(string)
  requests.get(base_url,output) 
  
  time.sleep(randint(30))
  


