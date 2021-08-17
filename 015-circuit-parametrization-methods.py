## THIS IS A COPIED EXAMPLE FROM THE CIRQ WEBSITE ##

import cirq
import numpy as np
import sympy as sp

##

# Get qubits to use in the circuit.
a = cirq.NamedQubit("a")
b = cirq.NamedQubit("b")

# Define a parameterized value.
s = sp.Symbol("s")

# Create a circuit.
circuit = cirq.Circuit(cirq.X.on(a) ** s, cirq.X.on(b) ** s)

# Display it.
print("Circuit with parameterized gates:\n")
print(circuit)

##Circuit with parameterized gates:
##
##a: ───X^s───
##
##b: ───X^s───

##
"""Simulate the circuit at multiple parameter values."""
simulator = cirq.Simulator()

# Simulate the circuit for several values of the parameter.
num_params = 5
for y in range(num_params):
    result = simulator.simulate(circuit, param_resolver={"s": y / 4.0})
    print("s={}: {}\n".format(y, np.around(result.final_state_vector, 2)))

##s=0: [1.+0.j 0.+0.j 0.+0.j 0.+0.j]
##
##s=1: [ 0.6 +0.6j   0.25-0.25j  0.25-0.25j -0.1 -0.1j ]
##
##s=2: [0. +0.5j 0.5+0.j  0.5+0.j  0. -0.5j]
##
##s=3: [-0.1 +0.1j   0.25+0.25j  0.25+0.25j  0.6 -0.6j ]
##
##s=4: [0.+0.j 0.+0.j 0.+0.j 1.+0.j]

##

"""Simulate the circuit at multiple parameter values."""
# Get a list of param resolvers.
num_params = 5
resolvers = [cirq.ParamResolver({'s': y / 8.0}) for y in range(num_params)]

# Add measurements to the circuit.
circuit.append([cirq.measure(a), cirq.measure(b)])

# Simulate the circuit using run_sweep.
results = simulator.run_sweep(
    program=circuit,
    params=resolvers,
    repetitions=10
)

for i, result in enumerate(results):
    print('params: {}\n{}\n'.format(result.params.param_dict, result))

##params: OrderedDict([('s', 0.0)])
##a=0000000000
##b=0000000000
##
##params: OrderedDict([('s', 0.125)])
##a=0001100000
##b=0000001000
##
##params: OrderedDict([('s', 0.25)])
##a=0000000001
##b=0001000101
##
##params: OrderedDict([('s', 0.375)])
##a=0011000111
##b=1010000100
##
##params: OrderedDict([('s', 0.5)])
##a=0010111101
##b=0011000011

##
results = simulator.sample(
    program=circuit,
    params=resolvers,
    repetitions=10
)

results.describe()

##               s          a          b
##count  50.000000  50.000000  50.000000
##mean    0.250000   0.240000   0.220000
##std     0.178571   0.431419   0.418452
##min     0.000000   0.000000   0.000000
##25%     0.125000   0.000000   0.000000
##50%     0.250000   0.000000   0.000000
##75%     0.375000   0.000000   0.000000
##max     0.500000   1.000000   1.000000

##
"""Alternative method of getting a sequence of param resolvers."""
linspace = cirq.Linspace(start=0, stop=1.0, length=11, key='x')
for p in linspace:
    print(p)
    
##cirq.ParamResolver({'x': 0.0})
##cirq.ParamResolver({'x': 0.1})
##cirq.ParamResolver({'x': 0.2})
##cirq.ParamResolver({'x': 0.3})
##cirq.ParamResolver({'x': 0.4})
##cirq.ParamResolver({'x': 0.5})
##cirq.ParamResolver({'x': 0.6})
##cirq.ParamResolver({'x': 0.7})
##cirq.ParamResolver({'x': 0.8})
##cirq.ParamResolver({'x': 0.9})
##cirq.ParamResolver({'x': 1.0})
