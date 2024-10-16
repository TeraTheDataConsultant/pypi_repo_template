import os
from openai import OpenAI
from dotenv import load_dotenv
from core_template.utils.logs import logger


class ConfigOpenAI:
    """
    Configure OpenAI Environment
    ----------------------------
    Load the .env file based on what's passed as the attribute.
    If no class attributes are passed, defaults to staging.

    Attributes
    ----------
        env: 'production' or 'staging'

    Returns
    -------
        configured client object to pass requests too

    Usage::

        >>> config = ConfigOpenAI(env='production')
        >>> print(f"Running in {config.get_environment()} environment")
        >>> print(f"Project ID: {config.get_open_ai_organization_id()}")
        >>> print(f"Project ID: {config.get_open_ai_project_id()}")

    ---
    """

    def __init__(self, env=None):
        if not env:
            env = os.getenv("ENV", "staging")

        # Load the .env file based on what's passed as the attribute
        if env == "production":
            load_dotenv(".env.production")
        else:
            load_dotenv(".env.staging")

        self.env = env

        # Initialize OpenAI Configuration
        self.organization_id = self.__get_open_ai_organization_id()
        self.project_id = self.__get_open_ai_project_id()
        self.api_key = self.__get_open_ai_api_key()

        self.client = OpenAI(
            organization=self.organization_id,
            project=self.project_id,
            api_key=self.api_key,
        )

    def __get_open_ai_organization_id(self):
        return os.getenv("open_ai_organization_id")

    def __get_open_ai_project_id(self):
        return os.getenv("open_ai_project_id")

    def __get_open_ai_api_key(self):
        return os.getenv("open_ai_api_key")

    def get_environment(self):
        """
        Checks the environment that's initialized
        """
        return self.env

    def test_client_connection(self):
        """
        Check to see if we can initialize the client with the environment
        keys. Works independently of the actual client we will use to connnect
        each environment to in the future.

        Usage::
            >>> cfg = ConfigEnv(env='staging')
            >>> cfg.test_client_connection()
        ---
        """
        try:
            logger.info(f"Current environment selected: {self.get_environment()}")
            client = OpenAI(
                organization=self.organization_id,
                project=self.project_id,
                api_key=self.api_key,
            )
            logger.debug(
                client.beta.assistants.list(limit=1)
            )  # Check to see if at least 1 assistant exists
        except Exception as error:
            logger.warning(f"Issue connecting to client: {error}")


if __name__ == "__main__":
    ConfigOpenAI()
