from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Auth Starter Kit"

    DATABASE_URL: str = "postgresql+psycopg2://postgres.huzavduooybqbcpjomdy:_HArsh020207@aws-1-ap-northeast-1.pooler.supabase.com:5432/postgres"

    JWT_SECRET: str = "MAITRI_MERI_BIWI_HAI"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    class Config:
        env_file = ".env"


settings = Settings()