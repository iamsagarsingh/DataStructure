#include<stdio.h>
#include<stdlib.h>
struct node 
{
int data;
struct node* next;
};
struct node* head;
void insert(int);
void display();
void main()
{
	int i,x,ele;
	head = NULL;
	printf("Enter no of Elements: ");
	scanf("%d",&x);
	for(i=0;i<x;i++)
	{
		printf("\nEnter element: ");
		scanf("%d",&ele);
		insert(ele);
		display();
	}
}
void insert(int ele)
{
	struct node* temp = (struct node*)malloc(sizeof(struct node));
	temp->data = ele;
	temp->next = NULL;
	if (head==NULL)
	{
		head = temp;
	}
	else
	{
		struct node* ptr;
		//struct node* str;
		ptr = head;
		while(ptr->next != NULL)
		{	//str = ptr;
			ptr = ptr->next;
		}
		ptr->next = temp;
	}
}
void display()
{
	if (head == NULL)
	{
		printf("Emplty linked list:>");
		return;
	}
	else
	{
		struct node* p;
		p = head;
		printf("Linked list is: ");
		while(p!=NULL)
		{
			printf("%d",p->data);
			p = p->next;
		}
	}
}
