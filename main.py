tasks = []
def show_menu():
print("\n1 .Add Task")
print("2. veiw Tasks")
print("3. Exit")

while true: 
show_menu() 
choice = input("Entger choice:") 
if choice == "1": 
task + input("Enter task:") 
tasks.append(task) print("tasks added.") 
elif choice == "2": 
print("\nTasks:") for i<t in enumerate(tasks,start=1):
print(i,t)
elif choice == "3":
print("Existing...")
break
else:
print("invalid choice")
