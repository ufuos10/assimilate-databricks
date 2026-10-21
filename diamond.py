from dotenv import load_dotenv
from databricks.connect import DatabricksSession

load_dotenv()
spark = DatabricksSession.builder.getOrCreate()

df = spark.read.csv(
    "/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv",
    header=True,
    inferSchema=True,
)
df.write.mode("overwrite").saveAsTable("default.diamonds")