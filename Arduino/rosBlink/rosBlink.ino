/*
   rosserial Subscriber Example
   turn an LED on/off callback

"""  alias python='/usr/bin/python2.7'  """
   on terminal#1: roscore
   on terminal#2: rosrun rosserial_python serial_node.py /dev/ttyUSB0

   // send message to the arduino via topic "setLED"
   on terminal#3: rostopic pub setLED std_msgs/Empty --once ..or
                  rostopic pub setLED std_msgs/UInt8 0 --once ..or
                  python talker.py 1, python talker.py 0

   // to see what's arduino published
   rostopic echo chatter ..or
   python listener.py
*/


#include <ros.h>
#include <std_msgs/Empty.h> // no parameter message
#include <std_msgs/UInt8.h> // also UInt16.h, 
#include <std_msgs/String.h>

std_msgs::String str_msg;
std_msgs::UInt8 int_msg;

ros::NodeHandle  nh;

ros::Publisher pub("ArduinoMsg", &int_msg);

void messageCb( const std_msgs::UInt8& msg) {
  
  // set the led state
  if (msg.data == 1) {
    digitalWrite(13, HIGH);
    int val = analogRead(0);
    delay(10);
    val = 1;
    int_msg.data = val;
    pub.publish( &int_msg );
    
    //str_msg.data = "led is on";
    //pub.publish( &str_msg );
    
  }
  
  if (msg.data == 0) {
    digitalWrite(13, LOW);
    int val = 0;
    int_msg.data = val;
    pub.publish( &int_msg );
    
    //str_msg.data = "led is off";
    //pub.publish( &str_msg );
  }
}

ros::Subscriber<std_msgs::UInt8> sub("setLed", &messageCb );

void setup()
{
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(pub);
}

void loop()
{
  nh.spinOnce();
  delay(1); // 1
}

