from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # DATABASE_URL: str
    # JWT_SECRET: str
    # JWT_ALGORITHM: str
    # REDIS_URL: str = "redis://localhost:6379/0"
    # MAIL_USERNAME: str
    # MAIL_PASSWORD: str
    # MAIL_FROM: str
    # MAIL_PORT: int
    # MAIL_SERVER: str
    # MAIL_FROM_NAME: str
    # MAIL_STARTTLS: bool = True
    # MAIL_SSL_TLS: bool = False
    # VALIDATE_CERTS: bool = True
    
    # API Config & Auth
    APP_DOMAIN: str
    ALLOWED_HOSTS: str
    ALLOWED_ORIGINS: str
    ALLOWED_METHODS: str
    ALLOWED_HEADERS: str
    ALLOW_CREDENTIALS:bool = True

    # NetCash Config
    WSDL_URL: str
    NETCASH_URL: str
    NETCASH_SERVICE_KEY: str
    NETCASH_SOFTWARE_VENDOR_KEY: str

    model_config = SettingsConfigDict(env_file="../.env", extra="ignore")


Config = Settings()


# broker_url = Config.REDIS_URL
# result_backend = Config.REDIS_URL
broker_connection_retry_on_startup = True
