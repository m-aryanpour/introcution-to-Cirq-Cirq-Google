import cirq

a = cirq.LineQubit.range(5)

strategies= ['EARLIEST', 'NEW',
             'INLINE',
             'NEW_THEN_INLINE'
             ]
circuit1 = cirq.Circuit()

circuit1.append([cirq.S(a[0]),
                 cirq.T(a[0]),
                 cirq.X(a[0]),
                 cirq.Y(a[0]),
                 cirq.Z(a[0]),
                 ])
for i, st in enumerate(strategies):
    strategy1 = 'cirq.InsertStrategy.'+st
    eval('circuit1.append([cirq.H(a[i+1])], strategy= '+strategy1+')')


print(circuit1)

##0: ───S───T───X───Y───Z───────────
##
##1: ───H───────────────────────────
##
##2: ───────────────────────H───────
##
##3: ───────────────────────H───────
##
##4: ───────────────────────────H───
