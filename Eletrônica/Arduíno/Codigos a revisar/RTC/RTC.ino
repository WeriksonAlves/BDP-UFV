#include "Wire.h"
 
void setup( void )
{
  Wire.begin() ;
  Serial.begin( 115200 ) ;

}
void loop( void )
{
  char * week[] = { "","Domingo"      , "Segunda-feira" , "Terca-feira" ,
                    "Quarta-feira" , "Quinta-feira"  , "Sexta-feira" ,
                    "Sabado" } ;
 
  char * month[] = { "","Janeiro"  , "Fevereiro" , "Marco"    , "Abril"      ,
                     "Maio"     , "Junho"     , "Julho"    , "Agosto"     ,
                     "Setembro" , "Outubro"   , "Novembro" , "Dezembro" } ;
  
  unsigned char buf[ 7 ] ;
  unsigned char i ;
  
  Wire.beginTransmission( 0x68 ) ;
  Wire.write( 0x00 ) ; // Endereço 00h.
  Wire.endTransmission();
 
  Wire.requestFrom( 0x68 , 7 ) ;
 
  for( i = 0 ; i < 7 ; i++ )
  {
    buf[ i ] = Wire.read() ;
  }
 
  Serial.print( week[ ( buf[ 3 ]  ) ] ) ;
  Serial.print( ", " ) ;
  Serial.print( buf[ 4 ] , HEX ) ;
  Serial.print( " de " ) ;
  Serial.print( month[ buf[ 5 ] ] ) ;
  Serial.print( " de 20" ) ;
  Serial.print( buf[ 6 ]  , HEX ) ;
  Serial.print( " " ) ;
  Serial.print( buf[ 2 ] , HEX ) ;
  Serial.print( ":" ) ;
  Serial.print( buf[ 1 ], HEX ) ;
  Serial.print( ":" ) ;
  Serial.print( buf[ 0 ], HEX ) ;
 
  Serial.println() ;
  
  delay( 1000 ) ;
}
