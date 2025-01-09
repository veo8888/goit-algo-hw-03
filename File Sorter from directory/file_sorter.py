import os
import shutil
import argparse


def copy_and_sort_files(src_dir, dest_dir):
    """
    Рекурсивно читає файли у вихідній директорії, копіює їх до нової директорії,
    та сортує у піддиректорії за розширенням файлів.

    Параметри:
     src_dir: Шлях до вихідної директорії.
     dest_dir: Шлях до директорії призначення.
    """
    try:
        # Перебір елементів у вихідній директорії
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            # Якщо елемент - директорія, рекурсивно обробляємо її
            if os.path.isdir(item_path):
                copy_and_sort_files(item_path, dest_dir)
            elif os.path.isfile(item_path):
                # Якщо елемент - файл, визначаємо розширення
                file_extension = os.path.splitext(item)[-1].lower()  # Розширення у нижньому регістрі
                if not file_extension:  # Якщо у файлу немає розширення
                    file_extension = "no_extension"

                # Створюємо піддиректорію за розширенням, якщо її ще немає
                extension_dir = os.path.join(dest_dir, file_extension.strip('.'))
                os.makedirs(extension_dir, exist_ok=True)

                # Копіюємо файл до відповідної піддиректорії
                shutil.copy2(item_path, extension_dir)
    except PermissionError as e:
        print(f"Помилка доступу: {e}")
    except Exception as e:
        print(f"Сталася помилка: {e}")


def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description="Рекурсивно копіює файли, сортує їх за розширенням.")
    parser.add_argument("src", help="Шлях до вихідної директорії")
    parser.add_argument("dest", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням: 'dist')")

    args = parser.parse_args()

    # Перевірка, чи існує вихідна директорія
    print(f"Шлях до вихідної директорії: {args.src}")
    if not os.path.exists(args.src) or not os.path.isdir(args.src):
        print(f"Вказана вихідна директорія '{args.src}' не існує або не є директорією.")
        return

    # Створюємо директорію призначення, якщо її немає
    os.makedirs(args.dest, exist_ok=True)

    # Запускаємо функцію сортування
    copy_and_sort_files(args.src, args.dest)
    print(f"Файли успішно скопійовані та відсортовані у '{args.dest}'.")


if __name__ == "__main__":
    main()
