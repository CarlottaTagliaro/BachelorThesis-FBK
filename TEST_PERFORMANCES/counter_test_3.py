import paho.mqtt.client as mqtt
import time, sys, ssl
import paho.mqtt.publish as publish

counter = 0
index = 0
dic = {}
dict = {'ca_certs':"ca.pem", 'certfile':"cert.crt", 'keyfile':"key.key", 'tls_version':ssl.PROTOCOL_TLS, 'ciphers':'ECDHE-RSA-AES256-GCM-SHA384'}
firstTime = True

while(index<=51):
    try:
        publish.single('test', payload=(str("%.20f" % time.time())), qos=1, retain=False, hostname="192.168.1.1",port=8883, client_id="id", 
                      keepalive=2, will=None, auth=None, tls=dict,protocol=mqtt.MQTTv311, transport="tcp")
        if (firstTime):
            counter = 0
            time.sleep(.05)
            index += 1
            firstTime = False   
      
        counter += 1

    except KeyboardInterrupt:
        print(dic)
        sys.exit()
    except:
        time.sleep(.1)
        dic[index] = counter
        firstTime = True         
        #continue
print(dic)

