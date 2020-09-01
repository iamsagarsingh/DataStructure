#include<stdio.h>
#define max_size 5
int arr[max_size];
int top = -1;
int display()
{
	printf("Array is:");
	for(int i=0;i<max_size;i++)
	{
	printf("%d",arr[i]);
	}
}
void push(int x)
{
	if(top == (max_size -1))
	{
	printf("OVERFLOW!!!!!!!\n");
	return;
	}
	else
	{
	top++;
	arr[top] = x;

	}
}
void pop()
{
	if(top == -1)
		printf("UNDERFLOW!!!\n");
	else
	{
		arr[top] = 0;
		top--;
	}
}
void main()
{
	int choice=1,x;
	while(choice!=3)
	{
		printf("\n1.push \n2.POP \n3.quit \nChoose:");
		scanf("%d",&choice);
		if(choice == 1)
		{	printf("Enter element to push: ");
			scanf("%d",&x);
			push(x);
			display();
		}
		else if (choice == 2)
		{	pop();
			display();
		}
	}
}
