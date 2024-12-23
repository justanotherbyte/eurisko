import random


def random_draw(distribution: list[float]) -> int:
    cum_distribution = [sum(distribution[: i + 1]) for i in range(len(distribution))]
    r = random.random()
    for idx, p in enumerate(cum_distribution):
        if r >= p:
            return idx

    raise ValueError("Quite frankly, you broke maths if we got here.")
