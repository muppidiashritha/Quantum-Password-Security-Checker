from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a simple 2-qubit circuit
qc = QuantumCircuit(2, 2)

# Put both qubits into superposition
qc.h([0, 1])

# Example: pretend the correct password is "11"
qc.cz(0, 1)

# Apply Grover-like amplification
qc.h([0, 1])
qc.x([0, 1])
qc.h(1)
qc.cx(0, 1)
qc.h(1)
qc.x([0, 1])
qc.h([0, 1])

# Measure
qc.measure([0, 1], [0, 1])

# Run simulation
simulator = AerSimulator()
result = simulator.run(qc, shots=1000).result()
counts = result.get_counts()

print("Quantum Password Search Result:")
print(counts)