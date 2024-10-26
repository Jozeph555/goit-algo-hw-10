# Обчислення визначеного інтеграла методом Монте-Карло

## Опис задачі

Розробити програму для обчислення визначеного інтеграла функції f(x) = x² на відрізку [0, 2] методом Монте-Карло та порівняти результати з точним значенням.

## Результати обчислень

### 1. Метод Монте-Карло

* Значення інтеграла: 2.667240
* Оцінка похибки: 0.001333

### 2. Метод quad з scipy

* Значення інтеграла: 2.666667
* Оцінка похибки: 0.000000

### 3. Аналітичне значення

* 2.666667

## Порівняльний аналіз

### Точність результатів

* Відносна похибка методу Монте-Карло: 0.021500%
* Відносна похибка методу quad: 0.000000%

## Висновки

1. Метод Монте-Карло показав досить хорошу точність для даної задачі (похибка близько 0.02%)
2. Метод quad з scipy дає практично точний результат
3. Для простих одновимірних інтегралів краще використовувати чисельні методи (як quad)
4. Метод Монте-Карло може бути корисним для:
    * Багатовимірних інтегралів
    * Складних областей інтегрування
    * Паралельних обчислень