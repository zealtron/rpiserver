from bottle import route, run, redirect, post, request
import json
from bootstrap import *
from subprocess import check_output


@route('/')
def index():
    redirect("/rpi")


@post('/rpi')
def service():
    data = json.loads(request.body.getvalue())
    print data
    lights = {}
    for elem in data["lights"]:
        lights[elem['lightId']] = Color(elem['red'],elem['green'],elem['blue'],elem['intensity'])
    #print lights
    last = -1
    propagate = data.get('propagate')
    #print type(propagate), propagate
    for index in xrange(32):
        c = lights.get(index)
        #print "%d\t\t%s\t%d"%(index, str(c), last)
        if c:
            led.set(index, c)
            if propagate:
                last = index
        elif last == -1:
            led.setOff(index)
        elif propagate == True:
            led.set(index, lights[last])
    led.update()

local_ip = check_output(['hostname', '-I']).split()[0].strip()
import requests

url = 'http://cs4720.cs.virginia.edu/ipregistration/?pokemon=Furret&ip=%s'%(local_ip)
r = requests.get(url)
#print r.text

#run(host='10.0.0.60', port=8080, debug=True, reloader=True, server="paste")
#run(host=local_ip, port=80, reloader=True, server="paste")
run(host=local_ip, port=80, debug=True, reloader=True, server="paste")


