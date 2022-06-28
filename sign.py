# -*- coding:utf-8 -*-

import base64
import hashlib
import time
import uuid
from urllib.parse import quote

from Crypto.Cipher import AES
from fastapi import FastAPI
from urllib3 import disable_warnings

disable_warnings()

server = FastAPI()


def sub(arg1, arg2, arg3):
    return arg1 + arg2 + arg3


def encrypt(code):
    return code


def func_sign(
        functionId,
        body,
        client="apple",
        clientVersion="10.3.6"
):
    uid = "".join(str(uuid.uuid4()).split("-"))
    st = str(int(time.time() * 1000))
    random1, random2 = 2, 0
    sv = f"{random1}{random2}"
    lists = [
        f"functionId={functionId}",
        f"body={body}",
        f"uuid={uid}",
        f"client={client}",
        f"clientVersion={clientVersion}",
        f"st={st}",
        f"sv=1{sv}"
    ]
    ret_bytes = sub(str.encode("&".join(lists)), random1, random2)
    lists = [
        f"body={quote(body)}",
        f"client={client}",
        f"clientVersion={clientVersion}",
        f"uuid={uid}",
        f"st={st}",
        f"sign={hashlib.md5(base64.b64encode(ret_bytes)).hexdigest()}",
        f"sv=1{sv}"
    ]
    return "&".join(lists)
