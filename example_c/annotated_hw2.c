#define BIT0 1 //type: pound, randomadd: False
#define BIT1 (1<<1) //type: pound, randomadd: False
#define BIT2 (1<<2) //type: pound, randomadd: False
#define BIT3 (1<<3) //type: pound, randomadd: False
#define BIT4 (1<<31) //type: pound, randomadd: False
#define BIT5 (1<<5) //type: pound, randomadd: False
#define BIT6 (1<<6) //type: pound, randomadd: False
#define BIT7 (1<<7) //type: pound, randomadd: False
#define BIT24 (1<<24) //type: pound, randomadd: False
#define BIT25 (1<<25) //type: pound, randomadd: False
#define BIT26 (1<<26) //type: pound, randomadd: False
#define BIT27 (1<<27) //type: pound, randomadd: False
#define BIT28 (1<<28) //type: pound, randomadd: False
#define BIT29 (1<<29) //type: pound, randomadd: False
#define BIT30 (1<<30) //type: pound, randomadd: False
#define BIT31 (1<<31) //type: pound, randomadd: False
int snippetA(int k) //type: function, randomadd: False
{ //type: , randomadd: False
    	int newnum; //type: , randomadd: False
    	newnum = k | BIT2; //type: , randomadd: False
    	newnum = newnum | BIT3; //type: , randomadd: False
    	return newnum;	 //type: , randomadd: False
} //type: , randomadd: False
 //type: , randomadd: False
int snippetB(int k) //type: function, randomadd: False
{ //type: , randomadd: False
    	int newnum = k; //type: , randomadd: False
    	newnum |= BIT31; //type: , randomadd: False
    	newnum |= BIT30; //type: , randomadd: False
    	newnum |= BIT27; //type: , randomadd: False
    	newnum |= BIT26; //type: , randomadd: False
    	newnum &= ~(BIT29); //type: , randomadd: False
    	newnum &= ~(BIT28); //type: , randomadd: False
    	newnum &= ~(BIT25); //type: , randomadd: False
    	newnum &= ~(BIT24); //type: , randomadd: False
    	return newnum; //type: , randomadd: False
} //type: , randomadd: False
 //type: , randomadd: False
int snippetC(int k) //type: function, randomadd: False
{ //type: , randomadd: False
    	int newnum = k; //type: , randomadd: False
    	newnum ^= BIT0; //type: , randomadd: False
    	newnum |= BIT5; //type: , randomadd: False
    	newnum &= ~(BIT7); //type: , randomadd: False
    	return newnum; //type: , randomadd: False
} //type: , randomadd: False
 //type: , randomadd: False
int snippetD(int k) //type: function, randomadd: False
{ //type: , randomadd: False
    	int lsb, msb; //type: , randomadd: False
    	lsb = k & BIT0; //type: , randomadd: False
    	msb = !(k & BIT31); //type: , randomadd: False
    	return(lsb && msb);	 //type: , randomadd: False
} //type: , randomadd: False
 //type: , randomadd: False
//problem 2 //type: , randomadd: False
/* A //type: , randomadd: False
 * binary: 	11010XX //type: , randomadd: False
 * hex:		0xB8 //type: , randomadd: False
 * //type: , randomadd: False
 * B //type: , randomadd: False
 * 0xAD: High intensity, blue, flickering light //type: , randomadd: False
 * //type: , randomadd: False
 *  //type: , randomadd: False
*/ //type: , randomadd: False
//C //type: , randomadd: False
#define INTENSITY_MASK_OFF 0 //type: pound, randomadd: False
#define INTENSITY_MASK_LOW 0x40 //type: pound, randomadd: False
#define INTENSITY_MASK_MEDIUM 0x80 //type: pound, randomadd: False
#define INTENSITY_MASK_HIGH 0xC0 //type: pound, randomadd: False
 //type: , randomadd: False
#define COLOR_MASK_BLUE 0 //type: pound, randomadd: False
#define COLOR_MASK_GREEN 0x10 //type: pound, randomadd: False
#define COLOR_MASK_RED 0x20 //type: pound, randomadd: False
#define COLOR_MASK_YELLOW 0x30 //type: pound, randomadd: False
 //type: , randomadd: False
#define FLICKER_MASK_NO 0 //type: pound, randomadd: False
#define FLICKER_MASK_YES 8 //type: pound, randomadd: False
 //type: , randomadd: False
 //type: , randomadd: False
//D //type: , randomadd: False
typedef enum INTENSITY {OFF, LOW, MEDIUM, HIGH} INTENSITY; //type: , randomadd: False
typedef enum COLOR {BLUE, GREEN, RED, YELLOW} COLOR; //type: , randomadd: False
typedef enum FLICKERING {NO, YES} FLICKERING; //type: , randomadd: False
 //type: , randomadd: False
//E //type: , randomadd: False
COLOR extractColor(unsigned int LSR) //type: function, randomadd: False
{ //type: , randomadd: False
    	unsigned int newnum = LSR & COLOR_MASK_YELLOW; //type: , randomadd: False
    	newnum = newnum << 4; //type: , randomadd: False
    	COLOR thecolor = (COLOR)newnum; //type: , randomadd: False
    	return thecolor; //type: , randomadd: False
} //type: , randomadd: False
 //type: , randomadd: False
//F //type: , randomadd: False
unsigned int makeLSR(INTENSITY newIntensity, COLOR newColor, FLICKERING newFlickering) //type: function, randomadd: False
{ //type: , randomadd: False
    	unsigned int newLSR = newIntensity; //type: , randomadd: False
    	newLSR = newLSR >> 2; //type: , randomadd: False
    	newLSR |= newColor; //type: , randomadd: False
    	newLSR = newLSR >> 1; //type: , randomadd: False
    	newLSR |= newFlickering; //type: , randomadd: False
    	newLSR = newLSR >> 3; //type: , randomadd: False
    	return newLSR; //type: , randomadd: False
} //type: , randomadd: False
 //type: , randomadd: False
//G //type: , randomadd: False
int main(void) //type: function, randomadd: False
{ //type: , randomadd: False
    	unsigned int LSR_ARRAY[8]; //type: , randomadd: False
    	unsigned int temp; //type: , randomadd: False
    	for(int i=0;i<8;++i) //type: loop, randomadd: False
    	{ //type: , randomadd: False
        		temp = LSR_ARRAY[i];	 //type: , randomadd: False
        		temp = temp << 6; //type: , randomadd: False
        		switch(temp) //type: switch, randomadd: False
        		{ //type: switch, randomadd: False
            			case OFF: //type: switch, randomadd: False
            				temp = LOW; //type: switch, randomadd: False
            				break; //type: switch, randomadd: False
            			case LOW: //type: switch, randomadd: False
            				temp = MEDIUM; //type: switch, randomadd: False
            				break; //type: switch, randomadd: False
            			case MEDIUM: //type: switch, randomadd: False
            				temp = HIGH; //type: switch, randomadd: False
            				break; //type: switch, randomadd: False
            			case HIGH: //type: switch, randomadd: False
            				break; //type: switch, randomadd: False
        		} //type: switch, randomadd: False
        		temp = temp >> 6; //type: , randomadd: False
        		LSR_ARRAY[i] = temp | LSR_ARRAY[i]; //type: , randomadd: False
    	} //type: , randomadd: False
} //type: , randomadd: False
