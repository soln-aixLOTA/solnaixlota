FROM denoland/deno:alpine-1.30.3

WORKDIR /app

# Cache dependencies
COPY deno.json .
RUN deno cache src/main.ts

# Copy source code
COPY . .

CMD ["deno", "run", "--allow-net", "src/main.ts"] 