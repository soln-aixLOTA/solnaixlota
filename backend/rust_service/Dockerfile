FROM rust:1.70

WORKDIR /app

# Copy source code
COPY . .

# Build the Rust application
RUN cargo build --release

CMD ["./target/release/rust_service"] 