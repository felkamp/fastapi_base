from aiokafka import AIOKafkaConsumer
import asyncio



async def consume():
    consumer = AIOKafkaConsumer(
        'tst', bootstrap_servers='kafka-1:9095',
        group_id='tst_group',
    )
    await consumer.start()
    batch = []
    try:
        async for msg in consumer:
            print('wait top')
            print(f"consumed: , topic-{msg.topic}, partition-{msg.partition}, offset-{msg.offset}, key-{msg.key}, value-{msg.value}, timestamp-{msg.timestamp}")
            print('wait bottoom')
    finally:
        print('stopping')
        await consumer.stop()