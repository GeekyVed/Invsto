# Step 1: Use a Python base image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the dependencies file (requirements.txt) to the container
COPY requirements.txt .

# Step 4: Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your FastAPI app into the container
COPY . .

# Step 6: Expose the FastAPI app's port (default is 8000)
EXPOSE 8000

# Step 7: Command to run FastAPI with Uvicorn (the ASGI server)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
