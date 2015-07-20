#!/bin/bash
module load openmm/6.2
module load sire/master

echo 'OpenMM Benchmark for stresstest'

START=$(date +%s.%N)
somd -C ../config.cfg --device 0 --platform CUDA
END=$(date +%s.%N)
printf "Time taken for single GPU calculation on device ${d} with platfrom ${p}.\n"
echo $END - $START | bc -l
echo '==================================================================='
