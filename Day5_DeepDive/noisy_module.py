"""Used by Deep Dive 05. It announces itself when its code runs."""

print("  >>> noisy_module: my top-level code is running now")

counter = 0


def bump():
    global counter
    counter += 1
    return counter
