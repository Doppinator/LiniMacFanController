from fan import Fan
from smc import SMC


def main():

    smc = SMC()
    fans = [Fan(number, smc) for number in smc.fan_numbers()]

    print()

    if fans:
        for fan in fans:
            print(fan)
    else:
        print("No fans were reported by the Apple SMC driver.")

    print()


if __name__ == "__main__":
    main()
