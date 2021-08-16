## THIS IS A COPIED EXAMPLE FROM THE CIRQ WEBSITE ##
import cirq

##
"""Store the operations to query each function in a dictionary."""
# Get qubits for the operations to act on.
q0, q1 = cirq.LineQubit.range(2)

# Define the dictionary of operations. The key of each dictionary entry
# is the subscript of the function f in the above explanatory text.
oracles = {
    '0': [],
    '1': [cirq.X(q1)],
    'x': [cirq.CNOT(q0, q1)],
    'notx': [cirq.CNOT(q0, q1), cirq.X(q1)]
}

##

"""Creating the circuit used in Deutsch's algorithm."""
def deutsch_algorithm(oracle):
    """Returns the circuit for Deutsch's algorithm given an input
    oracle, i.e., a sequence of operations to query a particular function.
    """
    yield cirq.X(q1)
    yield cirq.H(q0), cirq.H(q1)
    yield oracle
    yield cirq.H(q0)
    yield cirq.measure(q0)

for key, oracle in oracles.items():
    print(f"Circuit for f_{key}:")
    print(cirq.Circuit(deutsch_algorithm(oracle)), end="\n\n")


##
    """Simulate each of the circuits."""
simulator = cirq.Simulator()
for key, oracle in oracles.items():
    result = simulator.run(cirq.Circuit(deutsch_algorithm(oracle)), 
                          repetitions=10)
    print('oracle: f_{:<4} results: {}'.format(key, result))

##oracle: f_0    results: 0=0000000000
##oracle: f_1    results: 0=0000000000
##oracle: f_x    results: 0=1111111111
##oracle: f_notx results: 0=1111111111
