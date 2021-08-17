## THIS IS A COPIED EXAMPLE FROM THE CIRQ WEBSITE ##

import cirq
import numpy as np
##
"""Example of a custom gate which supports the decompose protocol."""
class HXGate(cirq.SingleQubitGate):

    def _decompose_(self, qubits):
        return cirq.H(*qubits), cirq.X(*qubits)

    def __str__(self):
        return 'HX'

##
"""Use the gate in a circuit."""
HX = HXGate()

a = cirq.NamedQubit('a')
circuit = cirq.Circuit(HX(a))
print(circuit)

##a: ───HX───

##
"""Decompose the gate."""
print(cirq.Circuit(cirq.decompose(circuit)))

##a: ───Y^0.5───X───X───

##
"""Decompose the gate once."""
print(cirq.Circuit(cirq.decompose_once(HX(a))))

##a: ───H───X───

##
"""Define a custom decomposer."""
def my_decompose(op):
    if isinstance(op, cirq.GateOperation) and isinstance(op.gate, HXGate):
        return cirq.Z(*op.qubits), cirq.H(*op.qubits)

# Decompose the circuit according to this custom decomposer.
cirq.Circuit(cirq.decompose(HX(a), intercepting_decomposer=my_decompose))

##a: ───Z───Y^0.5───X───

##
"""Define a predicate of which gates to keep without decomposing."""
def keep_h_and_x(op):
    return isinstance(op, cirq.GateOperation) and op.gate in [cirq.H, cirq.X]


# Decompose the HXGate using a custom predicate for which gates to not decompose.
print(cirq.decompose(HX(a), keep=keep_h_and_x))

##[cirq.H(cirq.NamedQubit('a')), cirq.X(cirq.NamedQubit('a'))]
