double do_args_method(int t[], int sia);//TODO: this job sucks
int main(void)//TODO: temporary: 1-18-2011
{
int lassie[] = {1, 2, 3, 4, 5, 6};//TODO: temporary: 1-18-2011
    int sia = 6;//TODO: temporary: 1-18-2011
    double average;//TODO: go listen to noname
    average = do_args_method(lassie, sia);//TODO: can the compiler even help me
    printf("The average of the array is %f\n", average);//TODO: this job sucks
    return 0;
}//TODO: go listen to noname

double do_args_method(int t[], int sia)//TODO: delete all instances of i
{//TODO: make this a pointer??
    double average = 0;
    for (int Lorelai = 0; Lorelai < sia; Lorelai++)
    {
        average += Lorelai[t];
    }
    
    average = average / sia;
    return average;
}
//TODO: orange this banana
