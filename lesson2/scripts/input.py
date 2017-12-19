import random
name = input("Hello, may I know your name?:")
reply = ["Wow, %s, such a beautiful name!", "%s, It's so lovely!", "Nice to meet you! %s!"]
print(random.choice(reply) % name)
