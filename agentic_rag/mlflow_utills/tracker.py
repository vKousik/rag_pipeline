import mlflow
import time

mlflow.set_experiment("Agentic-RAG")

def track_run(query, model, system_prompt, func):
    with mlflow.start_run():
        print("🔥 MLflow RUN STARTED")   # 👈 ADD THIS

        start = time.time()
        result = func()
        latency = time.time() - start

        mlflow.log_param("query", query)
        mlflow.log_param("model", model)
        mlflow.log_param("system_prompt", system_prompt)

        mlflow.log_metric("latency", latency)

        mlflow.log_text(str(result), "output.txt")

        print("✅ MLflow LOGGED")   # 👈 ADD THIS


        return result, latency