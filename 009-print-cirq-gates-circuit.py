
import cirq
import numpy as np

##
# Get some qubits.
q = cirq.LineQubit.range(4)

# sample gates defined in Cirq.
def Gate_Circuit(g,q):
    if g=='X':
        print(f"{g}\n",cirq.Circuit(cirq.X(q[0])))                     # Pauli-X.
    elif g=='Y':       
        print(f"{g}\n",cirq.Circuit(cirq.Y(q[1])) )                    # Pauli-Y.
    elif g=='Z':    
        print(f"{g}\n",cirq.Circuit(cirq.Z(q[2])) )                   # Pauli-Z.
    elif g=='CZ':       
        print(f"{g}\n",cirq.Circuit(cirq.CZ(q[0],q[1])) )                # Controlled-Z gate.
    elif g=='CNOT':
        print(f"{g}\n",cirq.Circuit(cirq.CNOT(q[1],q[2]) ))              # Controlled-X gate.
    elif g=='H':
        print(f"{g}\n",cirq.Circuit(cirq.H(q[0]) ))                    # Hadamard gate.
    elif g=='T':
        print(f"{g}\n",cirq.Circuit(cirq.T(q[1]) ))                    # T gate.
    elif g=='S':
        print(f"{g}\n",cirq.Circuit(cirq.S(q[2]) ))                    # S gate.
    elif g=='CCZ':
        print(f"{g}\n",cirq.Circuit(cirq.CCZ(q[0], q[1], q[2])))           # Controlled CZ gate.
    elif g=='SWAP':
        print(f"{g}\n",cirq.Circuit(cirq.SWAP(q[0], q[1])))              # Swap gate.
    elif g=='CSWAP':
        print(f"{g}\n",cirq.Circuit(cirq.CSWAP(q[0], q[1], q[2])))         # Controlled swap gate.
    elif g=='CCX':
        print(f"{g}\n",cirq.Circuit(cirq.CCX(q[0], q[1], q[2])) )          # Toffoli (CCNOT) gate.
    elif g=='ISWAP':
        print(f"{g}\n",cirq.Circuit(cirq.ISWAP(q[0], q[1])))             # ISWAP gate.
    elif g=='Rx':
        print(f"{g}\n",cirq.Circuit(cirq.Rx(rads=0.5 * np.pi)(q[0])))  # Rotation about X.
    elif g=='Ry':
        print(f"{g}\n",cirq.Circuit(cirq.Ry(rads=0.5 * np.pi)(q[1])))  # Rotation about Y.
    elif g=='Rz':
        print(f"{g}\n",cirq.Circuit(cirq.Rz(rads=0.5 * np.pi)(q[2])))  # Rotation about Z.
    elif g=='X**0.5':
        print(f"{g}\n",cirq.Circuit(cirq.X(q[0]) ** 0.5))              # Sqrt of NOT gate.
    elif g=='CX':
        print(f"{g}\n",cirq.Circuit([cirq.CX(q[0],q[1])]))
    elif g=='CCNOT':
        print(f"{g}\n",cirq.Circuit([cirq.CCNOT(q[0],q[1],q[2])]))
    else:
        print(f"error: not recognized gate: {g}")
        STOP

## list of gates
gates= ['H', 'S', 'T', 'X', 'Y', 'Z',
        'CX', 'CCX', 'Rx', 'Ry', 'Rz',
        'CNOT', 'CCNOT','SWAP','ISWAP','CSWAP',

        ]
##
for gate in gates:
    Gate_Circuit(gate,q)

##
##H
## 0: ───H───
##S
## 2: ───S───
##T
## 1: ───T───
##X
## 0: ───X───
##Y
## 1: ───Y───
##Z
## 2: ───Z───
##CX
## 0: ───@───
##      │
##1: ───X───
##CCX
## 0: ───@───
##      │
##1: ───@───
##      │
##2: ───X───
##Rx
## 0: ───Rx(0.5π)───
##Ry
## 1: ───Ry(0.5π)───
##Rz
## 2: ───Rz(0.5π)───
##CNOT
## 1: ───@───
##      │
##2: ───X───
##CCNOT
## 0: ───@───
##      │
##1: ───@───
##      │
##2: ───X───
##SWAP
## 0: ───×───
##      │
##1: ───×───
##ISWAP
## 0: ───iSwap───
##      │
##1: ───iSwap───
##CSWAP
## 0: ───@───
##      │
##1: ───×───
##      │
##2: ───×───    
