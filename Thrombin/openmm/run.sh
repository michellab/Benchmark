#!/bin/bash
module load openmm/6.2

echo 'OpenMM simple Benchmark'
NDEV=`nvidia-smi -L |wc -l`
for d in `seq 0 $((NDEV-1))`
do
for p in CUDA OpenCL
do
START=$(date +%s.%N)
python run_openmm.py --deviceid $d --platform $p
END=$(date +%s.%N)
printf "Time taken for single GPU calculation on device ${d} with platfrom ${p}.\n"
echo $END - $START | bc -l
echo '==================================================================='
rm *.dcd
done
done
