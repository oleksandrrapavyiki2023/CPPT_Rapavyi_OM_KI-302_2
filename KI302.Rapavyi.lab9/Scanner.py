class Scanner:
    """
    Базовий клас Scanner, що представляє пристрій для сканування документів.
    """

    def __init__(self, brand, model, scan_resolution):
        """
        Ініціалізує об'єкт сканера.

        :param brand: Бренд сканера.
        :param model: Модель сканера.
        :param scan_resolution: Роздільна здатність сканування.
        """
        self.brand = brand
        self.model = model
        self.scan_resolution = scan_resolution
        self.is_powered_on = False
        self.color_mode = "кольоровий"

    def turn_on(self):
        """Увімкнення сканера."""
        self.is_powered_on = True
        print(f"{self.brand} {self.model} увімкнений.")

    def turn_off(self):
        """Вимкнення сканера."""
        self.is_powered_on = False
        print(f"{self.brand} {self.model} вимкнений.")

    def scan_document(self, document_name):
        """Сканування документа."""
        if not self.is_powered_on:
            print(f"{self.brand} {self.model} вимкнений. Увімкніть сканер для сканування.")
            return
        print(f"Сканування документу '{document_name}' в режимі {self.color_mode} з роздільною здатністю {self.scan_resolution}.")

    def set_color_mode(self, mode):
        """Встановлення режиму сканування (кольоровий/чорно-білий)."""
        self.color_mode = mode
        print(f"Режим сканування змінено на {mode}.")

    def set_scan_resolution(self, resolution):
        """Встановлення роздільної здатності сканування."""
        self.scan_resolution = resolution
        print(f"Роздільна здатність змінена на {resolution}.")

    def perform_maintenance(self):
        """Виконання технічного обслуговування."""
        print(f"{self.brand} {self.model} обслуговано. Все готово до роботи.")

    def get_status(self):
        """Отримання статусу сканера."""
        power_status = "увімкнений" if self.is_powered_on else "вимкнений"
        return f"Сканер {self.brand} {self.model}: {power_status}, роздільна здатність {self.scan_resolution}, режим {self.color_mode}."
