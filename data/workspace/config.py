from phidata.app.postgres import PostgresDb
from phidata.workspace import WorkspaceConfig
from phidata.infra.docker.config import DockerConfig

######################################################
## Configure the dev environment running locally on docker
## Applications:
##  - Dev database: A postgres db running in a container for dev data
######################################################

dev_db = PostgresDb(
    name="dev-db",
    postgres_db="dev",
    postgres_user="dev",
    postgres_password="dev",
    # You can connect to this db on port 5532 (on the host machine)
    container_host_port=5532,
)
dev_docker_config = DockerConfig(
    apps=[dev_db],
)

## Configure the workspace
workspace = WorkspaceConfig(
    docker=[dev_docker_config],
)
