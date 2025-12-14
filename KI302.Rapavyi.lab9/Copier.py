from Scanner import Scanner

class Copier(Scanner):
    """
    Похідний клас Copier, що додає функціональність копіювання до базового класу Scanner.
    """

    def __init__(self, brand, model, scan_resolution, copy_speed):
        """
        Ініціалізує об'єкт копіювального апарата.

        :param brand: Бренд копіювального апарата.
        :param model: Модель копіювального апарата.
        :param scan_resolution: Роздільна здатність сканування.
        :param copy_speed: Швидкість копіювання (сторінок/хвилину).
        """
        super().__init__(brand, model, scan_resolution)
        self.copy_speed = copy_speed

    def copy_document(self, document_name, copies=1):
        """Копіює документ у заданій кількості."""
        if not self.is_powered_on:
            print(f"{self.brand} {self.model} вимкнений. Увімкніть пристрій для копіювання.")
            return
        print(f"Копіювання документу '{document_name}' ({copies} копій) зі швидкістю {self.copy_speed} стор./хв.")

    def set_copy_speed(self, new_speed):
        """Змінює швидкість копіювання."""
        self.copy_speed = new_speed
        print(f"Швидкість копіювання змінена на {new_speed} стор./хв.")

    def scan_and_copy(self, document_name):
        """Сканує документ і одразу створює його копію."""
        self.scan_document(document_name)
        self.copy_document(document_name)

    def get_status(self):
        """Отримує статус копіювального апарата."""
        base_status = super().get_status()
        return f"{base_status}, швидкість копіювання: {self.copy_speed} стор./хв."

    def set_copy_quality(self, quality):
        """Змінює якість копіювання."""
        print(f"Якість копіювання встановлено: {quality}.")

