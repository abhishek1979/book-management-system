# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /book-management-system

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port
EXPOSE 9999

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9999"]