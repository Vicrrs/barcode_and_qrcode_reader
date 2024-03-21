# Use a minimal Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Copy the dependency files and install them
COPY pyproject.toml poetry.lock* ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Expose port (optional, comment out if not found)
# EXPOSE 8080

# Command to run the application (replace with your actual command)
CMD ["python", "main.py"]
