from time import perf_counter


def timeit(func):
    async def wrapper():
        start = round(perf_counter(), 2)
        await func()
        print(f"Execution time: {round(perf_counter(), 2) - start} sec.")
    return wrapper
