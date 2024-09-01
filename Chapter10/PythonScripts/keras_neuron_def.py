import tensorflow as tf

w0 = tf.keras.initializers.Constant(1.)
b0 = tf.keras.initializers.Constant(1.)
l0=tf.keras.layers.Dense(units=1, 
                         input_shape=[1], 
                         kernel_initializer=w0, 
                         bias_initializer=b0, 
                         activation='sigmoid')
model = tf.keras.models.Sequential([l0])

result=model.predict([0.0])

print(result)
