#!/bin/bash

for i in {0..2}
do
mkdir out$i
cd out$i
nohup ../run.sh 2>&1 >out &
cd ../
done