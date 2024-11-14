# Stage 1: Build
FROM denoland/deno:2.0.0-alpine as builder

WORKDIR /app

# Cache dependencies
COPY deno.json .
RUN deno cache src/main.ts

# Copy source code
COPY . .

# Stage 2: Production
FROM denoland/deno:2.0.0-alpine

WORKDIR /app

# Copy from builder
COPY --from=builder /app .

# Use non-root user for security
USER deno

CMD ["deno", "run", "--allow-net", "src/main.ts"]

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1 