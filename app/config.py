from pydantic.env_settings import BaseSettings


# setting up validation for environment variables
class Settings(BaseSettings):
    database_password: str = ""
    database_username: str = ""
    database_port: str = ""
    database_hostname: str = ""
    database_name: str = ""
    secret_key: str = ""
    algorithm: str = ""
    access_token_expire_minutes: int = 30

    # path to env file
    class Config:
        env_file = ".env"


settings = Settings()

# if __name__=='__main__':
#     import secrets
#     print(secrets.token_urlsafe(512))