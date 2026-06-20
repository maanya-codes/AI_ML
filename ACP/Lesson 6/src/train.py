import tensorflow as tf
from tensorflow.keras import layers, models

# ==========================================
# 1. Load the Dataset (Updated with your paths)
# ==========================================
print("Loading training data...")
# Notice the 'r' before the quote to handle Windows backslashes
train_data = tf.keras.utils.image_dataset_from_directory(
    r'C:\Users\ORAYMAANYA\Downloads\archive\train', 
    image_size=(48, 48),
    batch_size=64,
    color_mode='grayscale'
)

print("Loading validation data...")
val_data = tf.keras.utils.image_dataset_from_directory(
    r'C:\Users\ORAYMAANYA\Downloads\archive\test',  
    image_size=(48, 48),
    batch_size=64,
    color_mode='grayscale'
)

# ==========================================
# 2. Build the Neural Network (CNN)
# ==========================================
model = models.Sequential([
    layers.Rescaling(1./255, input_shape=(48, 48, 1)),
    
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Flatten(),
    
    layers.Dense(64, activation='relu'),
    layers.Dense(7, activation='softmax') 
])

# ==========================================
# 3. Compile the Model
# ==========================================
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

# ==========================================
# 4. Train the Model
# ==========================================
print("Starting the training process...")
history = model.fit(train_data, validation_data=val_data, epochs=15)

# ==========================================
# 5. Save the Model
# ==========================================
model.save('emotion_model.h5')
print("Success! Model saved as 'emotion_model.h5'.")