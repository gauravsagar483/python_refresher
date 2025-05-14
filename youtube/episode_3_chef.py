import asyncio
import logging
from time import perf_counter, sleep, strftime

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] - [%(levelname)s]: %(message)s"
)

logger = logging.getLogger(__name__)


async def cook_burger():
    logging.info("Grilling Burger...")
    await asyncio.sleep(2)
    logging.info("Burger is ready!")

    return "Cooked 'Burger'!!"


async def toast_bun():
    logging.info("Toasting bun...")
    await asyncio.sleep(1)
    logging.info("Bun is ready!")

    return "Cooked 'Bun'!!"


async def main():
    start = perf_counter()
    await cook_burger()
    await toast_bun()
    # These tasks are run sequentially,
    # but non-blockingly.
    # Still not optimal yet. Let’s fix that.”

    logger.info(f"Time taken to prepare order: {perf_counter() - start:.3f} seconds")


asyncio.run(main())


# Now, let’s run them concurrently using asyncio.gather().
async def prepare_order():
    start = perf_counter()
    await asyncio.gather(cook_burger(), toast_bun())
    logger.info(
        f"Time taken to prepare order (concurrently): {perf_counter() - start:.3f} seconds"
    )


asyncio.run(prepare_order())


# Timeouts


# let's say there has been some exception in method
# and you do not want to wait forever
# so you can timebound the tasks
# if they fail to return in that time,
async def async_timeouts():
    try:
        await asyncio.wait_for(cook_burger(), timeout=1)
    except asyncio.TimeoutError:
        logging.info("Burger took too long! Cancelled.")


asyncio.run(async_timeouts())


# Task Cancellation
async def async_task_cancellation():
    task = asyncio.create_task(cook_burger())
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        logging.info("Burger task was cancelled.")
    finally:
        logging.info("Cleaning up...")


asyncio.run(async_task_cancellation())


# Task groups (using Context manager)


async def async_task_groups():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(cook_burger())
        task2 = tg.create_task(toast_bun())
    logging.info(f"Both tasks have completed now: {task1.result()}, {task2.result()}")


asyncio.run(async_task_groups())


# Running in threads


def blocking_io():
    logging.info(f"start blocking_io at {strftime('%X')}")
    sleep(1)
    logging.info(f"blocking_io complete at {strftime('%X')}")


async def async_in_threads():
    logging.info(f"started async_in_threads at {strftime('%X')}")

    await asyncio.gather(asyncio.to_thread(blocking_io), asyncio.sleep(1))

    logging.info(f"finished async_in_threads at {strftime('%X')}")


asyncio.run(async_in_threads())
# Can also Use run_in_executor to offload the CPU bound tasks


# Streaming Results with as_completed()


async def async_streaming_results():
    coros = [cook_burger(), toast_bun()]

    start = perf_counter()
    for func in asyncio.as_completed(coros):
        result = await func
        logging.info(f"Task completed: {result}")

    logging.info(f"Time taken to cook: {perf_counter() - start:.3f} seconds")


asyncio.run(async_streaming_results())


# Producer–Consumer using Queues (Your Mini-Kafka)
import random

queue = asyncio.Queue()


# Producer coroutine
async def producer(name: str, count: int):
    for i in range(count):
        await asyncio.sleep(random.uniform(0.1, 0.5))  # random delay
        item = f"{name}-{i}"
        await queue.put(item)
        logger.info(f"{name} produced: {item}")


# Consumer coroutine
async def consumer(name: str):
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break  # Exit on sentinel
        logger.info(f"{name} consumed: {item}")
        await asyncio.sleep(random.uniform(0.2, 0.4))  # Simulate processing
        queue.task_done()


# simulate
async def simulator():
    num_producers = 2
    num_consumers = 3
    items_per_producer = 5

    producers = [
        asyncio.create_task(producer(f"Producer-{i + 1}", items_per_producer))
        for i in range(num_producers)
    ]
    consumers = [
        asyncio.create_task(consumer(f"Consumer-{i + 1}")) for i in range(num_consumers)
    ]

    # Wait for all producers to finish
    await asyncio.gather(*producers)
    # Signal consumers to exit
    for _ in range(num_consumers):
        await queue.put(None)
    # Wait for all consumers to finish
    await asyncio.gather(*consumers)
    # Wait for the queue to be fully processed
    await queue.join()


asyncio.run(simulator())
logger.info("All done!!")


# # Concurrency vs Parallelism


from multiprocessing import freeze_support, Pool


def some_task(*args):
    logging.info("Doing some CPU-bound task...")
    sleep(2)
    logging.info("Task complete!")
    return args[0] if args else "ok"


def run_in_process():
    start = perf_counter()
    with Pool(processes=2) as pool:
        results = pool.map(some_task, range(4))
    logging.info(f"Results: {results}")

    logger.info(f"Time taken to run in process: {perf_counter() - start:.3f} seconds")


async def run_in_async():
    start = perf_counter()
    tasks = [asyncio.to_thread(some_task) for _ in range(4)]
    results = await asyncio.gather(*tasks)
    logging.info(f"Results: {results}")

    logger.info(f"Time taken to run in async: {perf_counter() - start:.3f} seconds")


if __name__ == "__main__":
    freeze_support()

    run_in_process()

    asyncio.run(run_in_async())
