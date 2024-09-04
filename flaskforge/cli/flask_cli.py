import argparse
from flaskforge.commands.provider_factory import ProviderFactory


class FlaskCli:
    """
    Singleton class for managing Flask command-line interface (CLI) tools.

    This class provides a centralized way to define and manage CLI commands for
    a Flask application. It uses the singleton pattern to ensure that only one
    instance of the CLI tool is created, allowing consistent command management
    throughout the application.

    Attributes:
        provider (ProviderFactory): The factory used to generate command functions.
    """

    _instance = None
    provider = ProviderFactory

    def __new__(cls, *args, **kwargs):
        """
        Ensure that only one instance of FlaskCli is created (singleton pattern).

        This method checks if an instance of FlaskCli already exists. If not,
        it creates and returns a new instance. Otherwise, it returns the existing
        instance.

        Returns:
            FlaskCli: The singleton instance of FlaskCli.
        """
        if not cls._instance:
            cls._instance = super(FlaskCli, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        """
        Initialize the FlaskCli instance.

        Sets up the argument parser and command storage. This method is only run
        once due to the singleton pattern.

        TODO:
            - Add error handling for initialization failures.
        """
        if not hasattr(self, "initialized"):
            self.initialized = True
            # Initialize the argument parser with a description of the CLI tool
            self.parser = argparse.ArgumentParser(
                description="""
                Flask CLI Tool for Managing Flask Projects and Resources.

                This CLI tool helps you initialize Flask projects, generate API resources,
                set up authentication, and manage relationships between models.
                """,
                formatter_class=argparse.RawTextHelpFormatter,
            )
            # Create subparsers for different commands with a general help message
            self.sub_parser = self.parser.add_subparsers(
                dest="command", help="Available commands for managing Flask projects"
            )
            self.command = {}

    def init(self):
        """
        Parse command-line arguments and execute the corresponding command function.

        This method processes the arguments passed to the CLI and invokes the function
        associated with the specified command. If the command is not recognized, it
        prints the help message.

        TODO:
            - Implement error handling for unknown commands and invalid arguments.
            - Add logging to capture command execution details and errors.
        """
        args = self.parser.parse_args()
        if args.command in self.command:
            # Call the function associated with the command
            self.command[args.command]["function"](args)
        else:
            # Print help if the command is not recognized
            self.parser.print_help()

    def create_command(self, name: str, help: str):
        """
        Register a new command with the CLI tool.

        This method adds a new command to the CLI tool and associates it with a
        function from the provider factory. The command's help text provides a brief
        description of what the command does.

        Args:
            name (str): The name of the command to be added.
            help (str): A brief description of the command's functionality.

        TODO:
            - Add support for command aliases.
            - Validate that the command name is unique.
        """
        # Create a parser for the new command with detailed help text
        command_parser = self.sub_parser.add_parser(
            name, help=help, formatter_class=argparse.RawTextHelpFormatter
        )
        # Register the command function using the provider
        command_function = self.provider(name)
        self.command[name] = {
            "parser": command_parser,
            "function": command_function,
        }

    def add_argument(self, command: str, name: str, *args, **kwargs):
        """
        Add an argument to a specified command's parser.

        This method adds an argument to the parser for a specific command, allowing
        for additional options and configurations. The argument can be required or
        optional, and its properties are defined using argparse.

        Args:
            command (str): The name of the command to which the argument should be added.
            name (str): The name of the argument. For optional arguments, it should start with '--'.
            *args: Positional arguments for argparse.add_argument().
            **kwargs: Keyword arguments for argparse.add_argument().

        TODO:
            - Validate argument configurations to ensure they are correctly set up.
            - Implement support for dynamically adding or removing arguments.
        """
        parser = self.command[command]["parser"]
        parser.add_argument(name, *args, **kwargs)
