from typing import Optional

from fastapi import FastAPI

from client import get_exchange_rate_banxico, get_exchange_rate_fixer, get_exchange_rate_diario

app = FastAPI()

@app.get("/")
def read_root():
    res_banxico = get_exchange_rate_banxico()
    res_fixer = get_exchange_rate_fixer()
    res_diario = get_exchange_rate_diario()
    return  {
    'rates':
    {
    'banxico': res_banxico,
    'fixer': res_fixer,
    'diario': res_diario
    }
    }
