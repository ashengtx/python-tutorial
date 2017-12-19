import os
import time

# Create a directory "test"
if not os.path.isdir("test"):
    os.mkdir("test")

time.sleep(5)

# remove directory
os.rmdir("test")
