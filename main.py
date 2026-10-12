import random

secret = random.randint(1, 10)
guess = int(input("Угадай число от 1 до 10: "))

if guess == secret:
    print("🎉 Супер! Ты угадал!")
else:
    print(f"Не угадал, это было число {secret}")