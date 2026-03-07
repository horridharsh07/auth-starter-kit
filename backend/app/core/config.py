from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Auth Starter Kit"

    DATABASE_URL: str = "postgresql://neondb_owner:npg_ngx2uOs8HyrS@ep-bitter-hall-a4cvqqlu-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

    JWT_SECRET: str = "MAITRI_MERI_BIWI_HAI"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15

    class Config:
        env_file = ".env"


settings = Settings()