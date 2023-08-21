# Use the official Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the frontend application code to the container
COPY . .

# Install any required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the app will run
EXPOSE 5000

# Start the frontend Flask app
CMD ["python", "app.py"]
