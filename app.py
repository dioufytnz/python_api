# main.py

from fastapi import FastAPI
from elasticsearch import Elasticsearch

app = FastAPI()
elastic_client = Elasticsearch(
    hosts=["http://localhost:9200"], http_auth=('elastic', 'eeRSORSm4RI38Np5yN1J'))

@app.get("/iot/{index}/{user}/{device}/{kpi}/{start_time}/{end_time}")
async def root(index, user, device, kpi, start_time, end_time):
    body = {
        "query": {
            "bool": {
                "must": [],
                "filter": [
                    {
                        "range": {
                            "@timestamp": {
                                "format": "epoch_millis",
                                "gte": start_time,
                                "lte": end_time
                            }
                        }
                    },
                    {
                        "match_phrase": {
                            "device": device
                        }
                    },
                    {
                        "match_phrase": {
                            "user": user
                        }
                    },
                    {
                        "match_phrase": {
                            "kpi": kpi
                        }
                    }
                ],
                "should": [],
                "must_not": []
            }
        }
    }

    result = elastic_client.search(index=index, body=body)
    return {"message": result}
