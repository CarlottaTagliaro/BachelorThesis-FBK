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
    client.disconnect()

def repeat(id, qos, cyph):
    client = mqtt.Client(client_id=id,clean_session=True, protocol=mqtt.MQTTv311, transport="tcp")

    client.on_connect = on_connect
    client.on_publish = on_publish

    client.tls_set(ca_certs="ca.pem", certfile="cert.crt", keyfile="key.key", cert_reqs=ssl.CERT_REQUIRED,tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=cyph)
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

print('ECDHE-RSA-CHACHA20-POLY1305 :\n')
for x in range(1, 101):
    for qos in range (3):
        repeat('Client' + str(x), qos, 'ECDHE-RSA-CHACHA20-POLY1305 ')

print('ECDHE-RSA-AES128-GCM-SHA256:\n')
for x in range(1, 101):
    for qos in range (3):
        repeat('Client' + str(x), qos, 'ECDHE-RSA-AES128-GCM-SHA256')
        
print('ECDHE-RSA-AES256-SHA384:\n')
for x in range(1, 101):
    for qos in range (3):
        repeat('Client' + str(x), qos, 'ECDHE-RSA-AES256-SHA384')
        
print('ECDHE-RSA-AES128-SHA256:\n')
for x in range(1, 101):
    for qos in range (3):
        repeat('Client' + str(x), qos, 'ECDHE-RSA-AES128-SHA256')
        
print('ECDHE-RSA-AES256-SHA:\n')
for x in range(1, 101):
    for qos in range (3):
        repeat('Client' + str(x), qos, 'ECDHE-RSA-AES256-SHA')
        
print('ECDHE-RSA-AES128-SHA:\n')
for x in range(1, 101):
    for qos in range (3):
        repeat('Client' + str(x), qos, 'ECDHE-RSA-AES128-SHA')

print('AES256-GCM-SHA384:\n')
for x in range(1, 101):
    for qos in range (3):
        repeat('Client' + str(x), qos, 'AES256-GCM-SHA384')
        
print('AES128-GCM-SHA256:\n')
for x in range(1, 101):
    for qos in range (3):
        repeat('Client' + str(x), qos, 'AES128-GCM-SHA256')
        
print('AES256-SHA256:\n')
for x in range(1, 101):
    for qos in range (3):
        repeat('Client' + str(x), qos, 'AES256-SHA256')
        
print('AES128-SHA256:\n')
for x in range(1, 101):
    for qos in range (3):
        repeat('Client' + str(x), qos, 'AES128-SHA256')

print('AES256-SHA:\n')
for x in range(1, 101):
    for qos in range (3):
        repeat('Client' + str(x), qos, 'AES256-SHA')

print('AES128-SHA:\n')
for x in range(1, 101):
    for qos in range (3):
        repeat('Client' + str(x), qos, 'AES128-SHA')


        
