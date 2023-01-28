import asyncio

async def send_hello():
    await asyncio.sleep(2)
    print('Hello!')


async def send_bye():
    await asyncio.sleep(1)
    print('Bye!')


async def main():
    task_1 = send_hello()
    task_2 = send_bye()

    await task_1
    await task_2


asyncio.run(main())
