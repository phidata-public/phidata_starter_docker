from phidata.asset.file import File
from phidata.asset.table.sql.postgres import PostgresTable
from phidata.product import DataProduct
from phidata.workflow.download.url.to_file import DownloadUrlToFile
from phidata.workflow.upload.file.to_sql import UploadFileToSql
from phidata.workflow.run.sql.query import RunSqlQuery

from data.workspace.config import pg_db

##############################################################################
## This example shows how to build a data product that calculates
## daily active users using postgres.
## Steps:
##  1. Download user_activity data from a URL.
##  2. Upload user_activity data to a postgres table
##  3. Calculate daily active users and load to a postgres table
##############################################################################

# Step 1: Download user_activity data from a URL.
# Define a File object which points to <ws_root_dir>/storage/dau/user_activity.csv
user_activity_csv = File(name="user_activity.csv", file_dir="dau")
# Create a Workflow to download the user_activity data from a URL
download = DownloadUrlToFile(
    file=user_activity_csv,
    url="https://raw.githubusercontent.com/phidata-public/demo-data/main/dau_2021_10_01.csv",
)

# Step 2: Upload user_activity data to a postgres table
# Define a postgres table named `user_activity`. Use the connection url from pg_db
user_activity_table = PostgresTable(
    name="user_activity",
    db_conn_url=pg_db.get_connection_url_local(),
)
# Create a Workflow to load the file downloaded above to the PostgresTable
upload = UploadFileToSql(
    file=user_activity_csv,
    sql_table=user_activity_table,
)

# Step 3: Calculate daily active users and load to a postgres table
daily_active_users_table = PostgresTable(
    name="daily_active_users",
    db_conn_url=pg_db.get_connection_url_local(),
)
load_dau = RunSqlQuery(
    query=f"""
    SELECT
        ds,
        SUM(CASE WHEN is_active=1 THEN 1 ELSE 0 END) AS active_users
    FROM {user_activity_table.name}
    GROUP BY ds
    ORDER BY ds
    """,
    sql_table=user_activity_table,
    show_sample_data=True,
    load_result_to=daily_active_users_table,
)


# Create a DataProduct for these tasks
dau = DataProduct(name="dau", workflows=[download, upload, load_dau])
