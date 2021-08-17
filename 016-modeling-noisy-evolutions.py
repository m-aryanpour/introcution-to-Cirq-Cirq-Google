## THIS IS A COPIED EXAMPLE FROM THE CIRQ WEBSITE ##

import cirq
import numpy as np
import sympy as sp

##

# Get qubits to use in the circuit.
a = cirq.NamedQubit("a")
b = cirq.NamedQubit("b")

"""Create a circuit with a depolarizing channel."""
circuit = cirq.Circuit(cirq.depolarize(0.2)(a), cirq.measure(a))
print(circuit)

##a: ───D(0.2)───M───

##
for i, kraus in enumerate(cirq.kraus(cirq.depolarize(0.2))):
    print(f"Kraus operator {i} is:", kraus, sep="\n", end="\n\n")

##Kraus operator 0 is:
##[[0.89442719 0.        ]
## [0.         0.89442719]]
##
##Kraus operator 1 is:
##[[0.        +0.j 0.25819889+0.j]
## [0.25819889+0.j 0.        +0.j]]
##
##Kraus operator 2 is:
##[[0.+0.j         0.-0.25819889j]
## [0.+0.25819889j 0.+0.j        ]]
##
##Kraus operator 3 is:
##[[ 0.25819889+0.j  0.        +0.j]
## [ 0.        +0.j -0.25819889+0.j]]

##
    """ representing Kraus operators in a Pauli basis"""
for i, kraus in enumerate(cirq.kraus(cirq.depolarize(0.2))):
    pauli_ex = cirq.expand_matrix_in_orthogonal_basis(kraus, cirq.PAULI_BASIS)
    print(f"Kraus operator {i} is:", pauli_ex, sep="\n", end="\n\n")

##Kraus operator 0 is:
##0.894*I
##
##Kraus operator 1 is:
##0.258*X
##
##Kraus operator 2 is:
##0.258*Y
##
##Kraus operator 3 is:
##0.258*Z

##
"""Example of simulating a noisy circuit with the density matrix simulator."""
# Circuit to simulate.
circuit = cirq.Circuit(cirq.depolarize(0.2)(a))
print('Circuit:\n{}\n'.format(circuit))

# Get the density matrix simulator.
simulator = cirq.DensityMatrixSimulator()

# Simulate the circuit and get the final density matrix.
matrix = simulator.simulate(circuit).final_density_matrix
print('Final density matrix:\n{}'.format(matrix))

##Circuit:
##a: ───D(0.2)───
##
##Final density matrix:
##[[0.8666666 +0.j 0.        +0.j]
## [0.        +0.j 0.13333333+0.j]]


##
"""Simulating a circuit with measurements using the DensityMatrixSimulator."""
# Get a circuit with measurements.
circuit = cirq.Circuit(cirq.depolarize(0.5)(a), cirq.measure(a))

# Simulate with the density matrix multiple times.
dmat1 = simulator.simulate(circuit).final_density_matrix
dmat2 = simulator.simulate(circuit).final_density_matrix

print(np.allclose(dmat1, dmat2))

##True


