# 📌 Function Caching using functools

# ✅ What is Caching?
# Caching stores results of expensive function calls to avoid recomputation. 
# The `lru_cache` decorator is a simple way to implement caching in Python.

from functools import lru_cache

# Apply the cache decorator to the function
@lru_cache(maxsize=10)
def slow_function(n):
    print("Computing...")  # Simulate a slow function
    return n * n

# Call the function with the same argument twice
print(slow_function(5))  # Computes and caches the result
print(slow_function(5))  # Retrieved from cache

# Output:
# Computing...
# 25
# 25  (cached result, no computation)
