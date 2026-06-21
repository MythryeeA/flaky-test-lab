import time

def test_payment():

    current_second = int(time.time())

    if current_second % 2 == 0:
        raise TimeoutError(
            "Payment API timeout"
        )