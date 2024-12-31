import mlflow
import random

mlflow.set_tracking_uri("http://ec2-13-49-70-110.eu-north-1.compute.amazonaws.com:5000/")

with mlflow.start_run():
    mlflow.log_param("param1", random.randint(1,100))
    mlflow.log_param("param2", random.random())
    
    # log some random metrics
    mlflow.log_metric("metric1", random.random())
    mlflow.log_metric("metric1", random.uniform(0.5, 1.5))
    print("log the random parameters and metrics")