"""To-Do List Application"""

# Initialize an empty to-do list
todo_list = []

while True:
    # Display menu
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark task as complete")
    print("4. Exit")

    # Get user choice 
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # Add Task 
        task = input("Enter task: ")
        todo_list.append({"task":task, "completed":False})
        print("Task added!")

    elif choice == "2":
        # View task 
        if not todo_list:
            print("No tasks in the to-do list.")
        else:
            print("\nTasks: ")
            for i, item in enumerate(todo_list,1):
                status = "   " if item["completed"] else "  "
                print(f"{i}. [{status}] {item['task']}")

    elif choice == "3":
        # Mark task as complete 
        if not todo_list:
            print("No task in the to-do list. ")
        else:
            task_num = int(input("Enter task number to mark as complete:"))
            if 1 <= task_num <=len(todo_list):
                todo_list[task_num - 1]["completed"] = True
                print("Task marked as complete!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        # Exit 
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")