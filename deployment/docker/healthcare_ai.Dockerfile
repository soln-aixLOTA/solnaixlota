FROM python:3.12-slim

WORKDIR /app

# Install Python dependencies
COPY src/healthcare_ai/drug_discovery/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/healthcare_ai/ .

# Expose port
EXPOSE 8005

# Create non-root user
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser

CMD ["python", "drug_discovery/drug_discovery_ai.py"] 