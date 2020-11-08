#include <SPI.h>
#include <SD.h>
#include <Keyboard.h>

const int pulsante = 8;
const int sd = 10;
int ultimoStatoPulsante;
int statoPulsanteAttuale;
File myFile;
char lettura;

void setup() {
  Serial.begin(9600);
  //while(!Serial){;}
  
  pinMode(pulsante, INPUT);
  statoPulsanteAttuale = digitalRead(pulsante);
  SD.begin(sd);
  
  myFile = SD.open("happy.txt", FILE_READ);
  if(myFile){
    delay(1000);
    /*Apertura Bash e avvio di NANO*/
    Keyboard.press(KEY_LEFT_CTRL);
    Keyboard.press(KEY_LEFT_ALT);
    Keyboard.write('t');
    Keyboard.releaseAll(); 
    delay(2000);
    Keyboard.print("setxkbmap us");
    Keyboard.write(KEY_RETURN);
    delay(1000);
    Keyboard.print("rm hap.py");
    Keyboard.write(KEY_RETURN);
    delay(1000);
    Keyboard.print("nano");
    Keyboard.write(KEY_RETURN); 
    
    /*Scrittura a NANO*/
    while(myFile.available()){
      lettura = myFile.read();
      Keyboard.write(lettura);
    }
    myFile.close();
    
    /*Salvataggio file*/
    Keyboard.press(KEY_LEFT_CTRL);
    Keyboard.write('o');
    Keyboard.releaseAll();
    Keyboard.print("hap.py");
    Keyboard.write(KEY_RETURN);
    Keyboard.press(KEY_LEFT_CTRL);
    Keyboard.write('x');
    Keyboard.releaseAll(); 
    delay(500);
    /*RUN FILE DA COMMAND*/
    Keyboard.print("python3 hap.py");
    Keyboard.write(KEY_RETURN);
    /*Keyboard.print("setxkbmap it");
    Keyboard.write(KEY_RETURN);*/
  }
  else{
    Serial.println("Errore");
    myFile.close();
  }

}

void loop() {
}