import cirq

## define 4 qubits as a linear vector
q = cirq.LineQubit.range(4)

## Define operations
ops = [cirq.X(q[0]),
       cirq.CNOT(q[1],q[0]),
       cirq.H(q[1]),
       cirq.H(q[2]),
       cirq.CNOT(q[1],q[3]),
       cirq.Z(q[1]),       
       cirq.S(q[3])
       ]


## make a circuit
circuit = cirq.Circuit(ops)

## print out circuit
print(circuit)


##0: ───X───X───────────────
##          │
##1: ───────@───H───@───Z───
##                  │
##2: ───H───────────┼───────
##                  │
##3: ───────────────X───S───
