# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy app files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Streamlit configuration
RUN mkdir -p ~/.streamlit
RUN echo "[server]\nheadless = true\nport = 8080\nenableCORS = false\n" > ~/.streamlit/config.toml

# Expose port 8080 (Amplify expects this)
EXPOSE 8080

# Run Streamlit
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8080", "--server.address=0.0.0.0"]
