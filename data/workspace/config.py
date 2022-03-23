from phidata.app.devbox import Devbox
from phidata.app.postgres import PostgresDb
from phidata.app.superset import Superset

from phidata.workspace import WorkspaceConfig
from phidata.infra.docker.config import DockerConfig

######################################################
## Configure the dev environment running locally on docker
## Applications:
##  - Devbox: A containerized environment for testing and debugging workflows.
##  - Dev database: A postgres db running in a container for dev data
######################################################

dev_pg_name = "dev_pg"
dev_pg = PostgresDb(
    name=dev_pg_name,
    postgres_user="dev",
    postgres_db="dev",
    postgres_password="dev",
    # You can connect to this db on port 5532 (on the host machine)
    container_host_port=5532,
)
devbox = Devbox(
    # Init Airflow webserver when the container starts
    init_airflow_webserver=True,
    db_connections={dev_pg_name: dev_pg.get_connection_url_docker()},
    create_airflow_test_user=True,
)
superset = Superset(enabled=False)
dev_docker_config = DockerConfig(
    apps=[devbox, dev_pg, superset],
)

## Configure the workspace
workspace = WorkspaceConfig(
    docker=[dev_docker_config],
)
