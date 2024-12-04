# secure_script.py
import os
import sys
from typing import Optional


def get_required_env_var(var_name: str) -> str:
    """Safely get an environment variable."""
    value = os.environ.get(var_name)
    if value is None:
        raise ValueError(f"Required environment variable '{var_name}' is not set")
    return value


def get_optional_env_var(var_name: str, default: str = None) -> Optional[str]:
    """Get an optional environment variable with a default value."""
    return os.environ.get(var_name, default)


def main():
    try:
        # Get required variables
        api_key = get_required_env_var("API_KEY")
        database_url = get_required_env_var("DATABASE_URL")

        # Get optional variables
        debug_mode = get_optional_env_var("DEBUG_MODE", "False").lower() == "true"

        # Your secure script logic here
        if debug_mode:
            print("Debug mode enabled")
            print(f"Using database: {database_url}")
            # Never print sensitive information like API keys

    except ValueError as e:
        print(f"Configuration error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
