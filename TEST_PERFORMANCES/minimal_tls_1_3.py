import paho.mqtt.client as mqtt
import ssl
import time

def on_connect(client, userdata, flags, rc):
    global x
    global qos
    print('on_connect('+str(x)+'-'+str(qos)+'): ' + str("%.20f" % time.time()))
    
    if(qos == 0):
        client.sent = True
        client.loop_stop()
    

def on_publish(client,userdata,mid):
    global x
    global qos

    print('on_publish('+str(x)+'-'+str(qos)+'): ' + str("%.20f" % time.time()))
    print('\n')
    client.disconnect()

def repeat(id, qos):
    client = mqtt.Client(client_id=id,clean_session=True, protocol=mqtt.MQTTv311, transport="tcp")

    client.on_connect = on_connect
    client.on_publish = on_publish

    client.tls_set(ca_certs="ca.pem", certfile="cert.crt", keyfile="key.key", cert_reqs=ssl.CERT_REQUIRED,tls_version=ssl.PROTOCOL_TLSv1_3)
    client.tls_insecure_set(True)

    client.username_pw_set(username="user", password=None)

    print('prima connect('+str(x)+'-'+str(qos)+'):' + str("%.20f" % time.time()))
    client.connect("IP Address", 8883, 60)
    print('dopo connect('+str(x)+'-'+str(qos)+'): ' + str("%.20f" % time.time()))

    if(qos == 0):
        client.sent = False
        client.loop_start()
        while client.sent == False:
            time.sleep(.1)
            
    client.publish("test", payload=("("+str(x)+'-'+str(qos)+"): "+str("%.20f" % time.time())), qos=qos, retain=False)

    client.loop_forever()

print('TLS 1.3 :\n')
for x in range(1, 101):
    for qos in range (3):
        repeat('Client' + str(x), qos)


        
