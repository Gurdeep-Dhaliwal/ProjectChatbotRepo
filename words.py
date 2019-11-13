import requests
 
parameter={"ml":"music"}
# means like 'music'
request=requests.get('https://api.datamuse.com/words',parameter)
rhyme_json=request.json()
for i in rhyme_json[0:15]:
    print(i['word'])
  

