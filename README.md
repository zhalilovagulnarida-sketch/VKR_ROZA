Lung Cancer Detection AI
Project Description
This project is a deep learning web application for lung cancer image classification using CT/X-ray images.

The application allows users to upload an image and receive a prediction of the detected lung cancer type.

The model was trained using images stored in the dataset folder. The system currently recognizes only the classes included in the training dataset, but it can be expanded by adding new images and retraining the model.


Features
Upload CT or X-ray image
Detect lung cancer type
Display prediction confidence
Show probability for each class
Web interface using Streamlit
Expandable dataset and model


Technologies Used
Python
TensorFlow / Keras
Streamlit
NumPy
Pillow
Scikit-learn


Project Structure
lung-cancer-app/

│

├── app.py

├── model.py

├── train_model.py

├── requirements.txt

├── classes.txt

├── ct_cnn_model.keras

│

└── dataset/


Installation
Install required libraries:

pip install -r requirements.txt


Train the Model
Run:

python train_model.py

After training, the following files will be created automatically:

ct_cnn_model.keras
classes.txt


Run the Application
Start the web application:

streamlit run app.py


Dataset
The dataset contains different categories of lung cancer images.

Each folder inside the dataset directory represents one class.

Example:

dataset/

    adenocarcinoma/

    squamous_cell/

    large_cell/

    normal/


Future Improvements
Add more medical image classes
Improve model accuracy
Use larger datasets
Implement advanced CNN architectures
Add medical image preprocessing

