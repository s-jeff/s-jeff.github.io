import requests
headers = {'User-Agent': 'Mozilla/5.0'}
gcap = ''
payload = {'name':'niceusername','email':'123456', 'subject':'','message':'', 'g-recaptcha-response':'gcap'}

session = requests.Session()
x= session.post('https://script.google.com/macros/s/AKfycbw0MEur9b_HynJjvL95GDGofBz62ofU7ZlWrVbSBWw/dev',headers=headers,data=payload)

print(x)