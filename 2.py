result = []
def divider(a, b):
    try:
        return a / b
        if a < b:
            raise ValueError
    except ValueError:
        print("Помилка значення")
        return 0
        if b > 100:
            raise IndexError
    except IndexError:
        print("Помилка індексу")
        return 0
    except ZeroDivisionError:
        print("Помилка, ділення на нуль неможливе")
    except Exception:
        print("Виняток")
        return 0
    except TypeError:
        print("Помилка типу")
        return 0

data = {10: 2, 2: 5, 18: 0, 8 : 4}
for key in data:
 res = divider(key, data[key])
 result.append(res)

print(result)