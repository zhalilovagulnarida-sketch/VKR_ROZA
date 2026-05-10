<<<<<<< HEAD
import numpy as np

from tensorflow.keras.models import load_model

model = load_model(
    "ct_cnn_model.keras"
)

with open("classes.txt", "r") as file:

    classes = [
        line.strip()
        for line in file.readlines()
    ]

_, img_height, img_width, _ = model.input_shape


def preprocess_image(image):

    image = image.convert("RGB")

    image = image.resize(
        (img_width, img_height)
    )

    image = np.array(
        image,
        dtype=np.float32
    )

    image = image / 255.0

    image = np.expand_dims(
        image,
        axis=0
    )

    return image


def predict(image):

    processed_image = preprocess_image(image)

    prediction = model.predict(
        processed_image,
        verbose=0
    )

    class_index = np.argmax(prediction)

    diagnosis = classes[class_index]

    confidence = float(
        np.max(prediction) * 100
    )

    probabilities = {
        classes[i]: float(prediction[0][i] * 100)
        for i in range(len(classes))
    }

=======
import numpy as np

from tensorflow.keras.models import load_model

model = load_model(
    "ct_cnn_model.keras"
)

with open("classes.txt", "r") as file:

    classes = [
        line.strip()
        for line in file.readlines()
    ]

_, img_height, img_width, _ = model.input_shape


def preprocess_image(image):

    image = image.convert("RGB")

    image = image.resize(
        (img_width, img_height)
    )

    image = np.array(
        image,
        dtype=np.float32
    )

    image = image / 255.0

    image = np.expand_dims(
        image,
        axis=0
    )

    return image


def predict(image):

    processed_image = preprocess_image(image)

    prediction = model.predict(
        processed_image,
        verbose=0
    )

    class_index = np.argmax(prediction)

    diagnosis = classes[class_index]

    confidence = float(
        np.max(prediction) * 100
    )

    probabilities = {
        classes[i]: float(prediction[0][i] * 100)
        for i in range(len(classes))
    }

>>>>>>> c1394cf (Initial commit)
    return diagnosis, confidence, probabilities