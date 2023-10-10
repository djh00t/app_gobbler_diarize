# Gobbler Audio Diarization Pipeline

This project provides a Python script that automates the process of downloading a WAV audio file from an AWS S3 bucket, running it through WhisperX for diarized transcription, and then uploading the transcript back to the same S3 bucket. It receives the S3 file URL via a Kafka topic and also publishes a message to a Kafka topic when processing is complete.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [How to Run](#how-to-run)
- [Modules](#modules)
- [Dockerization](#dockerization)
- [Makefile Commands](#makefile-commands)

## Requirements

- Python 3.8+
- Conda
- Docker (optional)

## Installation

1. Clone this repository.
2. Navigate to the project directory.
3. Run the following command to set up the Conda environment and install required packages:

    ```bash
    make setup
    ```

## Environment Variables

You'll need to set the following environment variables:

- `AWS_DEFAULT_REGION`: The AWS region of the S3 bucket.
- `AWS_ACCESS_KEY_ID`: AWS credentials for accessing the S3 bucket.
- `AWS_SECRET_ACCESS_KEY`: AWS credentials for accessing the S3 bucket.
- `AWS_S3_BUCKET_NAME`: The name of the S3 bucket.
- `KAFKA_BROKER`: Address of the Kafka broker. ie. `kafka:9092`
- `KAFKA_TOPIC`: Root name of the Kafka topics. ie. `diarize` will use
  `diarize-tasks` for new diarization tasks and `diarize-results` for diarization results.

## How to Run

### Running Locally

To run the project locally, execute the following command:

```bash
make run
```

### Running with Docker

To build and run the Docker container, execute the following commands:

```bash
make docker-build
make docker-run
```

## Modules

- `setup_env.py`: Reads environment variables.
- `s3_interaction.py`: Handles downloading and uploading files to S3 using the gobbler-file-manager library.
- `kafka_interaction.py`: Handles Kafka message consumption and production.
- `whisperx_processing.py`: Placeholder for WhisperX audio processing.
- `main.py`: The main script that ties everything together.

## Dockerization

The project includes a `Dockerfile` and `docker-compose.yml` for easy containerization and deployment.

## Makefile Commands

- `make setup`: Sets up a Python environment and installs required packages.
- `make run`: Runs the main Python script.
- `make docker-build`: Builds the Docker image.
- `make docker-run`: Runs the Docker container.
- `make up`: Starts up the Docker Compose services.
- `make down`: Stops the Docker Compose services.
