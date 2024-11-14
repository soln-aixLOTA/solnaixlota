# Stage 1: Build
FROM denoland/deno:alpine-1.31.1 as builder

WORKDIR /app

# Cache dependencies
COPY deno.json .
COPY src/types/tensorflow.d.ts ./src/types/tensorflow.d.ts
RUN deno cache src/main.ts

# Copy source code
COPY . .

# Stage 2: Production
FROM denoland/deno:alpine-1.31.1

WORKDIR /app

# Copy from builder
COPY --from=builder /app .

# Use non-root user for security
USER deno

CMD ["deno", "run", "--allow-net", "--allow-read", "--allow-env", "src/main.ts"]

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1 