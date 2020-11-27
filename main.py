# -*- coding: utf-8 -*-
from fastapi import FastAPI, Query

from crawler.main import get_address, main

tags_metadata = [
    {"name": "chinastax", "description": "国家税务总局全国增值税发票查验平台 API"},
]
app = FastAPI(
    title="国家税务总局全国增值税发票查验平台 API",
    openapi_tags=tags_metadata,

    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
    openapi_url="/api/v1/openapi.json",
)


@app.get("/", tags=['chinastax'])
async def chinastax(
    fpdm: str = Query(None, example="011001900511", description="发票代码"),
    fphm: str = Query(None, example="13093557", description="发票号码"),
    kprq: str = Query(None, example="20191111", description="开票日期"),
    jym: str = Query(None, example="821713", description="校验码后 6 位"),
):
    query_info = {
        "fpdm": fpdm,  # 发票代码
        "fphm": fphm,  # 发票号码
        "kprq": kprq,  # 开票日期
        "jym": jym,  # 校验码后 6 位
    }
    query_info["address"] = get_address(**query_info)
    result = main(**query_info)
    return result
