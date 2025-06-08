# USE python 3.13 base image
FROM python:3.13-slim-bullseye


# Set environment variables to prevent Python from writing .pyc files and buffering stdout/stderr

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#Set working directory

WORKDIR /app

#Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


#Copy rest of the application
COPY . .

# Expose the application port
EXPOSE 8000

# Command to start FastAPI application

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]