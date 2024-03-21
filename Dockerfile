# Use a minimal Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies using Poetry
RUN poetry install --no-interaction

# Expose port (optional, comment out if not needed)
# EXPOSE 8080

# Command to run the application (replace with your actual command)
CMD ["python", "main.py"]
