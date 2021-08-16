## THIS IS A MODIFIED EXAMPLE FROM THE CIRQ WEBSITE ##

import cirq
import numpy as np

## define a rotational custom gate

class Rx2(cirq.TwoQubitGate):
    def __init__(self, theta):
        self.theta = theta
    def _unitary_(self):
        cs= np.cos(self.theta/2)
        sn= np.sin(self.theta/2)
        return np.array([
            [1, 0,     0,     0],
            [0, 1,     0,     0],
            [0, 0,    cs, -1j*sn],
            [0, 0, -1j*sn,    cs]
            ])

    def __str__(self):
        return 'Rx2'
    def _circuit_diagram_info_(self, args):
        return '@', 'Rx({}π)'.format(self.theta/np.pi)


## unitary representation
print(np.around(cirq.unitary(Rx2(1./3 * np.pi)), 3))

##[[1.   +0.j  0.   +0.j  0.   +0.j  0.   +0.j ]
## [0.   +0.j  1.   +0.j  0.   +0.j  0.   +0.j ]
## [0.   +0.j  0.   +0.j  0.866+0.j  0.   -0.5j]
## [0.   +0.j  0.   +0.j  0.   -0.5j 0.866+0.j ]]
##


## Get qubits.
a = cirq.NamedQubit('a')
b = cirq.NamedQubit('b')
gate1 = Rx2(1./3 * np.pi)(a,b)
# Display the circuit.
print('Circuit diagram:')
print(cirq.Circuit(gate1))

##Circuit diagram:
##a: ───@─────────────────────────
##      │
##b: ───Rx(0.3333333333333333π)───

