#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)

    for i in range(len(names)):
        if not names[i].startswith("__"):
            print(names[i])
