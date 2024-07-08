model.summary()

print("\n LSTM layer parameters")
layer = model.get_layer(name="lstm")
matrices = layer.get_weights()

print("Kernel Weights:", matrices[0].shape)
print("Recurrent Weights:", matrices[1].shape)
print("Biases:", matrices[2].shape)

W = matrices[0]
U = matrices[1]
b = matrices[2]

Wi = W[:, :n_units]
Wf = W[:, n_units: n_units * 2]
Wc = W[:, n_units * 2: n_units * 3]
Wo = W[:, n_units * 3:]

print("Wi:", Wi)
print("Wf:", Wf)
print("Wc:", Wc)
print("Wo:", Wo)

Ui = U[:, :n_units]
Uf = U[:, n_units: n_units * 2]
Uc = U[:, n_units * 2: n_units * 3]
Uo = U[:, n_units * 3:]

print("Ui:", Ui)
print("Uf:", Uf)
print("Uc:", Uc)
print("Uo:", Uo)

bi = b[:n_units]
bf = b[n_units: n_units * 2]
bc = b[n_units * 2: n_units * 3]
bo = b[n_units * 3:]

print("bi:", bi)
print("bf:", bf)
print("bc:", bc)
print("bo:", bo)

print("\n Dense layer parameters")
layer = model.get_layer(name="dense")
matrices = layer.get_weights()

print("Wy:", matrices[0])
print("by:", matrices[1])