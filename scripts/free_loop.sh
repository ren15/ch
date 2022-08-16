while [ 1 ]
do
    date
    free -h | head -n 2 | tail -n 1
    sleep 0.2
done


