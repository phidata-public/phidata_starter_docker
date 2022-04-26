from phidata.app.postgres import PostgresDb
from phidata.infra.docker.config import DockerConfig
from phidata.workspace import WorkspaceConfig

######################################################
## Configure docker resources
## Applications:
##  - Dev database: A postgres db running in a container for dev data
######################################################

# Dev database: A postgres instance for storing dev data
dev_db = PostgresDb(
    name="dev-db",
    db_user="dev",
    db_password="dev",
    db_schema="dev",
    # You can connect to this db on port 5532
    container_host_port=5532,
)
dev_docker_config = DockerConfig(
    apps=[dev_db],
)

## Configure the workspace
workspace = WorkspaceConfig(
    docker=[dev_docker_config],
)
