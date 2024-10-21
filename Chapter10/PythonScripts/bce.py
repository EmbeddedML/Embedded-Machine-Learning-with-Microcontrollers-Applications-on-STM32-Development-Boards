import tensorflow as tf

y_pred_logits = tf.constant([0.41, -0.85, -1.39, 1.39])

y_pred = tf.keras.activations.sigmoid(y_pred_logits)

y_true = [0, 1, 0, 0]

bce = tf.keras.losses.BinaryCrossentropy()
bce_logits = tf.keras.losses.BinaryCrossentropy(from_logits=True)

result_logits = bce_logits(y_true, y_pred_logits)
result= bce(y_true, y_pred)

print(result.numpy())
print(result_logits.numpy())