# Base image
FROM python:3.8.10

# Set working directory
WORKDIR /app

# Copy the application code
COPY PNGM_microservice.py /app/PNGM_microservice.py

# Install dependencies
RUN pip install flask psutil

# Expose the port
EXPOSE 5000

# Start the application
CMD ["python", "PNGM_microservice.py"]
