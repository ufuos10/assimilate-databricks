from dotenv import load_dotenv
from databricks.sdk import WorkspaceClient

load_dotenv()  # loads DATABRICKS_HOST and DATABRICKS_TOKEN from .env

w = WorkspaceClient()  # reads those variables automatically

print("Cluster name, cluster ID")

for cluster in w.clusters.list():
    print(f"{cluster.cluster_name}, {cluster.cluster_id}")
