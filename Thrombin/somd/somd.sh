#!/bin/bash
module load openmm/6.2
module load sire/master

echo 'somd simple Benchmark'
NDEV=`nvidia-smi -L |wc -l`

for d in `seq 0 $((NDEV-1))`
do
  for p in CUDA OpenCL
  do
    mkdir output_$d_$P
    cd output_$d_$p
    START=$(date +%s.%N)
    somd -C ../config.cfg --device $d --platform $p
    END=$(date +%s.%N)
    printf "Time taken for single GPU calculation on device ${d} with platfrom ${p}.\n"
    echo $END - $START | bc -l
    echo '==================================================================='
    cd ../
  done
done
