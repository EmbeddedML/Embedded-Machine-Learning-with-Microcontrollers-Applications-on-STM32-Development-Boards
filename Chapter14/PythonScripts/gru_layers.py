model.summary()

print("\n GRU layer parameters")
layer = model.get_layer(name="gru")
matrices = layer.get_weights()

print("Kernel Weights:", matrices[0].shape)
print("Recurrent Weights:", matrices[1].shape)
print("Biases:", matrices[2].shape)

W = matrices[0]
U = matrices[1]
b = matrices[2]

Wz = W[:, :n_units]
Wr = W[:, n_units: n_units * 2]
Wh = W[:, n_units * 2: n_units * 3]

print("Wz:", Wz)
print("Wr:", Wr)
print("Wh:", Wh)

Uz = U[:, :n_units]
Ur = U[:, n_units: n_units * 2]
Uh = U[:, n_units * 2: n_units * 3]

print("Uz:", Uz)
print("Ur:", Ur)
print("Uh:", Uh)

bz = b[:n_units]
br = b[n_units: n_units * 2]
bh = b[n_units * 2: n_units * 3]

print("bz:", bz)
print("br:", br)
print("bh:", bh)

print("\n Dense layer parameters")
layer = model.get_layer(name="dense")
matrices = layer.get_weights()

print("Wy:", matrices[0])
print("by:", matrices[1])