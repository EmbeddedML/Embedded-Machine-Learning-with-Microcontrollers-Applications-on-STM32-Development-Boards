import tensorflow as tf

y_true = tf.constant([[0.4, 0.3], [-0.2, 0.6]])
y_pred = tf.constant([[0.8, 0.6], [0.4,-1.2]])

true_norm = tf.norm(y_true, axis = 1)
pred_norm = tf.norm(y_pred, axis = 1)
norm_prod = true_norm * pred_norm

cos_sim = -tf.reduce_sum(y_true * y_pred, axis = 1) / norm_prod

print(cos_sim.numpy())

cosine_loss = tf.keras.losses.CosineSimilarity(reduction = tf.keras.losses.Reduction.NONE)

result = cosine_loss(y_true, y_pred)
print(result.numpy())