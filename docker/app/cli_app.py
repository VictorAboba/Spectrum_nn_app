from fastapi import FastAPI


cli_app = FastAPI()


@cli_app.get("/")
def hello_world():
    return {"": "Hello World From Cli app"}
