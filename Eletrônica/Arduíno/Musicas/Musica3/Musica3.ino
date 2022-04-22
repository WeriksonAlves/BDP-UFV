#include "pitches.h"

int const piezoPin = 8;

int bpm = 100;
int bps = bpm / 60;
int fullNoteMs = 1000 / bps;
int halfNoteMs = fullNoteMs / 2;
int quarterNoteMs = halfNoteMs / 2;
int eighthNoteMs = quarterNoteMs / 2;

int note = 0;
int duration = 0;

void setup() {
  Serial.begin(9600); 
}

//The Simpson's main theme plays: C-E-F#-A-G-E-C-G-F#-F#-F#-G
//The tune rises for the first 4 notes, then from the G goes down to the G an octave lower. Three fast F#'s and back to the G.
int simpsons[] = {HALF, NOTE_C4, QUARTER, NOTE_E4, NOTE_FS4, EIGHTH, NOTE_A4, HALF, NOTE_G4, QUARTER, NOTE_E4, NOTE_C4, NOTE_G3, EIGHTH, NOTE_FS3, NOTE_FS3, NOTE_FS3, QUARTER, NOTE_G3};
int numNotes = sizeof(simpsons)/sizeof(int);

void loop() {
  if (note < numNotes) {
    if (simpsons[note] == HALF) {
      duration = halfNoteMs;
      note++;
      return;
    }
    if (simpsons[note] == QUARTER) {
      duration = quarterNoteMs;
      note++;
      return;
    }
    if (simpsons[note] == EIGHTH) {
      duration = eighthNoteMs;
      note++;
      return;
    }
    
    if (simpsons[note] == SILENCE) {
      noTone(piezoPin);
      delay(duration);
    } else { 
      tone(piezoPin, simpsons[note]);
      delay(duration);
      noTone(piezoPin);
    }
 
    note++;
  }
}
