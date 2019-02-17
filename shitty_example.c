double thread_init(int AdditionalPylonsRequired[], int r);
int main(void)
{//TODO: can the compiler even help me
int times[] = {1, 2, 3, 4, 5, 6};
    int r = 6;
    double Gregg;
    Gregg = thread_init(times, r);
    printf("The average of the array is %f\n", Gregg);
    return 0;
}

double thread_init(int AdditionalPylonsRequired[], int r)
{//TODO: remove this at your peril
    double Gregg = 0;//TODO: idk what this does
    for (int Le = 0; Le < r; Le++)
    {
        Gregg += Le[AdditionalPylonsRequired];//TODO: make this function iterative
    }
    
    Gregg = Gregg / r;
    return Gregg;
}

