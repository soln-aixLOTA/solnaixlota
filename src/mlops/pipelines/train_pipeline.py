import logging
import mlflow
from sklearn.model_selection import train_test_split
from src.mlops.models import load_data, train_model

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_training():
    logger.info("Starting training pipeline...")
    
    # Load data
    data = load_data('data/dataset.csv')
    X_train, X_test, y_train, y_test = train_test_split(data.features, data.labels, test_size=0.2, random_state=42)
    
    # Train model
    model = train_model(X_train, y_train)
    
    # Evaluate model
    accuracy = model.score(X_test, y_test)
    logger.info(f"Model accuracy: {accuracy}")
    
    # Log model with MLflow
    with mlflow.start_run():
        mlflow.sklearn.log_model(model, "model")
        mlflow.log_metric("accuracy", accuracy)
    
    logger.info("Training pipeline completed successfully.")

if __name__ == "__main__":
    run_training() 