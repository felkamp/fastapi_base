import asyncio

from fastapi import FastAPI

from src.db.base import init_db
from src.api.routes import api_router
from aiokafka import AIOKafkaConsumer

import logging

logging.basicConfig(level=logging.INFO)

loop = asyncio.get_event_loop()
consumer = AIOKafkaConsumer(
     *['tst', 'tst2'], bootstrap_servers='kafka-0:9092',
    group_id='tst_group',
    loop=loop,
)

async def consume():
    await consumer.start()
    batch = []
    try:
        async for msg in consumer:
            logging.info('wait top')
            logging.info(f"consumed: , topic-{msg.topic}, partition-{msg.partition}, offset-{msg.offset}, key-{msg.key}, value-{msg.value}, timestamp-{msg.timestamp}")
            logging.info('wait bottoom')
    except Exception as e:
        logging.info(str(e))
    finally:
        logging.info('stopping')
        await consumer.stop()


async def on_startup():
    app.router.include_router(api_router, prefix='/api/v1')
    loop.create_task(consume())

async def on_shutdown():
    await consumer.stop()



app = FastAPI(
    title='Base fastapi app',
    version='0.0.1',
    docs_url='/docs',
    openapi_url='/openapi',
    on_startup=[on_startup],
    on_shutdown=[on_shutdown],
)
