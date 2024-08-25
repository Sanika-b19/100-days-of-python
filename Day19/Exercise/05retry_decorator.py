# Exercise 5: Retry a Function with Limited Attempts

import time

def retry(attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying due to: {e}")
                    time.sleep(1)
            raise Exception("Function failed after maximum retry attempts.")
        return wrapper
    return decorator

@retry(attempts=3)
def unreliable_function():
    raise ValueError("Random error")

try:
    unreliable_function()
except Exception as e:
    print(e) 
