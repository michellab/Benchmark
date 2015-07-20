__author__ = 'ppxasjsm'
from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from sys import stdout
import time
from argparse import ArgumentParser
if '__main__' == __name__:

    #Let us allow the script to externally set the variables deviceid and platform
    parser = ArgumentParser()
    parser.add_argument(
            '--deviceid',
            type=int,
            default=0
        )
    parser.add_argument(
            "--platform",
            default='CUDA'
        )
    args = parser.parse_args()
    print 'Running on platfrom %s using deviceid %d' %(args.platform, args.deviceid)
    #Setting platfrom and device
    platform = openmm.Platform.getPlatformByName(args.platform) # platform to use
    platform_name = platform.getName()
    if platform_name == 'CUDA':
        platform.setPropertyDefaultValue('CudaDeviceIndex', '%d' % args.deviceid) # select Cuda device index
    if platform_name == 'OpenCL':
        platform.setPropertyDefaultValue('OpenCLDeviceIndex', '%d' % args.deviceid)
    #load the modulcule and setup the system
    prmtop = AmberPrmtopFile('solvated.parm7')
    inpcrd = AmberInpcrdFile('solvated.rst7')
    system = prmtop.createSystem(nonbondedMethod=CutoffPeriodic, nonbondedCutoff=1*nanometer, constraints=HBonds)

    #define barostat and add it to the system
    barostat = MonteCarloBarostat(1.0*bar, 300.0*kelvin, 25)
    system.addForce(barostat)
    integrator = LangevinIntegrator(300*kelvin, 1/picosecond, 0.002*picoseconds)
    simulation = Simulation(prmtop.topology, system, integrator, platform)
    simulation.context.setPositions(inpcrd.positions)
    if inpcrd.boxVectors is not None:
        simulation.context.setPeriodicBoxVectors(*inpcrd.boxVectors)
    #minimize just in case
    simulation.minimizeEnergy()

    #Let's run the actual simulation and time it.
    start_time = time.time()
    simulation.reporters.append(DCDReporter('traj.dcd', 1000))
    simulation.reporters.append(StateDataReporter(stdout, 5000, step=True, potentialEnergy=True, temperature=True))
    simulation.step(50000)
    state = simulation.context.getState(getPositions=True)
    f = open('final.pdb', 'w')
    PDBFile.writeFile(prmtop.topology,state.getPositions(), file=f)
    f.close()
    print("--- %s seconds ---" % (time.time() - start_time))
