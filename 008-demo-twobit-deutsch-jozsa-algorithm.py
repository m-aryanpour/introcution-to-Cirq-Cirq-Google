## THIS IS A COPIED EXAMPLE FROM THE CIRQ WEBSITE ##

import cirq

##
"""Operations to query all possible functions on two bits.
Two of these functions are constant, and six of these functions are balanced.
"""
# Define three qubits to use.
q0, q1, q2 = cirq.LineQubit.range(3)

# Define the operations to query each of the two constant functions.
constant = (
    [], 
    [cirq.X(q2)]
)

# Define the operations to query each of the six balanced functions.
balanced = (
    [cirq.CNOT(q0, q2)], 
    [cirq.CNOT(q1, q2)], 
    [cirq.CNOT(q0, q2), cirq.CNOT(q1, q2)],
    [cirq.CNOT(q0, q2), cirq.X(q2)], 
    [cirq.CNOT(q1, q2), cirq.X(q2)], 
    [cirq.CNOT(q0, q2), cirq.CNOT(q1, q2), cirq.X(q2)]
)

##
def dj_circuit(oracle):
    # Phase kickback trick.
    yield cirq.X(q2), cirq.H(q2)

    # Get an equal superposition over input bits.
    yield cirq.H(q0), cirq.H(q1)

    # Query the function.
    yield oracle

    # Use interference to get result, put last qubit into |1>.
    yield cirq.H(q0), cirq.H(q1), cirq.H(q2)

    # Use a final OR gate to put result in final qubit.
    yield cirq.X(q0), cirq.X(q1), cirq.CCX(q0, q1, q2)
    yield cirq.measure(q2)


##

"""Simulate the Deutsch-Jozsa circuit and check the results."""
simulator = cirq.Simulator()

print("Result on constant functions:")
for oracle in constant:
    result = simulator.run(cirq.Circuit(dj_circuit(oracle)), repetitions=10)
    print(result)

print("\nResult on balanced functions:")
for oracle in balanced:
    result = simulator.run(cirq.Circuit(dj_circuit(oracle)), repetitions=10)
    print(result)

##
##Result on constant functions:
##2=0000000000
##2=0000000000
##
##Result on balanced functions:
##2=1111111111
##2=1111111111
##2=1111111111
##2=1111111111
##2=1111111111
##2=1111111111
