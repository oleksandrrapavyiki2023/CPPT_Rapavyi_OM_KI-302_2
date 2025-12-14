from Copier import Copier

if __name__ == "__main__":
    # Створюємо копіювальний апарат
    copier = Copier(brand="Xerox", model="X1000", scan_resolution="2400x2400 dpi", copy_speed=30)

    # Демонструємо початковий статус пристрою
    print("\n1. Початковий стан пристрою:")
    print(copier.get_status())

    # Виконуємо кілька дій
    print("\n2. Сканування та копіювання документів:")
    copier.scan_document("Квитанція.pdf")
    copier.copy_document("Рахунок.docx")
    copier.copy_document("Інструкція.pdf", copies=3)

    # Перевірка функцій управління живленням
    print("\n3. Управління живленням:")
    copier.turn_on()
    copier.turn_off()
    copier.turn_on()

    # Використання сканера у кольоровому та чорно-білому режимах
    print("\n4. Сканування у різних режимах:")
    copier.set_color_mode("чорно-білий")
    copier.scan_document("Заява.docx")
    copier.set_color_mode("кольоровий")
    copier.scan_document("Презентація.pdf")

    # Перевірка налаштувань роздільної здатності
    print("\n5. Зміна роздільної здатності сканування:")
    copier.set_scan_resolution("300x300 dpi")
    copier.scan_document("Чек.pdf")

    # Встановлення нової швидкості копіювання
    print("\n6. Зміна швидкості копіювання:")
    copier.set_copy_speed(50)
    print(f"Нова швидкість копіювання: {copier.copy_speed} сторінок/хвилину")

    # Виконання обслуговування
    print("\n7. Технічне обслуговування:")
    copier.perform_maintenance()

    # Демонстрація фінального статусу
    print("\n8. Фінальний статус пристрою:")
    print(copier.get_status())
