import time
import datetime
import logging
from miio.philips_bulb import PhilipsBulb
from config import configs




def get_lights():
    lights = []
    for l_config in configs["lights"]:
        ip = l_config["ip"]
        token = l_config['token']
        light = PhilipsBulb(ip=ip, token=token, lazy_discover=False)
        lights.append(light)
    return lights


def wakeup_entity():
    wakeup_action = configs["wake_up_action"]
    if wakeup_action["mode"] == "linear":
        linear_wakeup(wakeup_action)
    else:
        raise ValueError("Unsupported mode: %s".format(wakeup_action["mode"]))

def linear_wakeup(config=None):
    logging.debug("linear mode.")
    if config is None:
        config = {}
    lights = get_lights()
    wake_up_duration = config["duration"]
    for i in range(1, 101):
        for light in lights:
            light.on()
            light.set_brightness_and_color_temperature(i, i)
            logging.debug("set light %s's brightness and cct to %d", light.ip, i)
        time.sleep(wake_up_duration / 100)

def schedule_next_wakeup():
    time.time()


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    # lights = get_lights()
    # for light in lights:
    #     light.off()
    #     light.set_brightness_and_color_temperature(100, 1)
    # # wakeup_entity()
    # exit(0)
    t = time.strptime("03:00", "%H:%M")

    print(time.localtime())
    print(t)

    print(time.localtime())
    print(time.gmtime())
    d1 = datetime.datetime.now()
    print(d1)
    # while time.ctime()
    while time.time() <= 1528153200 + 24 * 60 * 60:
        time.sleep(10)
    wakeup_entity()
