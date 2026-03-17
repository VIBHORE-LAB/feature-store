from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "feature-store"
    app_env: str = "development"
    log_level: str = "INFO"

    postgres_host: str = "localhost"
    postgres_post: int = 5432
    postgres_db: str = "feature_store"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"

    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0

    grpc_host: str = "0.0.0.0"
    grpc_post: int = 50051

    default_cache_ttl_seconds: int = 300

    model_config = SettingsConfigDict(
        env_file=".env"
        case_sensitive=False
        extra="ignore"
    )

    @property
    def sqlalchemy_database_uri(self) -> str:
        return (
            
        )