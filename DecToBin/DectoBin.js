var Decimal = prompt("Type a Number to convert to Binary. MUST BE LESS THAN OR EQUAL TO '255'!");
while(Decimal > 255){
Decimal = prompt("INCORRECT NUMBER MUST BE LESS THAN OR EQUAL TO '255'! Type a Number to conver to Binary.");
}
var array = [0,0,0,0,0,0,0,0];

if(Decimal >= 128){
           array[0] = 1;
   Decimal = Decimal - 128;
           };
if(Decimal >= 64){
           array[1] = 1;
  Decimal = Decimal - 64;
           };
if(Decimal >= 32){
           array[2] = 1;
  Decimal = Decimal - 32;
           };
if(Decimal >= 16){
           array[3] = 1;
  Decimal = Decimal - 16;
           };
if(Decimal >= 8){
           array[4] = 1;
  Decimal = Decimal - 8;
           };
if(Decimal >= 4){
           array[5] = 1;
  Decimal = Decimal - 4;
           };
if(Decimal >= 2){
           array[6] = 1;
  Decimal = Decimal - 2;
           };
if(Decimal >= 1){
           array[7] = 1;
  Decimal = Decimal - 1;
           };

document.write(array);