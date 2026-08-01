from fan import Fan


def main():

    fans = [
        Fan(1),
        Fan(2),
        Fan(3)
    ]

    print()

    for fan in fans:
        print(fan)

    print()


if __name__ == "__main__":
    main()