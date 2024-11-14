export class MonitoringService {
  private metrics = new Map<string, number>();
  private startTime = Date.now();

  recordMetric(name: string, value: number) {
    this.metrics.set(name, (this.metrics.get(name) || 0) + value);
  }

  getMetrics() {
    return {
      uptime: Date.now() - this.startTime,
      metrics: Object.fromEntries(this.metrics),
    };
  }

  async exportMetrics() {
    // Export metrics to monitoring system
    const metrics = this.getMetrics();
    await fetch(Deno.env.get("METRICS_ENDPOINT") || "", {
      method: "POST",
      body: JSON.stringify(metrics),
    });
  }
} 