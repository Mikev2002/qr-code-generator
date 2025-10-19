# Use the official Python slim image
FROM python:3.12-slim-bullseye

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Create output directories and add a non-root user
RUN useradd -m myuser && \
    mkdir logs qr_codes && \
    chown myuser:myuser logs qr_codes

# Copy the app code into the container and give ownership
COPY --chown=myuser:myuser . .

# Switch to the non-root user
USER myuser

# Default command to run the app
ENTRYPOINT ["python", "main.py"]
CMD ["--url", "https://github.com/Mikev2002"]
