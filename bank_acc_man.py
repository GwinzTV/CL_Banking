import concurrent.futures

# Define a function to simulate a task that takes some time to complete
def simulate_task(task_id):
    print(f"Task {task_id} started")
    # Simulate some time-consuming task
    result = sum(i * i for i in range(10**7))
    print(f"Task {task_id} completed")
    return result

def main():
    # Create a ThreadPoolExecutor with a maximum of 5 threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Submit tasks to the executor
        futures = [executor.submit(simulate_task, i) for i in range(10)]
        
        # Wait for all tasks to complete and collect results
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
        
        # Print results
        print("All tasks completed. Results:")
        for task_id, result in enumerate(results):
            print(f"Task {task_id}: Result = {result}")

if __name__ == "__main__":
    main()
