import json
import requests
import urllib.request
import urllib


url = 'https://raw.githubusercontent.com/AiyEm/newone/main/my_file.json'
r = urllib.request.urlopen(url)
f = 'hello'
data = json.dump(f, r)
print('All done !')


'''import urllib.request

webUrl=urllib.request.urlopen('https://github.com/AiyEm/newone/blob/6540e712668bf22bf52c674275bf1924d5ee08fe/my_file.json')

print("result: "+str(webUrl.getCode()))'''



'''
import urllib, json

url = "http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false"

response = urllib.urlopen(url)

data = json.loads(response.read())

print data
'''
'''
import urllib2

def main():
    webUrl = urllib2.urlopen("https://github.com/AiyEm/newone/blob/6540e712668bf22bf52c674275bf1924d5ee08fe/my_file.json")
    print("result : " + str(webUrl.getcode()))
    data = webUrl.read()
    print(data)

main()'''
