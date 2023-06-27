import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class ObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance')
        self.publisher_ = self.create_publisher(Twist, '/car/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(LaserScan, '/car/scan', self.scan_callback, 10)
        
    def scan_callback(self, msg):
        min = 10.0
        
        for i in range(0, 200):
            if(msg.ranges[i] < min):
                min = msg.ranges[i]
            
        vel = self.calculate_cmd_vel(min)
        self.publisher_.publish(vel)
    
    def calculate_cmd_vel(self, distance):
        vel = Twist()
        print(f"Closest distance: {distance}")
        
        if(distance < 4.8):
            vel.linear.x = 0.8
            vel.angular.z = 0.9
        else:
            vel.linear.x = 1.0
            vel.angular.z = 0.0
            
        return vel

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidance()
    
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
