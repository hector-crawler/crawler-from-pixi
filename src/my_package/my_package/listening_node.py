import rclpy
import RPi.GPIO as GPIO
from rclpy.node import Node
from std_msgs.msg import Empty


class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__("minimal_subscriber")

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(16, GPIO.OUT)

        queue_length = 5
        self.subscription = self.create_subscription(
            Empty, "led_blinker", self.listener_callback, queue_length
        )

    def listener_callback(self, msg):
        GPIO.output(16, not GPIO.input(16))
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
    GPIO.cleanup()


if __name__ == "__main__":
    main()
