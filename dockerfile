# Use the official Python image.
FROM python:3.9

# Set the working directory in the container.
WORKDIR /app

# Copy the dependencies file to the working directory.
COPY poetry.lock pyproject.toml ./

# Install Poetry.
RUN pip install poetry

# Install the dependencies.
RUN poetry install

# Copy the rest of the application code to the working directory.
COPY . .

# Run the FastAPI application.
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]