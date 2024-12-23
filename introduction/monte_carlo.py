import random


def sim_probability(num_heads: int, num_flips: int) -> float:
    success = 0
    trials = 1000
    for _ in range(trials):
        heads = 0
        for __ in range(num_flips):
            heads += 1 if random.random() < 0.5 else 0

        if heads == num_heads:
            success += 1

    return success / trials


print(sim_probability(1, 2))
K = 100
print(sum(sim_probability(n, K) for n in range(K)))  # sanity check
