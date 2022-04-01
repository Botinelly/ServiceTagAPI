from fastapi import Response, FastAPI
from random import choice
import uvicorn

app = FastAPI()

@app.get("/getServiceTagbySN")
def getServiceTagbySN(sn: str):
    test = sn
    sn = choice([sn, "8R33926O00QS", "2LCYHS2", "JQ8F2W2", "", "TR50278"])
    media_type = choice(["text/xml", "application/json"])
    if test == "TR50278":
        sn = "JQ8F2W2"
        media_type = "text/xml"
    if media_type == "text/xml":
        data = '<?xml version="1.0" encoding="utf-8"?>'
        data += f'<string xmlns="http://sfis.tpvaoc.com/COMMON">{sn}</string>'
    else:
        data = "ORA-12638: Credential retrieval failed"
    return Response(content=data, media_type=media_type)


if __name__ == "__main__":

    uvicorn.run("run:app", host="0.0.0.0", port=5000, log_level="info")
