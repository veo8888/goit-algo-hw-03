# File Sorter

Скрипт для рекурсивного сортування файлів за розширеннями.

---

## Як працює скрипт

1. Читає вміст вихідної директорії, включно з підпапками.
2. Для кожного типу файлів створює окрему піддиректорію за назвою розширення.
3. Копіює файли у відповідні папки.

---

## Аргументи

Скрипт приймає два аргументи:
1. Шлях до вихідної директорії (обов'язковий).
2. Шлях до директорії призначення (необов'язковий). Якщо не вказаний, використовується папка `dist`.

---

## Зразок для перевірки роботи скрипта

File Sorter from directory\random_structure

---

## Як запустити

```bash
python "<шлях до>\file_sorter.py" "<шлях до вихідної директорії>" "[шлях до директорії призначення]"
