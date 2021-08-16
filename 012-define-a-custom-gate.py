## THIS IS A MODIFIED EXAMPLE FROM THE CIRQ WEBSITE ##

import cirq
import numpy as np
import matplotlib.pylab as plt

## define a custom gate in Cirq
class MyGate1(cirq.SingleQubitGate):

    def _unitary_(self):
        return np.array([[3 / 5, 4 / 5], [-4 / 5, 3 / 5]])

    def __str__(self):
        return 'λ'

## use custom gate
a     = cirq.NamedQubit('a')
gate1 = MyGate1()
circuit1 = cirq.Circuit(gate1(a))
print(circuit1)

## simulate the circuit
simulator = cirq.Simulator()
result1   = simulator.simulate(circuit1)
print(result1)

##
##a: ───λ───
##measurements: (no measurements)
##output vector: 0.6|0⟩ - 0.8|1⟩
