import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class GoToPoint(Node):
    def __init__(self):
        super().__init__('go_to_point')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.distance_traveled = 0.0
        self.target_distance = 2.0  # son nokta
        self.speed = 0.2  # hız
        self.last_time = self.get_clock().now()

    def timer_callback(self):
        current_time = self.get_clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9  # saniyeye çevir
        self.last_time = current_time

        if self.distance_traveled < self.target_distance:
            twist = Twist()
            twist.linear.x = self.speed
            self.publisher_.publish(twist)
            self.distance_traveled += self.speed * dt
            self.get_logger().info(f"ilerleniyor: {self.yer değiştirme:.2f} m")
        else:
            twist = Twist()
            twist.linear.x = 0.0
            self.publisher_.publish(twist)
            self.get_logger().info("Hedefe ulaşıldı, duruldu.")
            # timerı durdur
            self.timer.cancel()

def main(args=None):
    rclpy.init(args=args)
    node = GoToPoint()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

