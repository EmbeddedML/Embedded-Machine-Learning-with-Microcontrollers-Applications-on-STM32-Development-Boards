test_ind=10

im = test_images[test_ind]

# Add the image to a batch where it's the only member.
img = np.expand_dims(im, 0)

# First way of predicting the label

predictions = model.predict(img)

print("Predictions")
print(predictions)

predicted_label = np.argmax(predictions)
actual_label = np.argmax(test_labels[test_ind])

plt.figure()
plt.imshow(im, cmap=plt.cm.binary)
plt.title('actual label= ' + str(actual_label) + ', predicted label = '+ str(predicted_label))

plt.show()
