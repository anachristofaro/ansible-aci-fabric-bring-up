from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
import ansible_runner



class BringUp(BaseModel):
    operation: str
    username: Union[str, None] = None
    password: Union[str, None] = None

def info():
    return ({"message": "Welcome to Ansible ACI Fabric API"})

def run_play(signal):
    if signal.operation == "start":
        r = ansible_runner.run(private_data_dir='../../', playbook='../../bring-up.yml')
        return ({"message": "Running bring-up.yml..."}, "{}: {}".format(r.status, r.rc))
    else:
        return ({"message": "Bring up operation not authorized"})