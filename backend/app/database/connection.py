"""Placeholder database connection configuration for future expansion."""

from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    """Default configuration used for a future DB connection layer."""

    host: str = "localhost"
    port: int = 5432
    database: str = "researchpilot"
    username: str = "postgres"

    def connection_string(self) -> str:
        return f"postgresql://{self.username}@{self.host}:{self.port}/{self.database}"

    def is_ready(self) -> bool:
        return bool(self.database and self.host)
