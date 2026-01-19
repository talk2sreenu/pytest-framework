class Constants:
    # API Endpoints
    API_BASE_URL = "https://api.example.com/v1/"
    USER_ENDPOINT = f"{API_BASE_URL}users/"
    AUTH_ENDPOINT = f"{API_BASE_URL}auth/"

    # Database Configuration
    DB_HOST = "localhost"
    DB_PORT = 5432
    DB_NAME = "example_db"
    DB_USER = "db_user"
    DB_PASSWORD = "secure_password"

    # Application Settings
    APP_NAME = "ExampleApp"
    VERSION = "1.0.0"
    DEBUG_MODE = True

    # File Paths
    LOG_FILE_PATH = "/var/log/example_app.log"
    CONFIG_FILE_PATH = "/etc/example_app/config.yaml"

    # Other Constants
    MAX_RETRIES = 5
    TIMEOUT_SECONDS = 30