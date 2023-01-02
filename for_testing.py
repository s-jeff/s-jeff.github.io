import requests
headers = {'User-Agent': 'Mozilla/5.0'}
gcap = 'googlee'
payload = {'name':'logtest','email':'meeee', 'subject':'subject','message':'44ee2', 'g-recaptcha-response':'gcap'}

session = requests.Session()
x= session.post('https://script.google.com/macros/s/AKfycbwCvQNGcg15tOHA7IKrT5ani5E1k_B7cI4fLECHsH8OAzRteLBJVpbUXZAFyxdmyYi2/exec',headers=headers,data=payload)

print(x)