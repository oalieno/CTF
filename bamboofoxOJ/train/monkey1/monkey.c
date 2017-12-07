#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void print_monkey(void)
{
    system("cat /home/ctf/graph");
    fflush(stdout);
}
void menu(void)
{
    printf("1 : change name\n");
    printf("2 : program\n");
    printf("3 : flag\n");
    printf("4 : monkey\n");
    printf("5 : exit\n");
    printf("Please enter your choice!\n");
    fflush(stdout);
};
void change_name(char* name)
{
    printf("Your name is %s now.\n",name);
    printf("Please enter your new name\n");
    printf("Please less than 20 characters\n");
    fgets(name,28,stdin);
    if(strlen(name)>=20)
    {
        printf("Sorry maybe next time.\n");
        exit(-1);
    }
    printf("Change name succeed\n");
    printf("You are %s now.\n",name);
    fflush(stdout); 
}
void program(void)
{
    char temp[1024];
    memset(temp,0,sizeof(temp));
    printf("Enter your code.\n");
    printf("I will print it out.\n");
    fflush(stdout); 
    fgets(temp,1024,stdin);
    printf(temp);
    printf("\n");
    fflush(stdout); 
}
void flag(int banana)
{
    if(banana==0x3132000a)
    {
        char flag[100];
        FILE * fp=fopen("/home/ctf/flag","r");
        fscanf(fp,"%s",flag);
        printf("%s",flag);
        fflush(stdout); 
    }
    else
    {
        printf("Wrong banana %d\n",banana);
        fflush(stdout); 
    }
}
int main(void)
{
    print_monkey();
    printf("****************************************************\n");
    printf("* Hello monkey programmer!!!                       *\n");
    printf("* Welcome to monkey programmer system!!!           *\n");
    printf("* This system will guide you how to hire a trained *\n");
    printf("* monkey to do your job!!!                         *\n");
    printf("****************************************************\n");
    int banana=1;
    char name[20]="Bamboofox";
    int choice;
    while(1)
    {
        menu();
        scanf("%d",&choice);
        getchar();
        switch(choice)
        {
            case 1:
                change_name(name);
                break;
            case 2:
                program();
                break;
            case 3:
                flag(banana);
                break;
            case 4:
                print_monkey();
                break;
            case 5:
                printf("Bye.\n");
                fflush(stdout);
                return 0;
            default:
                break;
        }
    }
}
