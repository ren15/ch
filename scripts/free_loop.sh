while [ 1 ]
do
    free -h | head -n 2 | tail -n 1
    sleep 0.5
done


