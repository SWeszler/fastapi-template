import asyncio


async def sub():
    return "Hello"


async def sub1():
    return "World"


async def main():
    return await asyncio.gather(sub(), sub1())

res = asyncio.run(main())
print(res)
