#include <stdio.h> //type: pound, randomadd: False
#include <string.h> //type: pound, randomadd: False
  //type: , randomadd: False
struct student  //type: struct, randomadd: False
{ //type: switchorstruct, randomadd: False
                int id; //type: switchorstruct, randomadd: False
                char name[20]; //type: switchorstruct, randomadd: False
                float percentage; //type: switchorstruct, randomadd: False
} record; //type: switchorstruct, randomadd: False
  //type: , randomadd: False
int main()  //type: , randomadd: False
{ //type: , randomadd: False
      //type: , randomadd: False
                record.id=1; //type: , randomadd: False
                strcpy(record.name, "Raju"); //type: , randomadd: False
                record.percentage = 86.5; //type: , randomadd: False
      //type: , randomadd: False
                printf(" Id is: %d \n", record.id); //type: , randomadd: False
                printf(" Name is: %s \n", record.name); //type: , randomadd: False
                printf(" Percentage is: %f \n", record.percentage); //type: , randomadd: False
                return 0; //type: , randomadd: False
} //type: , randomadd: False
