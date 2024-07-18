# -*- coding: utf-8 -*-
"""Todo List.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Rq1jfZTUK1CkKgn854FbLEKaU7l6iFYc
"""

#Todo list to keep track of tasks
print("Welcome to Todo List. Enter your task with comma separated ")
todoList = str(input()).split(',')
#print(todoList)
choice = 'yes'
while choice != 'exit':
  choice = str(input("Do you want to add any tasks? If add type yes, to remove type no else type exit "))
  if choice == 'yes':
    task = str(input("Enter the task to add "))
    todoList.append(task)
    #print(todoList)
    print("Todo tasks are, ")
    for task in todoList:
      print(f"-{task}")
  elif choice == 'no':
    task = str(input("Enter the task to remove "))
    todoList.remove(task)
    print("Tasks left are, ")
    for task in todoList:
      print(f"-{task}")
  else:
    print("Exited!")
    break