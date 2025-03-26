"""
introduction to faust library usage through typical 'hello world' application
"""

import faust

app = faust.App(
    "hello_world",
    broker="kafka://localhost:9092",  # if this app runs locally
    # broker="kafka://host.docker.internal:9092",  # if this app runs in docker
    value_serializer="raw",
)

wish_topic: faust.TopicT = app.topic("wishes")


@app.agent(wish_topic)
async def wish(wishes) -> None:
    async for w in wishes:
        print(w)
