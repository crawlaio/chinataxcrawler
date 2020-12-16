# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI, Query

from crawler.main import main

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
    result = main(fpdm=fpdm, fphm=fphm, kprq=kprq, jym=jym)
    return result


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        debug=True,
        reload=True,
    )
