from db import connect_with_connector
import logging



conn = connect_with_connector()
logger = logging.getLogger

# what is df?
def load_df_into_database(df, table_name="patients"):
    try:
        result = df.to_sql(table_name, conn, if_exists="append", index=False)
        print(result)
        print("load_df_into_database() done: result = ", result)
    except Exception as e:
        print("load_df_into_database() error: ", e)
