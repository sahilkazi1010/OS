import threading
import random
import time

buffer_size = 5
buffer = [0] * buffer_size

produce_pos = 0
consume_pos = 0
items = 0

lock = threading.Lock()

buffer_full = threading.Condition(lock)
buffer_empty = threading.Condition(lock)


def producer():

    global produce_pos, items

    while True:

        item = random.randint(1, 99)

        with buffer_full:

            while items == buffer_size:
                buffer_full.wait()

            buffer[produce_pos] = item

            print(f"Produced: {item} at {produce_pos}")

            produce_pos = (produce_pos + 1) % buffer_size
            items += 1

            buffer_empty.notify()

        time.sleep(1)


def consumer():

    global consume_pos, items

    while True:

        with buffer_empty:

            while items == 0:
                buffer_empty.wait()

            item = buffer[consume_pos]

            print(f"Consumed: {item} at {consume_pos}")

            consume_pos = (consume_pos + 1) % buffer_size
            items -= 1

            buffer_full.notify()

        time.sleep(1)


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()