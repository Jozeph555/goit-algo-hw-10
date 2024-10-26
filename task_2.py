"""
Модуль для обчислення визначеного інтеграла методом Монте-Карло та його порівняння
з точним значенням, отриманим за допомогою scipy.integrate.quad.
"""

import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np
from typing import Callable, Tuple


RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)


def f(x: float) -> float:
    """
    Визначає функцію f(x) = x^2

    Args:
        x (float): Вхідне значення x

    Returns:
        float: Значення функції x^2
    """
    return x ** 2


def monte_carlo_integration(func: Callable, a: float, b: float, n: int = 1000000) -> Tuple[float, float]:
    """
    Обчислює визначений інтеграл методом Монте-Карло.

    Args:
        func (Callable): Функція для інтегрування
        a (float): Нижня межа інтегрування
        b (float): Верхня межа інтегрування
        n (int): Кількість випадкових точок (за замовчуванням 1000000)

    Returns:
        Tuple[float, float]: (значення інтеграла, оцінка похибки)
    """
    # Знаходимо максимальне значення функції на відрізку [a,b]
    x_range = np.linspace(a, b, 1000)
    max_y = max(func(x_range))

    # Генеруємо випадкові точки
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, max_y, n)

    # Підраховуємо точки під кривою
    points_under = sum(y <= func(x))

    # Обчислюємо площу
    area = (b - a) * max_y * (points_under / n)

    # Оцінка похибки (стандартне відхилення)
    error = np.sqrt((area * (1 - points_under/n)) / n)

    return area, error


def plot_integration(func: Callable, a: float, b: float) -> None:
    """
    Створює візуалізацію функції та області інтегрування.

    Args:
        func (Callable): Функція для візуалізації
        a (float): Нижня межа інтегрування
        b (float): Верхня межа інтегрування
    """
    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = func(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = func(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
    plt.grid()
    plt.show()


def main():
    """
    Головна функція, яка виконує всі обчислення та порівняння.
    """
    # Визначення меж інтегрування
    a, b = 0, 2

    # Візуалізація
    plot_integration(f, a, b)

    # Обчислення методом Монте-Карло
    mc_result, mc_error = monte_carlo_integration(f, a, b)
    print(f"\nМетод Монте-Карло:")
    print(f"Значення інтеграла: {mc_result:.6f}")
    print(f"Оцінка похибки: {mc_error:.6f}")

    # Обчислення за допомогою scipy.integrate.quad
    quad_result, quad_error = spi.quad(f, a, b)
    print(f"\nМетод quad з scipy:")
    print(f"Значення інтеграла: {quad_result:.6f}")
    print(f"Оцінка похибки: {quad_error:.6f}")

    # Аналітичне значення (для x^2: інтеграл = x^3/3)
    analytical = (b**3 - a**3) / 3
    print(f"\nАналітичне значення: {analytical:.6f}")

    # Порівняння результатів
    mc_relative_error = abs(mc_result - analytical) / analytical * 100
    quad_relative_error = abs(quad_result - analytical) / analytical * 100

    print(f"\nВідносна похибка методу Монте-Карло: {mc_relative_error:.6f}%")
    print(f"Відносна похибка методу quad: {quad_relative_error:.6f}%")


if __name__ == "__main__":
    main()
