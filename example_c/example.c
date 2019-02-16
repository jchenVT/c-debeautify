#include <stdio.h>

/** Compute the average value in an array of integers
@param arr an array of integers
@param size number of integers in arr
@return average value in arr */
double getAverage(int arr[], int size);


int main(void)
{
	int array[] = {1, 2, 3, 4, 5, 6};
	int size = 6;
	double average;
	average = getAverage(array, size);
	printf("The average of the array is %f\n", average);
	return 0;
}


double getAverage(int arr[], int size)
{
	double average = 0;	
	for(int i=0; i<size; i++)
	{
		average += arr[i];
	}
	average = average/size;
	
	return average;
}
