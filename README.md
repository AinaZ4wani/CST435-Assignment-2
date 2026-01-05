# CST435-Assignment-2
This repository contains a Python-based parallel image processing system. The project implements an image processing pipeline using two parallel programming paradigms: multiprocessing and concurrent.futures. Performance is evaluated through execution time, speedup, and efficiency analysis using a subset of the Food-101 dataset.

# Initialization

## Part 1: GCP Setup

### A. Instance Configuration
1. Navigate to the **Compute Engine** section in the Google Cloud Console.
2. Select Create Instance.
3. Machine Family: Select General purpose, Series E2.
4. Machine Type: Select e2-standard-8 (8 vCPUs, 32 GB memory).
5. Boot Disk: Select Debian GNU/Linux 12 (bookworm) with 10 GB storage.
6. Firewall: Default settings are sufficient.

### B. Deployment
1. Click Create to provision the resource.
2. Once the Status indicator turns green, click SSH to establish a secure shell connection.

## Part 2: Environment and Python Dependency Installation

### A. Environment Setup
Execute the following commands to update the package manager and activate a virtual a virtual environment:

```python
$ sudo apt update
$ sudo apt install -y python3-venv python3-pip
$ python3 -m venv venv
$ source venv/bin/activate
```
You should see:

```python
(venv) username@instance-name:~$
```

### B. Dependency Installation
Execute the following commands to install the necessary Python libraries:

```python
$ pip install numpy pillow psutil
```

Dependencies verification (optional)

```python
$ python -c "import numpy, PIL, psutil; print('OK')"
```

## Part 3: Clone GitHub Repository

1. Click Code → HTTPS.
2. Copy the URL.
3. In the VM, execute the following commands to clone the repo and navigate into the correct directory:

```python
$ sudo apt install -y git
$ git clone https://github.com/AinaZ4wani/CST435-Assignment-2.git
$ cd CST435-Assignment-2
```

# Run concurrent.futures Paradigm:

Execute the following command to run the concurrent.futures module on the VM:

```python
$ python run_concurrent.py
```
