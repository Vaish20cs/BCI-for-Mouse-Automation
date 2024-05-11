from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv('dataset.csv')

# Features and labels
features = df[['x', 'y', 'z', 'electrode1', 'electrode2']]
labels = df['class']  # Assuming 'class' is the column with 'left', 'right', 'back', 'front'

# Split the dataset into a training set and a test set
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Create a Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf.fit(features_train, labels_train)

# Make predictions
labels_pred = rf.predict(features_test)

# Compute confusion matrix
cm = confusion_matrix(labels_test, labels_pred)

# Display confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=rf.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.show()

import matplotlib.pyplot as plt

def plot_training_progress(train_losses, val_losses=None, train_acc=None, val_acc=None):
    """
    Plot the training and validation losses and accuracies over epochs.

    Args:
    train_losses (list): List of training losses for each epoch.
    val_losses (list): List of validation losses for each epoch. Default is None.
    train_acc (list): List of training accuracies for each epoch. Default is None.
    val_acc (list): List of validation accuracies for each epoch. Default is None.
    """
    epochs = range(1, len(train_losses) + 1)

    plt.figure(figsize=(12, 6))

    # Plot losses
    plt.subplot(1, 2, 1)
    plt.plot(epochs, train_losses, 'bo-', label='Training Loss')
    if val_losses:
        plt.plot(epochs, val_losses, 'ro-', label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)

    # Plot accuracies
    if train_acc or val_acc:
        plt.subplot(1, 2, 2)
        if train_acc:
            plt.plot(epochs, train_acc, 'bo-', label='Training Accuracy')
        if val_acc:
            plt.plot(epochs, val_acc, 'ro-', label='Validation Accuracy')
        plt.title('Training and Validation Accuracy')
        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.grid(True)

    plt.tight_layout()
    plt.show()

# Example usage:
# Replace train_losses, val_losses, train_acc, and val_acc with your actual values
train_losses = [0.5, 0.4, 0.3, 0.25, 0.2]
val_losses = [0.45, 0.35, 0.28, 0.22, 0.18]
train_acc = [0.8, 0.85, 0.88, 0.9, 0.92]
val_acc = [0.75, 0.8, 0.82, 0.85, 0.88]

plot_training_progress(train_losses, val_losses, train_acc, val_acc)
