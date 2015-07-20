This directory contains one OpenMM benchmark for all your devices in your
current workstation.

An openMM installation needs to be present.
To execute the Benchmark run do:
`./run.sh`
This will write all output to stout, it might be clever to do something like this
instead:
`nohup ./run.sh > out 2>&1 &`
Now out will contain all the output from benchmark run. 
