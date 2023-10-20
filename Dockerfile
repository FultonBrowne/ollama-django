# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=your_project.settings
ENV DJANGO_SECRET_KEY=your_secret_key
ENV DJANGO_DEBUG=False
ENV DJANGO_ALLOWED_HOSTS=*
ENV DJANGO_DB_HOST=db
ENV DJANGO_DB_PORT=5432
ENV LLMS_BASE_URL='http://ollama:11434'

# Set environment variables for Daphne
ENV DAPHNE_WORKERS=4

# Set environment variables for other configurations
# ENV DJANGO_STATIC_URL=/static/
# ENV DJANGO_MEDIA_URL=/media/

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 for the ASGI server
EXPOSE 8000

# Run Daphne ASGI server
CMD ["daphne", "-u", "unix:/tmp/daphne.sock", "-p", "8000", "django_streaming.asgi:application"]
