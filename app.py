import time     
import requests
import datetime
 
webhook_Url = 'https://discord.com/api/webhooks/965203153240858704/Pd_ealWDo9B-Ar7RUqpXue6JIvyQkC-IPPo9HwRwNqifR81mHnK-Oqc7RH8XfgOXNBCS'

 

 
def intruderAlert():
    
    data = {"content": "I'm the webhook for this channel"}
    response = requests.post(webhook_Url, json=data)


#Main function
def main():
    time.sleep(5)
    intruderAlert()
  
 

                    

    
