import cirq

##
def rotate(qubits):
    for i in range(len(qubits) - 1):
        a, b = qubits[i: i + 2]
        yield cirq.CNOT(b,a)

line1 = cirq.LineQubit.range(5)

circuit1 = cirq.Circuit(rotate(line1))

print(circuit1)

##0: ───X───────────────
##      │
##1: ───@───X───────────
##          │
##2: ───────@───X───────
##              │
##3: ───────────@───X───
##                  │
##4: ───────────────@───
