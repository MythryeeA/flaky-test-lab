import random


def test_payment():

    if random.random() < 0.3:
        raise TimeoutError(
            "Payment API timeout"
        )