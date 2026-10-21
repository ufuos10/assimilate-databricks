#!/usr/bin/env python

from dotenv import load_dotenv

load_dotenv()

from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.getOrCreate()
spark.range(5).show()
