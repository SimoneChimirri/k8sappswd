# Use the official lightweight Python 3.11 image as the base
FROM python:3.11-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt ./

# Install Python dependencies listed in requirements.txt without using cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the current directory into the container
COPY . .

# Expose port 5000 to allow communication to/from the container
EXPOSE 5000

# Set the default command to run the Flask application
CMD [ "python", "app.py" ]