#!/usr/bin/env python
import asyncio

from src.basic import concurrency

if __name__ == "__main__":
    asyncio.run(concurrency.concurrent_coroutine_task_group())
