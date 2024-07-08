print("\n RNN layer parameters")
layer = model.get_layer(name="simple_rnn")
matrices = layer.get_weights()

print("Wh:", matrices[0])
print("Uh:", matrices[1])
print("bh:", matrices[2])

print("\n Dense layer parameters")
layer = model.get_layer(name="dense")
matrices = layer.get_weights()

print("Wy:", matrices[0])
print("by:", matrices[1])
