# Use a small Python base image
FROM python:3.11-slim

# Avoid prompts from apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /app

# Copy and install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose the port Amplify expects (8080)
EXPOSE 8080

# Run Streamlit, binding to 0.0.0.0 on port 8080
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8080", "--server.address=0.0.0.0", "--server.headless=true"]
