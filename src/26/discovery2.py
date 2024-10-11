from fastapi import FastAPI
import uvicorn
import py_eureka_client.eureka_client as eureka_client
from contextlib import asynccontextmanager
import requests

@asynccontextmanager
async def set_eureka(app: FastAPI):
    await eureka_client.init_async(
           eureka_server='http://localhost:8761/eureka',
           app_name="discovery2",
           instance_port=8881
           )
    yield
    
app = FastAPI(lifespan=set_eureka)

@app.get('/test')
async def get_data():
    return "fastapi服务测试成功！"

@app.get('/testservice')
def get_data():
    res = eureka_client.do_service(app_name="BOB",service="/",return_type="string")
    return res
    
@app.get('/rpc')
def get_data():
    r = requests.get('http://sidecar-alice:5678/hosts/bob')
    json = r.json()
    if len(json) == 0:
        return 'Service bob is not available yet.'
    uri = json[0]['uri']
    nr = requests.get(uri)
    return nr.text + ' Through Alice.\n'

if __name__ == '__main__':
    # reload 热加载，修改了自动重启
    uvicorn.run(app='discovery2:app', port=8881) #,reload=True)
