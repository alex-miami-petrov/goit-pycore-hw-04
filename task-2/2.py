
def get_cats_info(path: str) -> list[dict[str, str]]:

    try:

        with open("task-2/cats_file.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

    except FileNotFoundError:
        return []
    
    cats_info = []

    for line in lines:
        try:

            cat_id, name, age = line.strip().split(",")
            cats_info.append({"id": cat_id, "name": name, "age": age})

        except ValueError:
            continue

    return cats_info


cats_info = get_cats_info("task-2/cats_file.txt")
print(cats_info)


