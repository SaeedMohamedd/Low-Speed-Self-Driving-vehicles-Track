#!/usr/bin/env python3
import rclpy
import csv
from rclpy.node import Node

#TODO Import needed messages
from sensor_msgs.msg import NavSatFix


class my_node (Node):
    def __init__(self):
        super().__init__("Node_name") 
        self.csv_file_path = "GGA_GST.csv"
        self.lines = []
        with open(self.csv_file_path, newline='\n') as csvfile:       
          self.readCSV = csv.reader(csvfile, delimiter = ',')
          for row in self.readCSV:
              self.lines.append(row)

        self.count = 1 #Skip header
        
        #TODO create timer_call with the required frequency & publisher
        self.create_timer(1/5,self.timer_call)
        self.obj_pub=self.create_publisher(NavSatFix,"fix",10)

    def timer_call(self):
        row = self.lines[self.count]
        self.count +=1
        if (self.count >= len(self.lines)): # repeat csv file continously
            self.count = 0

        #TODO get The following values from csv
        row=self.lines[self.count]
        latitude_value =row[2]
        
        latitude_direction = row[3]
        
        longitude_value = row[4]
        longitude_direction =row[5]

        altitude_value = row[8]

        # The following functions convert the string data in degrees/minutes to float data in degrees as ROS message requires.        
        latitude = self.convert_latitude(latitude_value, latitude_direction)
        longitude = self.convert_longitude(longitude_value, longitude_direction)
        altitude = self.safe_float(altitude_value)
        
        hdop = float(row[7])
        lat_std_dev = float(row[21])
        lon_std_dev = float(row[22])
        alt_std_dev = float(row[23])

        #TODO Fill the gps message and publish
        msg=NavSatFix()
        msg.latitude=float(latitude)
        msg.longitude=float(longitude)
        msg.altitude=float(altitude)
        msg.position_covariance[0] = (hdop * lon_std_dev) ** 2
        msg.position_covariance[4] = (hdop * lat_std_dev) ** 2
        msg.position_covariance[8] = (2 * hdop * alt_std_dev) ** 2
        self.obj_pub.publish(msg)




    def convert_latitude(self, field_lat, lat_direction):
        latitude = self.safe_float(field_lat[0:2]) + self.safe_float(field_lat[2:]) / 60.0
        if lat_direction == 'S':
            latitude = -latitude
        return latitude

    def convert_longitude(self, field_long, long_direction):
        longitude = self.safe_float(field_long[0:2]) + self.safe_float(field_long[2:]) / 60.0 
        if long_direction == 'W':
            longitude = -longitude
        return longitude

    def safe_float(self, field):
        try:
            return float(field)
        except ValueError:
            return float('NaN')
        
def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__=="__main__":
    main()
