from typing import List



def print_header(title: str = "TO-DO MANAGER") -> None:
    print("\n" + "=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def show_menu() -> None:
    
    print("\nPlease choose an option:")
    print(" 1) Add task")
    print(" 2) View tasks")
    print(" 3) Delete task")
    print(" 4) Quit")
    print("-" * 50)

def prompt(message: str) -> str:
    
    return input(f"{message} ").strip()

def pause() -> None:
    
    input("\nPress Enter to continue...")



def add_task(tasks: List[str]) -> None:
    """Add a new task to the list."""
    print_header("ADD TASK")
    task = prompt("Enter a task description (or leave blank to cancel):")
    try:
        if not task:
            print("No task added (input was empty).")
            return
        tasks.append(task)
    except Exception as e:
        print(f"Unexpected error while adding task: {e}")
    else:
        print(f"✅ Added: '{task}'")
    finally:
        print("-" * 50)

def view_tasks(tasks: List[str]) -> None:
    """View all tasks, or alert if there are none."""
    print_header("VIEW TASKS")
    try:
        if not tasks:
            raise ValueError("There are no tasks to view.")
        for idx, t in enumerate(tasks, start=1):
            print(f"{idx}. {t}")
    except ValueError as ve:
        
        print(f"⚠️ {ve}")
    except Exception as e:
        print(f"Unexpected error while viewing tasks: {e}")
    else:
        print("-" * 50)
    finally:
        
        print("-" * 50)

def delete_task(tasks: List[str]) -> None:
    """Delete a task by its displayed number."""
    print_header("DELETE TASK")
    if not tasks:
        print("⚠️ There are no tasks to delete.")
        print("-" * 50)
        return

    
    for idx, t in enumerate(tasks, start=1):
        print(f"{idx}. {t}")
    print("-" * 50)

    raw = prompt("Enter the task number to delete (or 'c' to cancel):")
    try:
        if raw.lower() == "c":
            print("Deletion cancelled.")
            return

        num = int(raw) 
        if num < 1 or num > len(tasks):
            raise IndexError("That task number doesn't exist.")

        deleted = tasks.pop(num - 1) 
    except ValueError:
        print("❌ Invalid input. Please enter a valid task number.")
    except IndexError as ie:
        print(f"⚠️ {ie}")
    except Exception as e:
        print(f"Unexpected error while deleting: {e}")
    else:
        print(f"🗑️ Deleted: '{deleted}'")
    finally:
        print("-" * 50)



def get_menu_choice() -> int:
    
    raw = prompt("Your choice (1-4):")
    try:
        choice = int(raw)
    except ValueError:
        
        print("❌ Invalid choice. Please enter a number between 1 and 4.")
        raise 
    else:
        return choice
    finally:
        
        print("-" * 50)

def main() -> None:
    
    tasks: List[str] = []

    print_header("WELCOME")
    print("This is a simple command-line To-Do app.")
    print("Tasks are stored in memory while the app is running.")
    print("-" * 50)

    while True:
        show_menu()
        try:
            choice = get_menu_choice()
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                delete_task(tasks)
            elif choice == 4:
                print("\nGoodbye! 👋")
                break
            else:
                
                print("⚠️ That option doesn't exist. Please choose 1-4.")
        except ValueError:
            
            pass
        except Exception as e:
            
            print(f"An unexpected error occurred: {e}")
        finally:
            
            if 'choice' in locals() and choice != 4:
                pause()

if __name__ == "__main__":
    main()