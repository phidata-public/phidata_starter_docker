from phidata.app.devbox import Devbox
from phidata.app.postgres import PostgresDb

from phidata.workspace import WorkspaceConfig
from phidata.infra.docker.config import DockerConfig

######################################################
## Configure the dev environment running locally on docker
## Applications:
##  - Devbox: A containerized environment for testing and debugging workflows.
##  - Dev database: A postgres db running in a container for dev data
######################################################

pg_db_name = "pg_db"
pg_db = PostgresDb(
    name=pg_db_name,
    postgres_db="dev",
    postgres_user="dev",
    postgres_password="dev",
    # You can connect to this db on port 5532 (on the host machine)
    container_host_port=5532,
)
devbox = Devbox(
    # Init Airflow webserver when the container starts
    init_airflow_webserver=True,
    db_connections={pg_db_name: pg_db.get_connection_url_docker()},
    create_airflow_test_user=True,
)
dev_docker_config = DockerConfig(
    apps=[devbox, pg_db],
)

## Configure the workspace
workspace = WorkspaceConfig(
    docker=[dev_docker_config],
)
