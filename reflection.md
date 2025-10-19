
# Reflection on Dockerizing the QR Code Generator Application

This project taught me how to containerize a Python application using Docker. I began by creating a QR Code Generator script in Python, then packaged it using a Dockerfile that included best practices like using a non-root user and a minimal base image. I built the Docker image, ran it in a container, and successfully generated QR code images.

One of the challenges I faced was understanding how to access files created inside a Docker container. After some research, I learned how to use volume mounts to map container folders to my local file system, which allowed me to retrieve the generated QR code images easily. I also learned how to tag and push Docker images to DockerHub and how to share my project using GitHub.

Overall, this assignment helped me understand the full workflow of building, running, and deploying containerized applications. I now feel more confident working with Docker and applying these skills to future projects.
