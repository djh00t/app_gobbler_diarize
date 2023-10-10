import os

def get_env_variable(var_name, default=None):
    """Retrieve and return the value of an environment variable."""
    value = os.getenv(var_name, default)
    if value is None:
        raise ValueError(f"Environment variable {var_name} is not set.")
    return value
