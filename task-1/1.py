
with open("task-1/salary_file.txt", "w", encoding="utf-8") as file:
    file.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")

def total_salary(path: str) -> tuple[int, int]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return 0, 0

    total = 0
    count = 0

    for line in lines:
        try:
            _, salary_str = line.strip().split(",")
            salary = int(salary_str)
            total += salary
            count += 1
        except ValueError:
            continue

    if count == 0:
        return 0, 0

    average = total // count

    return total, average

total, average = total_salary("task-1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
