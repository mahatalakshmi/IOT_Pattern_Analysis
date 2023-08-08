#include <Wire.h>
#include <MPU9250_asukiaaa.h>

#define MPU1_ADDRESS 0x68
#define MPU2_ADDRESS 0x69
#define MPU3_ADDRESS 0x6A

MPU9250_asukiaaa mpu1;
MPU9250_asukiaaa mpu2;
MPU9250_asukiaaa mpu3;

void setup() {
  Wire.begin();
  Serial.begin(115200);
  delay(1000);
  
  mpu1.beginAccel();
  mpu1.beginGyro();
  mpu2.beginAccel();
  mpu2.beginGyro();
  mpu3.beginAccel();
  mpu3.beginGyro();
  
  setMPU9250Address(MPU1_ADDRESS, MPU1_ADDRESS);
  setMPU9250Address(MPU2_ADDRESS, MPU2_ADDRESS);
  setMPU9250Address(MPU3_ADDRESS, MPU3_ADDRESS);
}

void loop() {
  mpu1.accelUpdate();
  mpu1.gyroUpdate();

  float ax1 = mpu1.accelX();
  float ay1 = mpu1.accelY();
  float az1 = mpu1.accelZ();
  float gx1 = mpu1.gyroX();
  float gy1 = mpu1.gyroY();
  float gz1 = mpu1.gyroZ();

  mpu2.accelUpdate();
  mpu2.gyroUpdate();

  float ax2 = mpu2.accelX();
  float ay2 = mpu2.accelY();
  float az2 = mpu2.accelZ();
  float gx2 = mpu2.gyroX();
  float gy2 = mpu2.gyroY();
  float gz2 = mpu2.gyroZ();

  mpu3.accelUpdate();
  mpu3.gyroUpdate();

  float ax3 = mpu3.accelX();
  float ay3 = mpu3.accelY();
  float az3 = mpu3.accelZ();
  float gx3 = mpu3.gyroX();
  float gy3 = mpu3.gyroY();
  float gz3 = mpu3.gyroZ();

  Serial.print(ax1);
  Serial.print(", ");
  Serial.print(ay1);
  Serial.print(", ");
  Serial.print(az1);
  Serial.print(", ");
  Serial.print(gx1);
  Serial.print(", ");
  Serial.print(gy1);
  Serial.print(", ");1
  Serial.print(gz1);
  Serial.print(", ");
  Serial.print(ax2);
  Serial.print(", ");
  Serial.print(ay2);
  Serial.print(", ");
  Serial.print(az2);
  Serial.print(", ");
  Serial.print(gx2);
  Serial.print(", ");
  Serial.print(gy2);
  Serial.print(", ");
  Serial.print(gz2);
  Serial.print(", ");
  Serial.print(ax3);
  Serial.print(", ");
  Serial.print(ay3);
  Serial.print(", ");
  Serial.print(az3);
  Serial.print(", ");
  Serial.print(gx3);
  Serial.print(", ");
  Serial.print(gy3);
  Serial.print(", ");
  Serial.println(gz3);

  delay(1000);
}


void setMPU9250Address(uint8_t defaultAddress, uint8_t newAddress) {
  Wire.beginTransmission(defaultAddress);
  Wire.write(0x6B);
  Wire.write(0x80);
  Wire.endTransmission();

  delay(100);

  Wire.beginTransmission(defaultAddress);
  Wire.write(0x37);
  Wire.write(newAddress);
  Wire.endTransmission();

  Serial.print("MPU9250 sensor at address 0x");
  Serial.print(defaultAddress, HEX);
  Serial.print(" set to address 0x");
  Serial.println(newAddress, HEX);
}
