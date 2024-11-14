import logging
import psutil
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def collect_agi_metrics():
    registry = CollectorRegistry()
    agi_cpu_usage = Gauge('agi_cpu_usage', 'AGI CPU Usage Percentage', registry=registry)
    agi_memory_usage = Gauge('agi_memory_usage', 'AGI Memory Usage Percentage', registry=registry)

    # Assuming AGI processes are identifiable by a specific name or tag
    agi_processes = [p for p in psutil.process_iter(['name']) if 'agi_process' in p.info['name'].lower()]
    total_cpu = sum(p.cpu_percent(interval=1) for p in agi_processes)
    total_memory = sum(p.memory_percent() for p in agi_processes)

    agi_cpu_usage.set(total_cpu)
    agi_memory_usage.set(total_memory)

    logger.info(f"AGI CPU Usage: {total_cpu}%")
    logger.info(f"AGI Memory Usage: {total_memory}%")

    push_to_gateway('prometheus-pushgateway:9091', job='agiops_monitoring', registry=registry)

if __name__ == "__main__":
    collect_agi_metrics() 