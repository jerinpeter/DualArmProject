import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectoryPoint, JointTrajectory

class JointTrajectoryPublisher(Node):

    def __init__(self):
        super().__init__('joint_trajectory_publisher')
        self.publisher_ = self.create_publisher(JointTrajectory, '/joint_trajectory_controller/joint_trajectory', 10)
        self.home_position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    def publish_trajectory(self):
        joint_trajectory = JointTrajectory()
        joint_trajectory.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6"]

        # Define the trajectory point
        point = JointTrajectoryPoint()
        point.positions = [-0.01941018328893307, -2.2151417609529522, -2.5953482202942237, 1.5945826163870482, 2.6972900320808217, -1.5264275304019579]
        point.time_from_start.sec = 10  # Time to reach the point

        joint_trajectory.points.append(point)

        self.publisher_.publish(joint_trajectory)

    def go_to_home(self):
        # Implement logic to send commands to reach the home position (self.home_position)
        # This might involve sending individual joint commands or using another ROS 2 service
        print(f"Moving to home position: {self.home_position}")
        # Replace the print statement with your actual implementation

    def run(self):
        self.publish_trajectory()
        # Wait for some time before going to home
        rclpy.spin_once(self)
        rclpy.sleep(1.0)  # Adjust sleep time as needed
        self.go_to_home()

def main():
    rclpy.init()
    node = JointTrajectoryPublisher()
    node.run()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
