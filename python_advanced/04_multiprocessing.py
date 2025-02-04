# 📌 Multiprocessing in Python

# ✅ What is Multiprocessing?
# Multiprocessing allows Python programs to run multiple processes concurrently.
# It is useful for CPU-bound tasks, where you want to take advantage of multiple CPU cores.

import multiprocessing

# Define a function to be executed by a separate process
def worker():
    print("Worker Process Running")

# Create a process that will execute the `worker` function
process = multiprocessing.Process(target=worker)

# Start the process
process.start()

# Wait for the process to finish
process.join()

# Output:
# Worker Process Running (printed by the worker process)
