# run processes and store pids in array
for i in {1..8}; do
	sage solve.sage $1 $i &
    pids[${i}]=$!
done

# wait for all pids
for pid in ${pids[*]}; do
    wait $pid
done

