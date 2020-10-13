import paho.mqtt.client as mqtt
import ssl
import time

def on_connect(client, userdata, flags, rc):
    global x
    global qos
    
    if(qos == 0):
        client.sent = True
        client.loop_stop()
    

repetitions = [39,399,3999,39999,399999,3999999]
#39 volte per 1kb, .14
#399 volte per 10kb, 0.14
#3999 volte per 100kb, 0.14
#39999 volte per 1MB, 0.14
#399999 volte per 10MB, 0.14
#3999999 volte per 100MB, 0.14
string = 'AAAAAAAAAAAAAAAAAAAAAAAA\n'

def on_publish(client,userdata,mid):
    global x
    global qos

    print('on_publish('+str(x)+'-'+str(qos)+'): ' + str("%.20f" % time.time()))
    client.disconnect()

def repeat(id, qos, mess):
    client = mqtt.Client(client_id=id,clean_session=True, protocol=mqtt.MQTTv311, transport="tcp")

    client.on_connect = on_connect
    client.on_publish = on_publish

    client.tls_set(ca_certs="ca.pem", certfile="cert.crt", keyfile="key.key", cert_reqs=ssl.CERT_REQUIRED,tls_version=ssl.PROTOCOL_TLS)
    client.tls_insecure_set(True)

    client.username_pw_set(username="user", password=None)

    client.connect("IP address", 8883, 60)

    if(qos == 0):
        client.sent = False
        client.loop_start()
        while client.sent == False:
            time.sleep(.1)
            
    client.publish("test", payload=(str("%.14f" % time.time())+mess), qos=qos, retain=False)

    client.loop_forever()

for i in range(6):
    mess = ""
    for i in range(repetitions[i]):
        mess += string
    for x in range(1, 101):
        for qos in range (3):
            repeat('Client' + str(x), qos, mess)
            time.sleep(.1)
        if (i == 5):
            time.sleep(10)
