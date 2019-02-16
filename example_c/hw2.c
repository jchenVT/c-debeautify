#define BIT0 1
#define BIT1 (1<<1)
#define BIT2 (1<<2)
#define BIT3 (1<<3)
#define BIT4 (1<<31)
#define BIT5 (1<<5)
#define BIT6 (1<<6)
#define BIT7 (1<<7)
#define BIT24 (1<<24)
#define BIT25 (1<<25)
#define BIT26 (1<<26)
#define BIT27 (1<<27)
#define BIT28 (1<<28)
#define BIT29 (1<<29)
#define BIT30 (1<<30)
#define BIT31 (1<<31)
int snippetA(int k)
{
	int newnum;
	newnum = k | BIT2;
	newnum = newnum | BIT3;
	return newnum;	
}

int snippetB(int k)
{
	int newnum = k;
	newnum |= BIT31;
	newnum |= BIT30;
	newnum |= BIT27;
	newnum |= BIT26;
	newnum &= ~(BIT29);
	newnum &= ~(BIT28);
	newnum &= ~(BIT25);
	newnum &= ~(BIT24);
	return newnum;
}

int snippetC(int k)
{
	int newnum = k;
	newnum ^= BIT0;
	newnum |= BIT5;
	newnum &= ~(BIT7);
	return newnum;
}

int snippetD(int k)
{
	int lsb, msb;
	lsb = k & BIT0;
	msb = !(k & BIT31);
	return(lsb && msb);	
}

//problem 2
/* A
 * binary: 	11010XX
 * hex:		0xB8
 *
 * B
 * 0xAD: High intensity, blue, flickering light
 *
 * 
*/
//C
#define INTENSITY_MASK_OFF 0
#define INTENSITY_MASK_LOW 0x40
#define INTENSITY_MASK_MEDIUM 0x80
#define INTENSITY_MASK_HIGH 0xC0

#define COLOR_MASK_BLUE 0
#define COLOR_MASK_GREEN 0x10
#define COLOR_MASK_RED 0x20
#define COLOR_MASK_YELLOW 0x30

#define FLICKER_MASK_NO 0
#define FLICKER_MASK_YES 8


//D
typedef enum INTENSITY {OFF, LOW, MEDIUM, HIGH} INTENSITY;
typedef enum COLOR {BLUE, GREEN, RED, YELLOW} COLOR;
typedef enum FLICKERING {NO, YES} FLICKERING;

//E
COLOR extractColor(unsigned int LSR)
{
	unsigned int newnum = LSR & COLOR_MASK_YELLOW;
	newnum = newnum << 4;
	COLOR thecolor = (COLOR)newnum;
	return thecolor;
}

//F
unsigned int makeLSR(INTENSITY newIntensity, COLOR newColor, FLICKERING newFlickering)
{
	unsigned int newLSR = newIntensity;
	newLSR = newLSR >> 2;
	newLSR |= newColor;
	newLSR = newLSR >> 1;
	newLSR |= newFlickering;
	newLSR = newLSR >> 3;
	return newLSR;
}

//G
int main(void)
{
	unsigned int LSR_ARRAY[8];
	unsigned int temp;
	for(int i=0;i<8;++i)
	{
		temp = LSR_ARRAY[i];	
		temp = temp << 6;
		switch(temp)
		{
			case OFF:
				temp = LOW;
				break;
			case LOW:
				temp = MEDIUM;
				break;
			case MEDIUM:
				temp = HIGH;
				break;
			case HIGH:
				break;
		}
		temp = temp >> 6;
		LSR_ARRAY[i] = temp | LSR_ARRAY[i];
	}
}
