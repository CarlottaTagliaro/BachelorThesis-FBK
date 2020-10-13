while :
do
    echo 'network down'
    ifconfig eth0 down
    sleep 10
    echo 'network up'
    ifconfig eth0 up
    sleep 10
done
