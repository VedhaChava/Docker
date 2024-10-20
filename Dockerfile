# Use a lightweight base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /home/data

# Copy the script and the text files into the container
COPY scripts.py ./scripts.py
COPY IF.txt ./IF.txt
COPY AlwaysRememberUsThisWay.txt ./AlwaysRememberUsThisWay.txt

# Create the output directory
RUN mkdir -p output

# Run the Python script when the container starts
CMD ["python", "./scripts.py"]
