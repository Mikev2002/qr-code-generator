# QR Code Generator (Dockerized)

This project is a Python-based QR Code Generator that allows users to create QR codes for any given URL. The application is containerized using Docker and includes a GitHub Actions workflow for CI/CD automation.

---

## Features

- Accepts URL input via command-line argument
- Generates QR codes and saves them as `.png` files
- Uses a minimal and secure Docker image
- Automatically builds and pushes Docker image to DockerHub using GitHub Actions

---

##  How to Run the App

###  Prerequisites
- Docker installed
- Python installed (for local testing)

###  Run locally:
```bash
python main.py --url https://www.njit.edu

````
###  Run with Docker:

docker run --rm mikev424/qr-code-generator-app --url https://www.njit.edu

Save the QR Code to Your Machine:

docker run --rm -v ${PWD}/qr_codes:/app/qr_codes mikev424/qr-code-generator-app --url https://www.njit.edu

DockerHub:

You can find the published image on DockerHub:
 mikev424/qr-code-generator-app

Author

Name: Mike V

GitHub: Mikev2002

