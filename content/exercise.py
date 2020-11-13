from qiskit import *
from math import pi
from qiskit.visualization import plot_bloch_multivector

QuantumCircuit

from qiskit.visualization import plot_histogram

backend = Aer.get_backend('statevector_simulator') # Tell Qiskit how to simulate our circuit
out_state = execute(qc, backend, shots=1000).result().get_counts() # Do the simulation, returning the state vector
print(out_state)
plot_histogram(out_state)


from qiskit_textbook.tools import array_to_latex


