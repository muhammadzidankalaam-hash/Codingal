total_tasks = 4
originaltasks = total_tasks
print(f"you have {originaltasks} tasks to finish today")
completed_task = 0
task_num = 1
while task_num <= total_tasks:
    if task_num == 1: next_task = "make your bed"
    elif task_num == 2: next_task = "brush your teeth"
    elif task_num == 3: next_task =  "eat your breakfast"
    else:next_task = "wash the dishes"
    answer = input(f"have you finished {next_task}?yes/no")
    if answer == "yes":
        completed_task +=1
        task_num +=1
        print("Great job all the tasks have been completed")
    else:
        print("Okay, finish it and check again")
    print(" tasks remaining:", total_tasks - completed_task)


          
              


        