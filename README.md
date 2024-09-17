# bioinformatics-hw-3
Homework 3 for the bioinformatics class.

## Python Version

Using Python 3.12.6

## Running in Google Cloud

To run this project in Google Cloud, follow these steps:

1. Log into the Google Cloud portal and create a basic VM instance using **Compute Engine**. Ensure that the operating system is **Ubuntu** for ease of use.

2. After the VM is created, update the Ubuntu package manager and install the necessary software, including Git and Python 3.12.6. Run the following commands:

```bash
sudo apt-get update
sudo apt-get install python3.12
sudo apt-get install git
```

1. Clone the homework repository from GitHub by running:

```bash
git clone https://github.com/Guuzzeji/bioinformatics-hw-3
```

4. Once the files are cloned, follow the setup steps below.

## Setup

**Set up a virtual environment and install the required packages**

1. Create a Python virtual environment to isolate your project dependencies:

```bash
python3 -m venv venv
```

2. Activate the virtual environment:

```bash
source ./venv/bin/activate
```

3. Install the necessary Python packages from the `requirements.txt` file:

```bash
pip3 install -r requirements.txt
```

> **Tip:** Ensure the `requirements.txt` file is in the project’s root directory. This file should contain all the dependencies needed for the project.

## Running the Script

To run the Python scripts, use one of the following commands:

```bash
python3 homework3.py
```

or

```bash
python3 final_test.py
```

> **Note:** You may want to comment out the bottom part of `homework3.py` if you are using different input files (e.g., `input.txt`) for testing purposes. This allows you to experiment with multiple input scenarios without running all parts of the script at once.
