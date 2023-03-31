import snowflake.snowpark.functions as f
from snowflake.snowpark.functions import col

def model(dbt, session):
        
    orders = dbt.ref("raw_orders")

    df_result = orders.describle()

    return df_result