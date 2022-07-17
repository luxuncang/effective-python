import asyncio
from effective import Effective

effective = Effective({'a': lambda: 'main'})

async def test1(name):
    effective = Effective(a = lambda: 'test1')
    while True:
        print('test1: ', Effective.perform(name))
        await asyncio.sleep(1)

async def test2(name):
    effective = Effective(b = lambda: 'test2')
    while True:
        print('test2: ', Effective.perform(name))
        await asyncio.sleep(1)


loop = asyncio.get_event_loop()
loop.create_task(test1('a'))
loop.create_task(test2('b'))
loop.run_forever()