import sys
from pathlib import Path
from colorama import Fore, Style, init

def visualize_directory(directory_path: str) -> None:
    
    init(autoreset=True)

    directory = Path(directory_path)

    if not directory.exists():
        print(Fore.RED + f"Помилка: Директорія '{directory_path}' не існує.")
        return
    
    if not directory.is_dir():
        print(Fore.RED + f"Помилка: '{directory_path}' не є директорією.")

    print(Fore.CYAN + f"Структура директорії: {directory_path}")
    visualize_directory_recursive(directory)

def visualize_directory_recursive(directory: Path, indent: str = "" ) -> None:

    items = sorted(directory.iterdir())

    for index, item in enumerate(items):

        if item.is_dir():

            print(indent + Fore.BLUE + f"[{item.name}]")
            visualize_directory_recursive(item, indent + "  ")

        else:

            print(indent + Fore.GREEN + f"- {item.name}")

        if index == len(items) - 1:

            print(Style.RESET_ALL, end = "")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Використання: python script.py <шлях_до_директорії>")
        sys.exit(1)

directory_path = sys.argv[1]

visualize_directory(directory_path)

