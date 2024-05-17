# Brute-Force-Attack-Detection-Using-Machine-Learning

This repository contains a unsupervised machine learning algorithm designed to detect brute force attacks. The project aims to leverage the power of unsupervised machine learning model to analyze network traffic patterns and identify potential brute force attacks in real-time.

## Overview

The primary goal of this project is to develop a robust and efficient system capable of identifying brute force attacks on network systems. By utilizing unsupervised machine learning algorithm techniques, we aim to enhance the accuracy and speed of attack detection, thereby improving overall network security.

When an abnormality is detected, the model sends an alert, allowing the administrator to take appropriate action. The administrator can block the attacker's IP address, making it a reliable option for real-world brute-force attack detection.

## Key Files

### Python Files

- `keys.py`: Contains the twilio keys used for alert messaging mechanism.
- `main.py`: The main script that runs the unsupervised machine learning model for detecting brute force attacks.

### CSV Files

- `train.csv`: Contains training data for the unsupervised machine learning model.
- `test.csv`: Contains test data to evaluate the performance of the trained model.
  
## Installation

To get started with the project, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/sakshay2318/Brute-Force-Attack-Detection-Using-Machine-Learning.git
```
2. Navigate to the project directory:
```bash
cd Brute-Force-Attack-Detection-Using-Machine-Learning
```
3. Install required Python packages:
```bash
pip install -r requirements.txt
```

## Usage

After setting up the environment, you can run the main script to start detecting brute force attacks. Use the following command:
```bash
python main.py
```

This script will initiate the deep learning model and begin monitoring network traffic for signs of brute force attacks.

## Contributing

Contributions to this project are welcome If you find a bug, have a feature request, or would like to contribute to the development of the model, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
