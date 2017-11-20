// 电子秤ADC（HX771AD）对应的引脚号
const int VT  = 11;
const int WSCK = 12;

const int temp1=A3;//杯温
const int temp2=A4;//水温
int delaytime=1000;

// 称重函数
long weigh(void){
  long data = 0;   // 压力传感器ADC数值
  int i;          // 循环计数器
  digitalWrite(WSCK, LOW);   // 拉低时钟，准备读取ADC
  while(digitalRead(VT));   // 等待数据恢复低电平（防止ADC忙）
  // 逐为读取ADC数据（从高位到低位）
  for(i = 0; i < 24; i++){
    data <<= 1;
    digitalWrite(WSCK, HIGH);
    data += digitalRead(VT);
    digitalWrite(WSCK, LOW); 
  }
  // 结束脉冲的个数将决定下一个数据的采样通道和增益
  // ....一个结束脉冲——通道A，增益128
  // ....两个结束脉冲——通道B，增益64
  // ....三个结束脉冲——通道A，增益64
  for(i = 0; i < 3; i++){   // 通道A，增益64
    digitalWrite(WSCK, HIGH);
    digitalWrite(WSCK, LOW); 
  }
  
  return data;
}

long getweigh(){
  return (16739000-weigh())*50/10000;
}

int gettemp(int io){
  return analogRead(io)*330/1023;
}

void setup() {
  pinMode(VT,  INPUT);
  pinMode(WSCK, OUTPUT);
  // 串口初始化，波特率9600
  Serial.begin(9600);
}

void loop() {
  Serial.print("weight:");
  Serial.print(getweigh());
  Serial.print(" ");
  Serial.print("temp1:");
  Serial.print(gettemp(temp1));
  Serial.print(" ");
  Serial.print("temp2:");
  Serial.print(gettemp(temp2));
  Serial.print("\n");
  delay(delaytime);
}
