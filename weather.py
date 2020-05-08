import ssl, decimal
import urllib.request, urllib.parse, urllib.error
import json
#metaweather location url
link='https://www.metaweather.com/api/location/search/?'
link2='https://www.metaweather.com/api/location/'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#enter location
while True:
    inpu=input('Enter your location: ')
    if len(inpu)<1:
        print('no place')
        break
    inp=inpu.replace(' ','+') #replace whitespace with +
    url=link+'query='+inp
#send request,open data
    hand = urllib.request.urlopen(url, context=ctx)
    data = hand.read().decode()
#check if data in order
    try:
        js=json.loads(data)
    except:
        js=None
    #print(json.dumps(js, indent=4))
    if len(js)<1:
        print('Location <',inp,'> not found.')
        break
    else:
        #print('City ',js[0]['title'])
        #print('Where on earth id ', js[0]['woeid'])
        #print('Latt','Long',js[0]['latt_long'])

#request detailed data with woeid
        url2=link2+str(js[0]['woeid'])
        hand2=urllib.request.urlopen(url2, context=ctx)
        data2=hand2.read().decode()
        try:
            js2=json.loads(data2)
        except:
            js2=None
        if len(js2)<1:
            print('No data found.')
            break
        else:
            #print(json.dumps(js2, indent=4))
            print('Temperature in ',inpu,': ',round(js2['consolidated_weather'][0]['the_temp']), 'degrees C')
        quit()
