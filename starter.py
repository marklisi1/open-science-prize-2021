from qiskit import QuantumCircuit, QuantumRegister
import numpy as np


# SPECIFY The `trotter_steps` you want to evaluate on
MY_TROTTER_STEPS = 8
TARGET_TIME = np.pi  # we'll not change this, you can use it for convenience

def my_trotter(trotter_steps):
    num_qubits = 3
    Trot_qr = QuantumRegister(num_qubits)
    Trot_qc = QuantumCircuit(Trot_qr, name="Trot")
    # Start of my trotter implementation



    # End of my trotter implementation
    Trot_gate = Trot_qc.to_instruction()
    return Trot_gate, [1, 3, 5]
