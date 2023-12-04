import time

from icecream import ic


def read_file(file: str) -> list:
    with open(file, "r", encoding="utf-8") as f:
        input_data = f.readlines()
    return [i.strip() for i in input_data]


def timer(part=0, day=0, year=0):
    title = ""
    if year:
        title += "%s." % year
    if day:
        title += "%s " % day
    if part:
        title += "Part %s: " % part

    def decorator(func):
        def wrapper(*a, **kw):
            start = time.perf_counter()
            result = func(*a, **kw)
            duration = (time.perf_counter() - start) * 1000
            timer = f"{title}({duration:.7f} ms)"
            ic(timer)
            return result

        return wrapper

    return decorator
