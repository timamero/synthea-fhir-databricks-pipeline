# Read data from Databricks SQL using the Databricks SQL Connector for Python
# References:
# - https://docs.databricks.com/aws/en/dev-tools/python-sql-connector
# - https://docs.databricks.com/aws/en/dev-tools/auth/pat#pat-user

from databricks import sql
import os


def get_condition_counts():
    query = """
  SELECT p.gender, c.condition_description, COUNT(*) AS condition_count
  FROM learning.synthea.conditions c
  JOIN learning.synthea.patients p ON c.patient_id = p.patient_id
  GROUP BY p.gender, c.condition_description
  ORDER BY condition_count DESC LIMIT 5;
  """
    try:
        with sql.connect(
            server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
            http_path=os.getenv("DATABRICKS_HTTP_PATH"),
            access_token=os.getenv("DATABRICKS_TOKEN"),
        ) as connection:

            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()

                for row in result:
                    print(row)
    except Exception as e:
        print(f"Error executing query: {e}")
