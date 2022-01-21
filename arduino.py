int valor = 0;

void setup(){
    pinMode(A1, INPUT);
    pinMode(A2, INPUT);
    pinMode(A3, INPUT);
    pinMode(A4, INPUT);
    pinMode(A5, INPUT);
    pinMode(13, OUTPUT);
}

void loop(){
    if(digitalRead(A1) == 0){valor = 1;}
    if(digitalRead(A2) == 0){valor = 2;}
    if(digitalRead(A3) == 0){valor = 3;}
    if(digitalRead(A4) == 0){valor = 4;}
    if(digitalRead(A5) == 0){valor = 5;}
    if(digitalRead(A1) || digitalRead(A2) || digitalRead(A3) || digitalRead(A4) || digitalRead(A5)) { valor = 0; }

    if(valor != 0){
        digitalWrite(13, HIGH);
    }else{
        digitalWrite(13, LOW);
    }
}