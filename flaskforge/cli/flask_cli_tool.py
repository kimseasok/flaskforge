#!/usr/bin/env python

import argparse
from flaskforge.flask_cli import FlaskCli


def main():
    """
    Main function to initialize and configure the Flask CLI tool.

    This function sets up various CLI commands for managing Flask projects, generating
    API resources, and configuring authentication. It allows you to initialize a new
    Flask project, create models and resources, set up authentication, and manage
    relationships between models.

    TODO:
    - Add support for configuring environment variables during project initialization.
    - Implement a command to generate or update configuration files for various environments.
    - Create commands for adding and managing database migrations.
    - Provide detailed documentation for each command and argument.
    - Add validation for argument inputs to ensure correct usage.
    """
    # Create an instance of the FlaskCli
    flask_cli = FlaskCli()

    # Define the "initapp" command for initializing a new Flask project
    flask_cli.create_command(
        "initapp",
        """
        Initialize a new Flask project with optional configurations. This command sets up a
        basic Flask application structure with the ability to customize certain features.

        Example:
            $ flask initapp my_project --jwt-enable=False --swagger-enable=True
            Initializes a new Flask project named 'my_project' with JWT authentication disabled
            and Swagger documentation enabled.
        """,
    )
    flask_cli.add_argument(
        "initapp",
        "project",
        help="""
        The name of the new Flask project you wish to create. This will be used to name the 
        project directory and other initial files.

        Example:
            $ flask initapp my_project
            Creates a new Flask project directory named 'my_project'.
        """,
    )
    flask_cli.add_argument(
        "initapp",
        "--jwt-enable",
        help="""
        Enable or disable JSON Web Token (JWT) authentication for the new project. Defaults
        to True (enabled). Set to False to disable JWT authentication.

        Example:
            $ flask initapp my_project --jwt-enable=False
            Creates a project with JWT authentication disabled.
        """,
        type=bool,
        default=True,
    )
    flask_cli.add_argument(
        "initapp",
        "--swagger-enable",
        help="""
        Enable or disable Swagger OpenAPI documentation for the new project. Defaults to True
        (enabled). Set to False to disable Swagger documentation.

        Example:
            $ flask initapp my_project --swagger-enable=False
            Creates a project with Swagger documentation disabled.
        """,
        type=bool,
        default=True,
    )
    flask_cli.add_argument(
        "initapp",
        "--use-docker",
        action="store_true",
        help="""
        Use Docker for the project setup. This option will create Docker configuration files 
        and set up the project environment for Docker use.

        Example:
            $ flask initapp my_project --use-docker
            Initializes a project with Docker configuration files.
        """,
    )
    flask_cli.add_argument(
        "initapp",
        "--force",
        action="store_true",
        help="""
        Forcefully overwrite existing project files if they already exist. Use this option to
        create the project even if it conflicts with existing files or directories.

        Example:
            $ flask initapp my_project --force
            Overwrites any existing files or directories with the same name.
        """,
    )

    # Define the "create" command for generating API resources
    flask_cli.create_command(
        "create",
        """
        Generate API resources, including models and their associated endpoints. This command
        helps you quickly scaffold out the essential components for your API.

        Example:
            $ flask create User --endpoints GET,POST --getter-setter
            Generates a User model with GET and POST endpoints, including getter and setter methods.
        """,
    )
    flask_cli.add_argument(
        "create",
        "model",
        help="""
        The name of the model to be generated. This will create a model class and optionally 
        generate associated endpoints based on your specifications.

        Example:
            $ flask create User
            Generates a model class named 'User'.
        """,
    )
    flask_cli.add_argument(
        "create",
        "--getter-setter",
        help="""
        Automatically generate getter and setter methods for private properties in the model class.
        Use this flag to include these methods in the generated model.

        Example:
            $ flask create User --getter-setter
            Generates getter and setter methods for the User model.
        """,
        action="store_true",
    )
    flask_cli.add_argument(
        "create",
        "--endpoints",
        help="""
        Specify a list of HTTP methods (e.g., 'GET,POST') for which endpoints should be generated
        for the model. Provide comma-separated values for multiple methods.

        Example:
            $ flask create User --endpoints GET,POST
            Creates endpoints for GET and POST methods for the User model.
        """,
        type=str,
        nargs="+",
    )
    flask_cli.add_argument(
        "create",
        "--exclude-endpoints",
        help="""
        Specify a list of HTTP methods (e.g., 'DELETE') to exclude from the generated endpoints
        for the model. Provide comma-separated values for multiple methods.

        Example:
            $ flask create User --exclude-endpoints DELETE
            Creates all endpoints for the User model except for DELETE.
        """,
        type=str,
        nargs="+",
    )
    flask_cli.add_argument(
        "create",
        "--model-only",
        help="""
        Generate only the model class without creating additional resources such as endpoints.
        Use this flag to limit the generation to the model only.

        Example:
            $ flask create User --model-only
            Generates only the User model without any endpoints.
        """,
        action="store_true",
        default=False,
    )
    flask_cli.add_argument(
        "create",
        "--use-search",
        action="store_true",
        help="""
        Use a search method instead of the default get_all method for querying records.

        Example:
            $ flask create User --use-search
            Uses a search method for querying records of the User model.
        """,
    )
    flask_cli.add_argument(
        "create",
        "--use-single",
        action="store_true",
        help="""
        Use a search method instead of the default get_all method for querying a single record.

        Example:
            $ flask create User --use-single
            Uses a search method for querying a single record of the User model.
        """,
    )
    flask_cli.add_argument(
        "create",
        "--param",
        help="""
        Specify the name of the query string parameter used for filtering results.

        Example:
            $ flask create User --param status
            Uses 'status' as the query string parameter for filtering User records.
        """,
    )
    flask_cli.add_argument(
        "create",
        "--type",
        help="""
        Specify the type of the query string parameter (e.g., 'int', 'string').

        Example:
            $ flask create User --type int
            Specifies the query string parameter type as integer.
        """,
    )
    flask_cli.add_argument(
        "create",
        "--force",
        action="store_true",
        help="""
        Overwrite existing model files if they already exist. Use this option to regenerate 
        model files, replacing any existing files.

        Example:
            $ flask create User --force
            Overwrites existing User model files if they exist.
        """,
    )

    # Define the "create:authentication" command for setting up authentication resources
    flask_cli.create_command(
        "create:authentication",
        """
        Generate authentication-related resources for a specified model. This command sets up
        the necessary components to support authentication features for the given model.

        Example:
            $ flask create:authentication User --username-field email --password-field password
            Sets up authentication for the User model using 'email' as the username field and
            'password' as the password field.
        """,
    )
    flask_cli.add_argument(
        "create:authentication",
        "model",
        help="""
        The name of the model to be used for authentication. This model will be configured to
        handle authentication-related operations.

        Example:
            $ flask create:authentication User
            Sets up authentication for the User model.
        """,
    )
    flask_cli.add_argument(
        "create:authentication",
        "--username-field",
        required=True,
        help="""
        Specify the name of the field in the model that will be used to store the username for
        authentication purposes.

        Example:
            $ flask create:authentication User --username-field email
            Uses 'email' as the username field for authentication in the User model.
        """,
    )
    flask_cli.add_argument(
        "create:authentication",
        "--password-field",
        required=True,
        help="""
        Specify the name of the field in the model that will be used to store the password for
        authentication purposes.

        Example:
            $ flask create:authentication User --password-field password
            Uses 'password' as the password field for authentication in the User model.
        """,
    )

    # Define the "create:relationship" command for generating custom relationships between models
    flask_cli.create_command(
        "create:relationship",
        """
        Generate a custom relationship between two models. This command helps you define how
        two models are related in your application.

        Example:
            $ flask create:relationship Parent Child --relation 1 --use-child-backref
            Creates a one-to-many relationship from Parent to Child with a backref in the Child model.
        """,
    )
    flask_cli.add_argument(
        "create:relationship",
        "parent",
        help="""
        Specify the parent model class. This is the model that will contain the relationship field.

        Example:
            $ flask create:relationship Parent Child
            Specifies 'Parent' as the model that will contain the relationship field.
        """,
    )
    flask_cli.add_argument(
        "create:relationship",
        "child",
        help="""
        Specify the child model class. This is the model that will be related to the parent model.

        Example:
            $ flask create:relationship Parent Child
            Specifies 'Child' as the model that will be related to the parent model.
        """,
    )
    flask_cli.add_argument(
        "create:relationship",
        "--relation",
        type=int,
        default=0,
        help="""
        Specify the type of relationship between the models. For example:
            0 for zero or one relationship (one-to-one),
            1 for one and only one relationship (one-to-one with required validation)
            2 for zero or many relationship (one-to-many)
            3 for at least one relationship (many-to-many with required validation)
            8 for many-to-may relationship.

        Example:\n
            $ flask create:relationship Parent Child --relation 1
            Creates a many-to-many relationship between Parent and Child models.
        """,
    )
    flask_cli.add_argument(
        "create:relationship",
        "--use-child-backref",
        action="store_true",
        help="""
        If this flag is set, a backref will be added to the child model, allowing for easy
        access back to the parent model.

        Example:
            $ flask create:relationship Parent Child --use-child-backref
            Adds a backref to the Child model for easy access back to the Parent model.
        """,
    )

    # Define the "create:resource" command for generating resource-related components
    flask_cli.create_command(
        "create:resource",
        """
        Generate resource-related components for a specified model. This includes setting up
        routes and endpoints for managing resources related to the model.

        Example:
            $ flask create:resource User --name userResource --endpoints GET,POST
            Creates resource-related components for the User model with GET and POST endpoints.
        """,
    )
    flask_cli.add_argument(
        "create:resource",
        "model",
        help="""
        The name of the model for which resource-related components should be generated. This
        will set up the necessary infrastructure for managing resources of the specified model.

        Example:
            $ flask create:resource User
            Generates resource-related components for the User model.
        """,
    )
    flask_cli.add_argument(
        "create:resource",
        "--name",
        help="""
        Specify the name of the resource to be created. This name will be used for the resource
        and its associated components.

        Example:
            $ flask create:resource User --name userResource
            Specifies 'userResource' as the name for the generated resource.
        """,
        required=True,
    )
    flask_cli.add_argument(
        "create:resource",
        "--endpoints",
        help="""
        Specify a list of HTTP methods (e.g., 'GET,POST') for which endpoints should be generated
        for the resource. Provide comma-separated values for multiple methods.

        Example:
            $ flask create:resource User --endpoints GET,POST
            Creates endpoints for GET and POST methods for the resource.
        """,
        type=str,
        nargs="+",
    )
    flask_cli.add_argument(
        "create:resource",
        "--exclude-endpoints",
        help="""
        Specify a list of HTTP methods (e.g., 'DELETE') to exclude from the generated endpoints
        for the resource. Provide comma-separated values for multiple methods.

        Example:
            $ flask create:resource User --exclude-endpoints DELETE
            Excludes DELETE method from the generated endpoints for the resource.
        """,
        type=str,
        nargs="+",
    )
    flask_cli.add_argument(
        "create:resource",
        "--url-prefix",
        help="""
        Specify the URL prefix for the resource routes. This is useful for grouping related
        routes under a common prefix.

        Example:
            $ flask create:resource User --url-prefix /api/v1
            Sets the URL prefix for the resource routes to '/api/v1'.
        """,
    )
    flask_cli.add_argument(
        "create:resource",
        "--use-search",
        action="store_true",
        help="""
        Use a search method instead of the default get_all method for querying resources.

        Example:
            $ flask create:resource User --use-search
            Uses a search method for querying resources.
        """,
    )
    flask_cli.add_argument(
        "create:resource",
        "--use-single",
        action="store_true",
        help="""
        Use a search method instead of the default get_all method for querying a single resource.

        Example:
            $ flask create:resource User --use-single
            Uses a search method for querying a single resource.
        """,
    )
    flask_cli.add_argument(
        "create:resource",
        "--param",
        help="""
        Specify the name of the query string parameter used for filtering resources.

        Example:
            $ flask create:resource User --param status
            Uses 'status' as the query string parameter for filtering resources.
        """,
    )
    flask_cli.add_argument(
        "create:resource",
        "--type",
        help="""
        Specify the type of the query string parameter (e.g., 'int', 'string').

        Example:\n
            $ flask create:resource User --type int
            Specifies the query string parameter type as integer.
        """,
    )
    flask_cli.create_command(
        "migrate",
        """
        Manage database migrations using Alembic within a Docker container. This command
        allows you to perform operations such as upgrading, downgrading, and creating
        new revisions. You can pass arbitrary Alembic arguments to the command.

        Example:
            $ flask migrate revision --autogenerate --message "create table user" --container my_container
            Creates a new Alembic revision inside the Docker container named 'my_container'.
        """,
    )
    flask_cli.add_argument(
        "migrate",
        "operation",
        help="""
        The Alembic operation to perform. This could be 'upgrade', 'downgrade', 'revision', etc.

        Example:
            $ flask migrate revision --autogenerate --message "create table user" --container my_container
            Executes the 'revision' operation for creating a new database revision.
        """,
    )

    flask_cli.add_argument(
        "migrate",
        "--container",
        default="api",
        help="""
        The name of the Docker container where Alembic should be executed.

        Example:
            $ flask migrate revision --autogenerate --message "create table user" --container my_container
            Specifies 'my_container' as the Docker container for running Alembic commands.
        """,
    )
    flask_cli.add_argument(
        "migrate",
        "--alembic-args",
        help="""
        Arbitrary arguments to pass to the Alembic command. Use this to specify options
        like '--autogenerate' or '--message "create table user"'.

        Example:
            $ flask migrate revision --autogenerate --message "create table user" --container my_container
            Passes '--autogenerate --message "create table user"' as arguments to the Alembic command.
        """,
        nargs=argparse.REMAINDER,
    )

    # Parse arguments and execute the appropriate command
    flask_cli.init()


if __name__ == "__main__":
    main()
