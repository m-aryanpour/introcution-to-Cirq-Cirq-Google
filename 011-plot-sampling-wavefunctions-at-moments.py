## THIS IS A MODIFIED EXAMPLE FROM THE CIRQ WEBSITE ##

##

import cirq
import numpy as np
import matplotlib.pylab as plt
##
"""Plot the probability of measuring a qubit in the ground state."""
# Get a qubit.
a = cirq.NamedQubit('a')

# Get a circuit of a bunch of X rotations.
num_angles = 200

# Number of times to sample.
repetitions = 100
simulator = cirq.Simulator()
##
for rot in ['Rx','Ry','Rz']:
    if rot=='Rx':
        circuit = cirq.Circuit([cirq.Rx(rads=np.pi / 50.0)(a) for theta in range(num_angles)])
        mark = 'xr'
    if rot=='Ry':
        circuit = cirq.Circuit([cirq.Ry(rads=np.pi / 50.0)(a) for theta in range(num_angles)])
        mark = 'oy'
    if rot=='Rz':
        circuit = cirq.Circuit([cirq.Rz(rads=np.pi / 50.0)(a) for theta in range(num_angles)])
        mark= 'bs'

    # List to store the probability of the ground state.
    sampled_probs = []

    for i, step in enumerate(simulator.simulate_moment_steps(circuit)):
        samples = step.sample([a], repetitions=repetitions)
        prob = np.sum(samples, axis=0)[0] / repetitions
        sampled_probs.append(prob)


    # Plot the probability of the ground state at each simulation step.
    plt.style.use('seaborn-whitegrid')
    plt.plot(sampled_probs, mark)
##    
plt.xlabel("Step")
plt.ylabel("Probability of ground state");
plt.legend(['Rx','Ry','Rz'])
plt.show()

