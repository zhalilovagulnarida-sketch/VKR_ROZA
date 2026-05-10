<<<<<<< HEAD
import os
import numpy as np

from PIL import Image

from sklearn.model_selection import train_test_split

from tensorflow.keras.utils import to_categorical

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout
)

DATASET_PATH = "dataset"

IMAGE_SIZE = 224

images = []
labels = []

class_names = sorted([

    folder for folder in os.listdir(DATASET_PATH)

    if os.path.isdir(
        os.path.join(DATASET_PATH, folder)
    )
])

print("Classes found:")
print(class_names)

class_to_index = {

    class_name: index

    for index, class_name
    in enumerate(class_names)
}

for class_name in class_names:

    class_folder = os.path.join(
        DATASET_PATH,
        class_name
    )

    for filename in os.listdir(class_folder):

        if not filename.lower().endswith(
            (".png", ".jpg", ".jpeg")
        ):
            continue

        filepath = os.path.join(
            class_folder,
            filename
        )

        image = Image.open(filepath)

        image = image.convert("RGB")

        image = image.resize(
            (IMAGE_SIZE, IMAGE_SIZE)
        )

        image = np.array(image)

        image = image / 255.0

        images.append(image)

        labels.append(
            class_to_index[class_name]
        )

X = np.array(images)

y = to_categorical(
    labels,
    num_classes=len(class_names)
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = Sequential([

    Conv2D(
        32,
        (3,3),
        activation="relu",
        input_shape=(224,224,3)
    ),

    MaxPooling2D(2,2),

    Conv2D(
        64,
        (3,3),
        activation="relu"
    ),

    MaxPooling2D(2,2),

    Conv2D(
        128,
        (3,3),
        activation="relu"
    ),

    MaxPooling2D(2,2),

    Flatten(),

    Dense(
        256,
        activation="relu"
    ),

    Dropout(0.5),

    Dense(
        128,
        activation="relu"
    ),

    Dropout(0.5),

    Dense(
        len(class_names),
        activation="softmax"
    )
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=8,
    validation_data=(X_test, y_test)
)

model.save(
    "ct_cnn_model.keras"
)

with open("classes.txt", "w") as file:

    for class_name in class_names:

        file.write(
            class_name + "\n"
        )

=======
import os
import numpy as np

from PIL import Image

from sklearn.model_selection import train_test_split

from tensorflow.keras.utils import to_categorical

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout
)

DATASET_PATH = "dataset"

IMAGE_SIZE = 224

images = []
labels = []

class_names = sorted([

    folder for folder in os.listdir(DATASET_PATH)

    if os.path.isdir(
        os.path.join(DATASET_PATH, folder)
    )
])

print("Classes found:")
print(class_names)

class_to_index = {

    class_name: index

    for index, class_name
    in enumerate(class_names)
}

for class_name in class_names:

    class_folder = os.path.join(
        DATASET_PATH,
        class_name
    )

    for filename in os.listdir(class_folder):

        if not filename.lower().endswith(
            (".png", ".jpg", ".jpeg")
        ):
            continue

        filepath = os.path.join(
            class_folder,
            filename
        )

        image = Image.open(filepath)

        image = image.convert("RGB")

        image = image.resize(
            (IMAGE_SIZE, IMAGE_SIZE)
        )

        image = np.array(image)

        image = image / 255.0

        images.append(image)

        labels.append(
            class_to_index[class_name]
        )

X = np.array(images)

y = to_categorical(
    labels,
    num_classes=len(class_names)
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = Sequential([

    Conv2D(
        32,
        (3,3),
        activation="relu",
        input_shape=(224,224,3)
    ),

    MaxPooling2D(2,2),

    Conv2D(
        64,
        (3,3),
        activation="relu"
    ),

    MaxPooling2D(2,2),

    Conv2D(
        128,
        (3,3),
        activation="relu"
    ),

    MaxPooling2D(2,2),

    Flatten(),

    Dense(
        256,
        activation="relu"
    ),

    Dropout(0.5),

    Dense(
        128,
        activation="relu"
    ),

    Dropout(0.5),

    Dense(
        len(class_names),
        activation="softmax"
    )
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=8,
    validation_data=(X_test, y_test)
)

model.save(
    "ct_cnn_model.keras"
)

with open("classes.txt", "w") as file:

    for class_name in class_names:

        file.write(
            class_name + "\n"
        )

>>>>>>> c1394cf (Initial commit)
print("Training completed")