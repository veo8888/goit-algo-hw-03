def hanoi_towers(n, source, target, auxiliary, state):
    """
    Рекурсивна функція для вирішення задачі Ханойських веж.

    Параметри:
     n: Кількість дисків
     source: Початковий стрижень
     target: Цільовий стрижень
     auxiliary: Допоміжний стрижень
     state: Стан стрижнів
    """
    if n == 1:
        # Переміщуємо диск з source до target
        disk = state[source].pop()  # Знімаємо верхній диск з початкового стрижня
        state[target].append(disk)  # Кладемо диск на цільовий стрижень
        print(f"\033[35m Перемістити диск з {source} на {target}: {disk} \033[0m")
        print(f"Проміжний стан: \033[36m {state} \033[0m")
    else:
        # Переміщуємо n-1 дисків з source до auxiliary
        hanoi_towers(n - 1, source, auxiliary, target, state)

        # Переміщуємо найбільший диск з source до target
        hanoi_towers(1, source, target, auxiliary, state)

        # Переміщуємо n-1 дисків з auxiliary до target
        hanoi_towers(n - 1, auxiliary, target, source, state)


def main():
    """
    Основна функція для виконання задачі Ханойських веж.
    """
    n = int(input("\n\033[33m Введіть кількість дисків: \033[0m"))  # Вводимо кількість дисків

    # Ініціалізуємо початковий стан стрижнів
    state = {
        'A': list(range(n, 0, -1)),  # Стрижень A (початковий)
        'B': [],  # Стрижень B (допоміжний)
        'C': []   # Стрижень C (цільовий)
    }

    print(f"\n\033[42m Початковий стан: \033[0m {state}")
    hanoi_towers(n, 'A', 'C', 'B', state)  # Викликаємо функцію для вирішення задачі
    print(f"\033[41m Кінцевий стан: \033[0m {state}\n")


if __name__ == "__main__":
    main()
