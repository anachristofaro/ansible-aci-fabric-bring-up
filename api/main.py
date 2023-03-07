from fastapi import FastAPI
import modules.index
import modules.bring_up

app = FastAPI()

# get methods and default pages section
@app.get("/")
async def index():
    return (modules.index.info())

@app.get("/bring_up")
def index_device():
    return (modules.bring_up.info())

# post methods to execute operations such as bring_up

@app.post("/bring_up")
async def initialize(item: modules.bring_up.BringUp):
    return (modules.bring_up.run_play(item))