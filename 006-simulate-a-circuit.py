import cirq

a= cirq.NamedQubit('a')
b= cirq.NamedQubit('b')
##
"""Get a circuit to simulate."""
def basic_circuit(measure=True):
    """Returns a simple circuit with some one- and two-qubit gates,
    as well as (optionally) measurements.
    """
    # Gates we will use in the circuit.
    sqrt_x = cirq.X**0.5
    cz = cirq.CZ

    # Yield the operations.
    yield cirq.H(a), sqrt_x(b)
    yield cz(a, b)
    yield sqrt_x(a), cirq.S(b)
    if measure:
        yield cirq.measure(a,b)

# Create a circuit including measurements.
circuit = cirq.Circuit(basic_circuit())
print(circuit)
##a: ───H───────@───X^0.5───M───
##              │           │
##b: ───X^0.5───@───S───────M───


#
##
# ===================================================
# Get a simulator.
simulator = cirq.Simulator()

# Pass the circuit to the simulator.run method.
result = simulator.run(circuit, repetitions=1)
print("Measurement results:")
print(result)
##
##Measurement results:
##a,b=1, 0


##
# ===================================================
import numpy as np
"""Simulating a circuit with the `simulate` method."""
# Get a circuit without measurements.
circuit = cirq.Circuit(basic_circuit(measure=False))

# Simulate the circuit.
result = simulator.simulate(circuit, qubit_order=[a, b])

# Print the final state vector (wavefunction).
print("State vector:")
print(np.around(result.final_state_vector, 3))

# Print the state vector in Dirac notation.
print("\nDirac notation:")
print(result.dirac_notation())

##State vector:
##[ 0.354+0.354j -0.354+0.354j  0.354+0.354j  0.354-0.354j]
##
##Dirac notation:
##(0.35+0.35j)|00⟩ + (-0.35+0.35j)|01⟩ + (0.35+0.35j)|10⟩ + (0.35-0.35j)|11⟩
