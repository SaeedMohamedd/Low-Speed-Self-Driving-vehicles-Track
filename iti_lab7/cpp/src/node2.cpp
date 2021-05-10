#include <chrono>
#include"string.h"
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class Node2 : public rclcpp::Node
{
public:
    Node2():Node("string_subscriber")
    {
        //string_publisher_ = this->create_publisher<std_msgs::msg::String>("int_fb",10);
        string_subscriber_ = this->create_subscription<std_msgs::msg::String>("str_topic",rclcpp::SensorDataQoS(), std::bind(&Node2::timer_cb, this, std::placeholders::_1));
        
    }
private:
    void timer_cb(const std_msgs::msg::String::SharedPtr msg)const
    {
        std_msgs::msg::String string_msg = std_msgs::msg::String();
        std::string s =msg->data.c_str();
        RCLCPP_INFO(this->get_logger(),s);
        /*
        std::string delimiter = ":";
        size_t pos = 0;
        std::string token;
        while ((pos = s.find(delimiter)) != std::string::npos) {
        token = s.substr(0, pos);
        s.erase(0, pos + delimiter.length());
        RCLCPP_INFO(this->get_logger(),s);
         string_msg.data = s ;
        string_publisher_->publish(string_msg);
}
    */
    }
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr string_subscriber_;
   // rclcpp::Publisher<std_msgs::msg::String>::SharedPtr string_publisher_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc,argv);
    rclcpp::spin(std::make_shared<Node2>());
    rclcpp::shutdown();
    return 0;
}