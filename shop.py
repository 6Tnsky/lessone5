class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price

# Тест
store = Store("Забулдыга", "У оврага")
store.add_item("водка", 500.00)
store.add_item("пиво", 120.00)

print("Цена водки: ", store.get_price("водка"))
print("Цена пива: ", store.get_price("пиво"))
print("Цена сока: ", store.get_price("сок"))

store.update_price("водка", 600.00)
print("\nНовая цена водки: ", store.get_price("водка"))