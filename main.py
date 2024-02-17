from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from core import refresh
import asyncio
import json

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
def hello():
    return 'Hello, World!'

@app.get('/api/refresh')
async def router_refresh():
    await refresh()
    with open('status.json', 'r') as file:
        status_data = json.load(file)
    return JSONResponse(content=status_data)

@app.get('/api/status')
def router_status():
    with open('status.json', 'r') as file:
        status_data = json.load(file)
    return JSONResponse(content=status_data)

@app.get('/api/status/{certname}')
def router_status_cert(certname: str):
    with open('status.json', 'r') as file:
        status_data = json.load(file)
    return JSONResponse(content=status_data[certname])

@app.get('/api/download/{certname}')
def download_cert(certname: str):
    return FileResponse(path=f'Cert/{certname}.zip', filename=f'{certname}.zip')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)

