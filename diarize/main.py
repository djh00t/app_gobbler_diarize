import setup_env
import s3_interaction
import kafka_interaction
import whisperx_processing
import logging

def main():
    logging.basicConfig(level=logging.INFO)

    # Get AWS default region from environment variables
    aws_default_region = setup_env.get_env_variable("AWS_DEFAULT_REGION")
    # Ensure that the AWS default region is set
    if aws_default_region is None:
        raise ValueError("AWS_DEFAULT_REGION environment variable is not set.")
    # Get AWS Access Key ID from environment variables
    aws_access_key_id = setup_env.get_env_variable("AWS_ACCESS_KEY_ID")
    # Ensure that the AWS Access Key ID is set
    if aws_access_key_id is None:
        raise ValueError("AWS_ACCESS_KEY_ID environment variable is not set.")
    # Get AWS Secret Access Key from environment variables
    aws_secret_access_key = setup_env.get_env_variable("AWS_SECRET_ACCESS_KEY")
    # Ensure that the AWS Secret Access Key is set
    if aws_secret_access_key is None:
        raise ValueError("AWS_SECRET_ACCESS_KEY environment variable is not set.")
    # Get AWS S3 bucket name from environment variables
    aws_s3_bucket_name = setup_env.get_env_variable("AWS_S3_BUCKET_NAME")
    # Ensure that the AWS S3 bucket name is set
    if aws_s3_bucket_name is None:
        raise ValueError("AWS_S3_BUCKET_NAME environment variable is not set.")
    # Get Kafka broker from environment variables
    kafka_broker = setup_env.get_env_variable("KAFKA_BROKER")
    # Ensure that the Kafka broker is set
    if kafka_broker is None:
        raise ValueError("KAFKA_BROKER environment variable is not set.")
    # Get Kafka topic from environment variables
    kafka_topic = setup_env.get_env_variable("KAFKA_TOPIC")
    # Ensure that the Kafka topic is set
    if kafka_topic is None:
        raise ValueError("KAFKA_TOPIC environment variable is not set.")
    # Get WhisperX DB from environment variables
    whisperx_db = setup_env.get_env_variable("WHISPERX_DB")
    # Ensure that the WhisperX DB is set
    if whisperx_db is None:
        raise ValueError("WHISPERX_DB environment variable is not set.")

    # Initialize WhisperX
    whisperx_processing.initialize_whisperx(whisperx_db)

    # Setup Kafka consumer and producer
    consumer = kafka_interaction.setup_kafka_consumer(kafka_broker, kafka_topic+'tasks')
    producer = kafka_interaction.setup_kafka_producer(kafka_broker, kafka_topic+'results')

    # Consume messages from Kafka topic
    for message in kafka_interaction.consume_messages(consumer):
        wav_file_key = message.decode("utf-8")
        
        local_path = f"/tmp/{wav_file_key}"
        s3_interaction.download_wav_from_s3(aws_s3_bucket_name, wav_file_key, local_path)
        
        transcript = whisperx_processing.process_audio(local_path)
        
        transcript_key = wav_file_key.replace(".wav", ".txt")
        s3_interaction.upload_transcript_to_s3(aws_s3_bucket_name, transcript_key, transcript)
        
        kafka_interaction.publish_message(producer, kafka_topic, "Processing complete")
        
        logging.info(f"Processing complete for {wav_file_key}")

if __name__ == "__main__":
    main()
