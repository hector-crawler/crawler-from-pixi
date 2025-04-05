import rclpy
from rclpy.node import Node
from std_msgs.msg import Empty

from machine import Pin


class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__("minimal_subscriber")
        self.led = Pin(25, Pin.OUT)
        queue_length = 5
        self.subscription = self.create_subscription(
            Empty, "led_blinker", self.listener_callback, queue_length
        )

    def listener_callback(self, msg):
        self.led.Toggle()
        self.get_logger().info("Got signal")


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
