# asyncio in depth
from time import perf_counter
import asyncio
import logging

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] - [%(levelname)s]: %(message)s"
)


# Methods or should i say `Coroutines`?
async def check():
    await asyncio.sleep(1)  # Simulating a delay
    logging.info("all good here!!")


async def greet_user(name):
    logging.info(f"Hello {name}!!")
    await asyncio.sleep(2)  # Simulating a delay

    # important we should await here,
    # and we should not use time.sleep

    logging.info(f"Goodbye {name}!!")


async def main():
    start = perf_counter()
    await greet_user("One")
    await check()

    logging.info(f"Time taken: {perf_counter() - start:.3f} seconds")

    start = perf_counter()
    greet_task = asyncio.create_task(greet_user("Two"))
    check_task = asyncio.create_task(check())
    await greet_task
    await check_task

    logging.info(f"Time taken: {perf_counter() - start:.3f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
