# Scala Service Dockerfile
FROM hseeberger/scala-sbt:11.0.14_1.6.2_2.13.8

WORKDIR /app

# Copy build definition files
COPY build.sbt ./
COPY project/ ./project/

# Update and cache dependencies
RUN sbt update

# Copy the rest of the source code
COPY src/ ./src/

# Compile the project
RUN sbt compile

EXPOSE 8080

CMD ["sbt", "run"]
