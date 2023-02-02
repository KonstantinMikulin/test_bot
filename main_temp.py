import asyncio


async def send_one():
    n = 0
    while True:
        await asyncio.sleep(1)
        n += 1
        if n % 3 != 0:
            print(f'Прошло {n} секунд')
        elif n % 3 == 0:
            print('Прошло еще три секунды')


async def main():
    task_1 = asyncio.create_task(send_one())

    await task_1


if __name__ == '__main__':
    asyncio.run(main())
