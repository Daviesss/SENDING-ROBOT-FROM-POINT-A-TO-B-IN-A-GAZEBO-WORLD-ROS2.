import rclpy
from geometry_msgs.msg import Twist  #using the Twist message type
from rclpy.node import Node
from nav_msgs.msg import Odometry    #using the odometry message type
from sensor_msgs.msg import LaserScan #using the Laserscan message type

class move(Node): #A class which contains various methods 
    def __init__(self):
        super().__init__("publisherr")
        self.publisher = self.create_publisher(Twist,'/cmd_vel',10)
        # self.odom_publisher = self.create_publisher(Odometry,'/odom',10)
        # self.speed = speed
        # speed = 0.2
        time_count = 0.5
        self.time_counter = self.create_timer(time_count,self.velocity_command)
        # self.time_counter = self.create_timer(time_count,self.odom_command)
        ###############################################
        self.subscribe = self.create_subscription(Odometry,'/odom',self.odom_callback,10)
        self.laser_subscriber = self.create_subscription(LaserScan,'/scan',self.laser_callback,10)

    # def odom_command(self):
    #     velocity_odometry = Odometry()
    #     self.odom_publisher.publish(velocity_odometry)
    #     if velocity_odometry.twist.twist.angular.z > 0.10: 
    #         velocity_command = Twist()
    #         velocity_command.linear.x = 0.1
    #         self.publisher.publish(velocity_command)


    #defining the method for publiching to velocity message
    def velocity_command(self):
        velocity_command = Twist()
        velocity_command.linear.x = 0.1
        self.publisher.publish(velocity_command)
        #return velocity_command


    #Subscribing to Odometry message to know the position and also the orientation of the robot in 2D space
    def odom_callback(self,data):
        self.get_logger().info('I heard:" %s "' % str(data.pose.pose.position.x))
        self.get_logger().info('I heard:" %s "' % str(data.pose.pose.orientation.x))
        self.get_logger().info('I heard:" %s "' % str(data.pose.pose.orientation.y))
        self.get_logger().info('I heard:" %s "' % str(data.pose.pose.orientation.z))
        self.get_logger().info('I heard:" %s "' % str(data.pose.pose.orientation.w))
        self.get_logger().info('I heard:" %s "' % str(data.twist.twist.angular.z))

       
        
        
        if  data.pose.pose.position.x > 0.90:    #position of x (once the position of the robot is 0.9m the robot will turn at a radians of 0.1)
            velocity_command = Twist()
            velocity_command.angular.z = 0.2
            self.publisher.publish(velocity_command)
        
  
       
        if data.pose.pose.orientation.z > 0.70:
            #getting the orientation of angle z
            velocity_command = Twist()
            velocity_command.linear.x = 0.1 
            self.publisher.publish(velocity_command)

        if data.pose.pose.position.y > 0.60:
            velocity_command = Twist()
            velocity_command.angular.z = 0.2
            self.publisher.publish(velocity_command)

        if data.pose.pose.orientation.z > 0.999:  #0.9952
            velocity_command = Twist()
            velocity_command.linear.x = 0.2
            self.publisher.publish(velocity_command)

        if data.pose.pose.position.x < -2.0:
            velocity_command = Twist()
            velocity_command.linear.x = 0.0
            self.publisher.publish(velocity_command)
            # self.get_logger().info('"The Robot stopped at a distance of: "' % str(data.pose.pose.position.x))
            print("The Robot has stopped: GOAL REACHED")
            # velocity_movement.destroy_node()
            # rclpy.shutdown(velocity_command)
            
            


        
        


    def laser_callback(self,data):
        self.get_logger().info('I heard:" %s "' % (data.ranges))
        self.get_logger().info('I heard:" %s "' % str(data.angle_min))
        self.get_logger().info('I heard:" %s "' % str(data.angle_max))
        self.get_logger().info('I heard:" %s "' % str(data.angle_increment))

        velocity_command = Twist()
        velocity_command.linear.x = 0.1
        self.publisher.publish(velocity_command)


        # if len(data.ranges) > 1.4:
        #     velocity_command = Twist()
        #     velocity_command.linear.x = 0.2
        #     self.publisher.publish(velocity_command)

#main function that calls the class       
def main(args = None):
    rclpy.init(args = args)
    velocity_movement = move()
    rclpy.spin(velocity_movement)

    # velocity_movement.destroy_node()
    rclpy.shutdown(velocity_movement)


if __name__ == '__main__':
    main()




        


