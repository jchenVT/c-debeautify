#include <stdio.h> //type: pound, randomadd: False
 //type: , randomadd: False
/** Compute the average value in an array of integers //type: , randomadd: False
@param arr an array of integers //type: , randomadd: False
@param size number of integers in arr //type: , randomadd: False
@return average value in arr */ //type: , randomadd: False
double getAverage(int arr[], int size); //type: function, randomadd: False
 //type: , randomadd: False
 //type: , randomadd: False
int main(void) //type: function, randomadd: False
{ //type: , randomadd: False
    	int array[] = {1, 2, 3, 4, 5, 6}; //type: , randomadd: False
    	int size = 6; //type: , randomadd: False
    	double average; //type: , randomadd: False
    	average = getAverage(array, size); //type: , randomadd: False
    	printf("The average of the array is %f\n", average); //type: , randomadd: False
    	return 0; //type: , randomadd: False
    } //type: , randomadd: False
 //type: , randomadd: False
 //type: , randomadd: False
double getAverage(int arr[], int size) //type: function, randomadd: False
{ //type: , randomadd: False
    	double average = 0;	 //type: , randomadd: False
    	for(int i=0; i<size; i++) //type: loop, randomadd: False
    	{ //type: , randomadd: False
        		average += arr[i]; //type: , randomadd: False
        	} //type: , randomadd: False
    	average = average/size; //type: , randomadd: False
    	 //type: , randomadd: False
    	return average; //type: , randomadd: False
    } //type: , randomadd: False
