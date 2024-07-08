import tensorflow as tf

y_true = tf.constant([[0, 1, 0], [0, 0, 1]])

logits = tf.constant([[-1.99, 0.95, -100], [-1.3,0.78,-1.3]])

y_pred = tf.nn.softmax(logits)

cce_logits = tf.keras.losses.CategoricalCrossentropy(from_logits=True)
cce = tf.keras.losses.CategoricalCrossentropy()

result_logits = cce_logits(y_true, logits)
result= cce(y_true, y_pred)

print(result.numpy())
print(result_logits.numpy())