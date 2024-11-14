import logging
import psutil
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def collect_metrics():
    registry = CollectorRegistry()
    cpu_usage = Gauge('cpu_usage', 'CPU Usage Percentage', registry=registry)
    memory_usage = Gauge('memory_usage', 'Memory Usage Percentage', registry=registry)

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    cpu_usage.set(cpu)
    memory_usage.set(memory)

    logger.info(f"CPU Usage: {cpu}%")
    logger.info(f"Memory Usage: {memory}%")

    push_to_gateway('prometheus-pushgateway:9091', job='aiops_monitoring', registry=registry)

if __name__ == "__main__":
    collect_metrics() 