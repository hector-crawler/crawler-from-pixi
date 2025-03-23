from my_package import device_consts
import rospy2
from luma.core.render import canvas
from std_msgs.msg import String


def monitor_callback(data):
    with canvas(device_consts.device) as draw:
        draw.rectangle(device_consts.device.bounding_box, outline="white", fill="black")
        draw.text((10, 10), data.data, font=device_consts.oled_font, fill="white")


def main():
    print("Hi from my_package.")
    rospy2.init_node("Monitor_node")
    rospy2.Subscriber("monitor_message", String, monitor_callback)
    rospy2.spin()


if __name__ == "__main__":
    main()
