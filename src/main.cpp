#include <Arduino.h>
#include <Keyboard.h>
#include <SPI.h>
#include <SD.h>

//String baseNomeFile = "file";
//File myFile = SD.open(baseNomeFile);
int fileC = 0;
const int pulsante = 8;
int ultimoStatoPulsante;
int statoPulsanteAttuale;
const int chipSelect = 10;
char carattere;

String baseNomeFile = "file.txt";
File myFile = SD.open(baseNomeFile, FILE_WRITE);

void setup() {
  // put your setup code here, to run once:
  pinMode(chipSelect, OUTPUT);
  pinMode(pulsante, INPUT);

  Serial.begin(115200);

  if(!SD.begin(chipSelect)){
    Serial.println("Sei un fallimento");
    return;
  }

  //statoPulsanteAttuale = digitalRead(pulsante);
  Keyboard.begin();

  myFile.print("Hello World!");
  myFile.close();

}

void loop(){
  
  // put your main code here, to run repeatedly:
  // ultimoStatoPulsante = statoPulsanteAttuale;
  // statoPulsanteAttuale = digitalRead(pulsante);

  // if(ultimoStatoPulsante == HIGH && statoPulsanteAttuale == LOW){

  //   Keyboard.press(KEY_LEFT_CTRL);
  //   delay(50);
  //   Keyboard.press(KEY_LEFT_ALT);
  //   delay(50);
  //   Keyboard.write('t');
  //   delay(1000);
  //   Keyboard.releaseAll();
  //Serial.println(Serial.read());
  // }

  // if(Serial.read()) {
  // baseNomeFile = baseNomeFile.concat(fileC);
  // baseNomeFile = baseNomeFile.concat(".txt");
  // myFile.close();
  // myFile = SD.open(baseNomeFile, FILE_WRITE);
  // fileC++;
  // //delay(100);
  // }




  // while(carattere = Serial.read() == true){
  //   myFile.write(carattere);
  //   //Keyboard.write(carattere);
  // }
  // myFile.close();

}