# Use an official Python image as a base
FROM python:3.10  

# Set the working directory
WORKDIR /app  

# Install Poetry
RUN pip install poetry  

# Copy only necessary files first (for efficient caching)
COPY pyproject.toml poetry.lock ./

# Install dependencies (without creating a virtual environment)
RUN poetry config virtualenvs.create false && poetry install --no-root  

# Copy the rest of the application code
COPY . .  

# Run your command
CMD ["poetry", "run", "python", "-m", "ultravox.training.train", "--config_path", "ultravox/training/configs/lalbok_config.yaml"]