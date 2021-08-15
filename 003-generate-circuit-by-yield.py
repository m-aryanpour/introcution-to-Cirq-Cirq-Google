import cirq
##
a= cirq.NamedQubit('a')
b= cirq.NamedQubit('b')
##
def swap2(a, b):
    """Swaps two qubits with three CNOTs."""
    yield cirq.CNOT(a, b) # |a> |b> --> |a> |a ^ b>
    yield cirq.H(a)       # 
    yield cirq.CNOT(b, a) # |a> |a ^ b> --> |a ^ a ^ b> | a ^ b> = |b>|a^b>
    yield cirq.Z(b)       #     
    yield cirq.CNOT(a, b) # |b> |a ^ b> --> |b>|a ^ b ^ b> = |b> |a>
##
circuit1= cirq.Circuit(swap2(a, b))
print(circuit1)

##a: ───@───H───X───────@───
##      │       │       │
##b: ───X───────@───Z───X───

##
circuit2= cirq.Circuit(swap2(b, a))
print(circuit2)

##a: ───X───────@───Z───X───
##      │       │       │
##b: ───@───H───X───────@───
