# -*- coding:utf-8 -*-

import uvicorn
from fastapi import Request, Form
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, HTMLResponse

from sign import *

disable_warnings()

server = FastAPI()


@server.exception_handler(RequestValidationError)
async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    try:
        error_keys = []
        for element in exc.errors():
            error_keys.append(element['loc'][1])
        return JSONResponse({"code": "400", "msg": f"请传入 {'、'.join(error_keys)} 键！", "data": {}})
    except IndexError:
        if "type_error.dict" in str(exc.errors()):
            return JSONResponse({"code": "400", "msg": "请将data=data改为json=data或用data=json.dumps(data)！", "data": {}})
        else:
            return JSONResponse({"code": "400", "msg": exc.errors(), "data": {}})


@server.get("/", response_class=HTMLResponse)
async def hello():
    return """
    <html>
        <body>
            <h1>Hello World!</h1>
        </body>
    </html>
    """


@server.post('/sign')
async def server_sign(
        fn: str = Form(...),
        url: str = Form(...),
        action: str = Form(...)
):
    body = f'"{action}": "{url}"'
    res_sign = func_sign(fn, body)
    return_json = {
        "code": 200,
        "msg": "ok",
        "data": {
            "fn": fn,
            "body": f'body={quote(body)}&{res_sign}',
        }
    }
    return JSONResponse(return_json)
    

@server.post('/genToken')
async def server_genToken(
        url: str = Form(...)
):
    body = '{"to":"%s"}' % url
    res_sign = func_sign("genToken", body)
    return_json = {
        "code": 200,
        "data": {
                "sign": res_sign,
                "body": f'body={quote(body)}',
            }
    }
    return JSONResponse(return_json)


if __name__ == '__main__':
    uvicorn.run("app:server", host='0.0.0.0', port=80, debug=True)
