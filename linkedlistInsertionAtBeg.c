/*
This is insertion of elements at the beginning of the linked list.
*/
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
	int x,i,ele;
	head = NULL;
	printf("Enter No of  Elements to enter:");
	scanf("%d",&x);
	for(i=0;i<x;i++)
	{
		printf("\nEnter Element: ");
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
	if (head == NULL)
		head = temp;
	else
	{
		struct node* ptr;
		ptr = head;
		head = temp;
		temp->next = ptr;
	}
}
void display()
{
	if (head == NULL)
	{
		printf("Linked list is empty");
		return;
	}
	else
	{
		struct node* p;
		p = head;
		printf("Linked List is:");
		while(p != NULL)
		{
			printf("%d",p->data);
			p = p->next;
		}
	}
}
