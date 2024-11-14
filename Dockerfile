FROM eclipse-temurin:17-jdk-focal

WORKDIR /app

# Copy dependencies
COPY target/scala-2.12/lib/ /app/lib/
COPY target/scala-2.12/ai-service.jar /app/

# Set classpath and main class
ENV CLASSPATH="/app/lib/*:/app/ai-service.jar"
ENTRYPOINT ["java", "-cp", "${CLASSPATH}", "com.example.ScalaService"] 