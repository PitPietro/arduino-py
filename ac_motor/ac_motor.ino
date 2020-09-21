// https://www.instructables.com/id/Python-pySerial-Arduino-DC-Motor

#include <DC_Motor.h>
 
DC_Motor motor(7,6);
 
void setup() 
{
  
}
 
void loop() 
{
  motor.forward();
  delay(5000);
  motor.stop_motor();
  delay(2000);
  motor.reverse();
  delay(5000);
  motor.stop_motor();
  delay(2000);
}
