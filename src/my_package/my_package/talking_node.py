import rclpy
from rclpy.node import Node
from std_msgs.msg import Empty


class MinimalPublisher(Node):
    def __init__(self):
        super().__init__("minimal_publisher")
        queue_length = 5
        self.publisher = self.create_publisher(Empty, "led_blinker", queue_length)
        interval_seconds = 0.5
        self.timer = self.create_timer(interval_seconds, self.timer_callback)

    def timer_callback(self):
        msg = Empty()
        self.publisher.publish(msg)
        self.get_logger().info("Sent a signal")


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
