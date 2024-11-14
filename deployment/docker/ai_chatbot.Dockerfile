FROM python:3.12-slim AS builder

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add non-root user
RUN useradd -m appuser

# Copy application code
COPY . .

# Set ownership
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Run the application with Gunicorn
CMD ["gunicorn", "-w", "4", "-k", "gevent", "--bind", "0.0.0.0:8000", "ai_chatbot.chatbot:app"] 