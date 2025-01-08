import mlflow
import random
import config

mlflow.set_tracking_uri(config.tracking_uri)

with mlflow.start_run():
    mlflow.log_param("param1", random.randint(1,100))
    mlflow.log_param("param2", random.random())
    
    # log some random metrics
    mlflow.log_metric("metric1", random.random())
    mlflow.log_metric("metric1", random.uniform(0.5, 1.5))
    print("log the random parameters and metrics")