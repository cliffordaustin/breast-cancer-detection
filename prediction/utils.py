import numpy as np
import cv2

from keras.models import load_model
from keras.layers import BatchNormalization


def process_image(image_path):
    try:
        nparr = np.frombuffer(image_path, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (30, 30))

        # reshape the image to a 4D tensor with shape (1, 30, 30, 3)
        image = image.reshape((-1, image.shape[0], image.shape[1], image.shape[2]))

        # convert the image to a float32
        image = np.float32(image) / 255
        return image
    except Exception as e:
        print(e)
        return None


def predict_breast_cancer(image_path, model_path):
    # Load the pre-trained model
    model = load_model(model_path, compile=False)

    # Load and preprocess the image
    image = process_image(image_path)

    # Make predictions
    prediction = model.predict(image)

    predicted_percentage = prediction[0][0]

    # should be in percentage format
    predicted_percentage = np.format_float_positional(predicted_percentage, precision=2)

    return float(predicted_percentage) * 100
