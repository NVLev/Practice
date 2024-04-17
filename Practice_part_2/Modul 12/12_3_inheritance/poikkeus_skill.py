class DivisionError(Exception):
    pass

with open("numbers.txt", "r", encoding="utf8") as file:
    for line in file:
        try:
            clear_line = line.rstrip()
            first, second = clear_line.split()
            if int(first) < int(second):
                raise DivisionError("нельзя делить большее на меньшее")
        except (ValueError, DivisionError) as exc:
            print(exc, type(exc), first, second)