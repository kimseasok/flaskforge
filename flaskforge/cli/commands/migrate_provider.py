import os

from flaskforge.utils.commons import exec_command, join_path

from .base_cli_provider import AbstractProvider


class MigrateProvider(AbstractProvider):
    def handler(self, args: object):

        docker = f"""docker exec -it {args.container}"""

        user_docker = os.path.isfile(join_path(self.project_path, "Dockerfile"))

        if (
            user_docker
            and exec_command(f"docker ps -q -f name={args.container}") == ""
            and self.io.confirm(
                """api container was not found!
        Would you like to up docker services before execute the command"""
            )
            == "yes"
        ):
            exec_command("docker-compose up -d")

        operation = f"{docker} {args.operation}" if user_docker else args.operation

        alembic_args = " ".join(args.alembic_args)

        full_command = f"""{operation} {alembic_args}"""

        exec_command(full_command)
