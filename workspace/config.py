from phidata.app.postgres import PostgresDb
from phidata.infra.docker.config import DockerConfig
from phidata.workspace import WorkspaceConfig

ws_key = "phidata-starter-docker"

# -*- Configure docker resources

# Dev database: A postgres instance for storing dev data
dev_db = PostgresDb(
    name="dev-db",
    db_user="dev",
    db_password="dev",
    db_schema="dev",
    # You can connect to this db on port 5532
    container_host_port=5532,
)

# -*- Define the DockerConfig
dev_docker_config = DockerConfig(
    apps=[dev_db],
)

# -*- Define the WorkspaceConfig
workspace = WorkspaceConfig(
    docker=[dev_docker_config],
)
