t = int(input())

for _ in range(t):
    sound = input().split()

    while True:
        animal = input().split()

        if animal[0] == "what":
            print(" ".join(sound))
            break
        while animal[2] in sound:
            sound.remove(animal[2])