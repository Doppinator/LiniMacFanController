from fan import Fan
from smc import SMC
from controller import Controller


def main():

    smc = SMC()
    fans = [Fan(number, smc) for number in smc.fan_numbers()]
    controller = Controller()

    print("Fan control curve:")
    for temperature, rpm in controller.curve:
        print(f"  {temperature}°C -> {rpm} RPM")
        
    if fans:
        for fan in fans:
            print(fan)
    else:
        print("No fans were reported by the Apple SMC driver.")

if __name__ == "__main__":
    main()
