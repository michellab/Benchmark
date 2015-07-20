This directory contains two Benchmarks to be run with Sire.

1. *somd.sh* will run somd simulations using all dvices available on the computer
as well as the two platforms CUDA and OpenCL. The script will assume that both
OpenCL and CUDA are supported.
To execute simly run:
./somd.sh

2.*run.sh* will execute stresstest.sh, which will run n somd simulations at the
same time. In order to specify how many somd jobs should be started in parallel
simply execute the script in the following way:
./run.sh 8
This would start 8 jobs shortly after each other.
