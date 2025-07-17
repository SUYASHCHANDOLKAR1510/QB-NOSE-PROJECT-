# 🧠 Quantum Bioelectronic Nose (Q-BE Nose)

A smart gas classification system using Arduino, gas sensors, and TinyML.  
Inspired by how the human olfactory system works — this project detects and classifies gases in real-time using embedded AI on ESP32.

---

## 🚀 Features

- 👃 Bio-inspired gas sensing using MQ3, MQ135 & Graphene-based sensors
- 🧠 Trained ML model using Python + Keras
- 📟 Embedded Arduino firmware for real-time inference
- ⚡ ESP32-based implementation (TinyML-ready)
- 🧪 Dataset of 150 sensor readings (Clean Air, Alcohol, Ammonia)
- 📊 Circuit diagrams, project report & presentation included

---

## 🔧 Tech Stack

- Arduino IDE (ESP32 board)
- Python 3.8+
- TensorFlow / Keras
- Scikit-learn, pandas
- TFLite (optional)

---

## 📁 Project Structure

📦 QBE-Nose
├── qbe_model_training.py # Python script to train the ML model
├── qbe_model.h5 / qbe_model.tflite # Trained model (Keras / TFLite)
├── qbe_gas_sensor_dataset.csv # Sample dataset
├── qbe_arduino_code.ino # Firmware for ESP32
├── circuit_diagram.png # Engineering-style circuit
├── QBE_Presentation.pptx # Project PPT
└── Project_Report_QBE_Nose.pdf # Final report


---

## 📸 Demo

---

## 🧠 Dataset Classes

| Label | Gas Type    |
|-------|-------------|
| 0     | Clean Air   |
| 1     | Alcohol     |
| 2     | Ammonia     |

---

## 📌 Future Scope

- Add Bluetooth/Wi-Fi gas alerts
- Expand dataset with real-world readings
- Add OLED display / mobile app
- Explore VOCs, CO2 & toxic gas classifications

---

## 📬 Contact

Made with ❤️ by [Suyash Chandolkar]  
📧 [suyashchandolkar15@gmail.com]  
🌐 [LinkedIn/GitHub]

---

> “Turning sensors into senses.” 🧠🔬

