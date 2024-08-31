import os
from datetime import datetime

class SimpleShell:
    def __init__(self):
        self.current_directory = os.getcwd()

    def cd(self, path):
        try:
            os.chdir(path)
            self.current_directory = os.getcwd()
        except Exception as e:
            print(f"Error: {e}")

    def ls(self):
        print("\n".join(os.listdir(self.current_directory)))

    def date(self):
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def run(self):
        while True:
            command = input(f"{self.current_directory} >>> ")
            if command == "exit":
                break
            elif command.startswith("cd "):
                self.cd(command.split(" ")[1])
            elif command == "ls":
                self.ls()
            elif command == "date":
                self.date()
            else:
                print("Unknown command")

def main():
    shell = SimpleShell()
    shell.run()

if __name__ == "__main__":
    main()
