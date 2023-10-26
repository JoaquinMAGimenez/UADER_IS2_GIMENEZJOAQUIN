/*
  Custom LED Blink Pattern

  Implementa un patrón de parpadeo personalizado para el LED incorporado en Arduino.

  Esta versión del código realiza las siguientes acciones:
  a. Encender el LED por 400 mSeg y apagarlo por un tiempo similar. Repetir tres veces.
  b. Mantener el LED apagado por 1200 mSeg.
  c. Encender el LED por 1200 mSeg y apagarlo por un tiempo similar. Repetir tres veces.
  d. Mantener el LED apagado por 1200 mSeg.
  e. Encender el LED por 400 mSeg y apagarlo por un tiempo similar. Repetir tres veces.
  f. Mantener el LED apagado por 3600 mSeg.
  g. Volver a repetir el ciclo.

  Este código está en el dominio público.
*/

// El pin LED_BUILTIN es el pin incorporado para el LED en la mayoría de las placas Arduino.
int ledPin = LED_BUILTIN;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  while (true) {
    // a. Encender el LED por 400 mSeg y apagarlo por un tiempo similar. Repetir tres veces.
    for (int i = 0; i < 3; i++) {
      digitalWrite(ledPin, HIGH);  // Encender el LED
      delay(400);  // Esperar 400 mSeg
      digitalWrite(ledPin, LOW);  // Apagar el LED
      delay(400);  // Esperar 400 mSeg
    }

    // b. Mantener el LED apagado por 1200 mSeg.
    delay(1200);

    // c. Encender el LED por 1200 mSeg y apagarlo por un tiempo similar. Repetir tres veces.
    for (int i = 0; i < 3; i++) {
      digitalWrite(ledPin, HIGH);  // Encender el LED
      delay(1200);  // Esperar 1200 mSeg
      digitalWrite(ledPin, LOW);  // Apagar el LED
      delay(1200);  // Esperar 1200 mSeg
    }

    // d. Mantener el LED apagado por 1200 mSeg.
    delay(1200);

    // e. Encender el LED por 400 mSeg y apagarlo por un tiempo similar. Repetir tres veces.
    for (int i = 0; i < 3; i++) {
      digitalWrite(ledPin, HIGH);  // Encender el LED
      delay(400);  // Esperar 400 mSeg
      digitalWrite(ledPin, LOW);  // Apagar el LED
      delay(400);  // Esperar 400 mSeg
    }

    // f. Mantener el LED apagado por 3600 mSeg.
    delay(3600);
  }
}
