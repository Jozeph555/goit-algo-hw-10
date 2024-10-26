"""
Модуль для розв'язання задачі оптимізації виробництва напоїв.

Задача полягає в максимізації загальної кількості вироблених напоїв
(лимонаду та фруктового соку) з урахуванням обмежень на ресурси.

Рецептура напоїв:
- Лимонад: 2 од. води, 1 од. цукру, 1 од. лимонного соку
- Фруктовий сік: 1 од. води, 2 од. фруктового пюре

Наявні ресурси:
- Вода: 100 од.
- Цукор: 50 од.
- Лимонний сік: 30 од.
- Фруктове пюре: 40 од.
"""


import pulp


def create_production_model() -> pulp.LpProblem:
    """
    Створює та налаштовує модель оптимізації виробництва.
    
    Returns:
        pulp.LpProblem: Налаштована модель оптимізації
    """
    # Ініціалізація моделі
    model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

    # Визначення змінних
    lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Integer')
    fruit_juice = pulp.LpVariable('fruit_juice', lowBound=0, cat='Integer')

    # Функція цілі (Максимізація виробництва)
    model += lemonade + fruit_juice, "Production"

    # Додавання обмежень
    # Обмеження для води: 2 од. на лимонад + 1 од. на сік <= 100
    model += 2 * lemonade + 1 * fruit_juice <= 100, "Water"

    # Обмеження для цукру: 1 од. на лимонад <= 50
    model += 1 * lemonade <= 50, "Sugar"

    # Обмеження для лимонного соку: 1 од. на лимонад <= 30
    model += 1 * lemonade <= 30, "Lemon"

    # Обмеження для фруктового пюре: 2 од. на сік <= 40
    model += 2 * fruit_juice <= 40, "Sauce"

    return model


def solve_and_print_results(model: pulp.LpProblem) -> None:
    """
    Розв'язує модель та виводить результати.

    Args:
        model (pulp.LpProblem): Модель для розв'язання
    """
    # Розв'язання моделі
    model.solve()

    # Отримання змінних з моделі та їх значень
    variables = {var.name: var.varValue for var in model.variables()}
    lemonade = variables['lemonade']
    fruit_juice = variables['fruit_juice']

    # Перевірка використання ресурсів
    water_used = 2 * lemonade + fruit_juice
    sugar_used = lemonade
    lemon_used = lemonade
    sauce_used = 2 * fruit_juice

    # Вивід результатів
    print("\nРезультати оптимізації:")
    print("=" * 50)
    print("Для максимізації загальної кількості продуктів необхідно виробляти:")
    print(f"Лимонад: {int(lemonade)} од.")
    print(f"Фруктовий сік: {int(fruit_juice)} од.")
    print(f"Загальна кількість продукції: {int(lemonade + fruit_juice)} од.")
    print("=" * 50)

    # Вивід використання ресурсів
    print("\nВикористання ресурсів:")
    print(f"Вода: {int(water_used)}/100 од.")
    print(f"Цукор: {int(sugar_used)}/50 од.")
    print(f"Лимонний сік: {int(lemon_used)}/30 од.")
    print(f"Фруктове пюре: {int(sauce_used)}/40 од.")


def main():
    """
    Головна функція програми.
    """
    # Створення та розв'язання моделі
    model = create_production_model()
    solve_and_print_results(model)


if __name__ == "__main__":
    main()
