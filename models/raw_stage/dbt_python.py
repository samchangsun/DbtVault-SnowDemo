import snowflake.snowpark.functions as f
from snowflake.snowpark.functions import col

def model(dbt,session):
            dbt.configure = (materialized = "table")

# Create a DataFrame from the data in the "sample_product_data" table.

        df_table = dbt.ref("raw_inventory")
        df_table2 = dbt.ref("raw_orders")

# To print out the first 10 rows, call df_table.show()

        df_result = df_table2.show()

        return df_result