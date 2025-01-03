import os

def linux_terminal():
    os_name = "ամենա լավ ՕՀ"
    current_directory = os.getcwd()

    print(f"Բարի գալուստ {os_name}-ի տերմինալ:")
    print("Մուտքագրեք `exit` դուրս գալու համար:")
    
    while True:
        # Ցուցադրում ենք հրամանը մուտքագրման համար
        command = input(f"{os_name}:{current_directory}$ ")

        if command.strip() == "exit":
            print("Դուրս ենք գալիս տերմինալից:")
            break
        elif command.strip() == "pwd":
            print(current_directory)
        elif command.strip() == "ls":
            files = os.listdir(current_directory)
            for file in files:
                print(file)
        elif command.startswith("cd "):
            try:
                new_dir = command[3:].strip()
                os.chdir(new_dir)
                current_directory = os.getcwd()
            except FileNotFoundError:
                print("Սխալ: Նշված թղթապանակը գոյություն չունի:")
            except Exception as e:
                print(f"Սխալ: {e}")
        else:
            print("Սխալ: Նշված հրամանը չի աջակցվում:")
    
if __name__ == "__main__":
    linux_terminal()
