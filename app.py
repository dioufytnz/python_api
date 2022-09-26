# main.py

from fastapi import FastAPI
from elasticsearch import Elasticsearch
import json

app = FastAPI()
elastic_client = Elasticsearch(
    hosts=["http://localhost:9200"], http_auth=('elastic', 'eeRSORSm4RI38Np5yN1J'))



@app.get("/iot/{index}/{user}/{device}/{kpi}/{start_time}/{end_time}")
async def search_elastic(index, user, device, kpi, start_time, end_time):
    list_result = []
    result_value = {}
    body = {
        "query": {
            "bool": {
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
                ]
            }
        }
    }
    result = elastic_client.search(index=index, body=body)
    result_value['hits'] = str(result['hits']['total']['value'])
    if result['hits']['total']['value'] >= 0:
        list_result.append(result_value)
        for hit in result['hits']['hits']:
            temp_dict = hit["_source"]
            temp_dict['timestamp'] = temp_dict.pop('@timestamp')
            list_result.append(temp_dict)
    else:
        list_result.append(result_value)

    result
    return list_result