Написать функцию, которая на вход получает две строки. 
Обе строки в формате  "23:11" и означают текущее время в часах и минутах. Формат времени 24-часовой.
Значение часов варьируется от 00 до 23. Значение минут - от 00 до 59.

Первая строка показывает текущее время, а вторая - какое-то будущее время. Задача помощника - вернуть строку 
в том же формате, подсказывающую сколько часов и минут осталось до указанного времени.

Например:

На вход пришли строки "01:30" и  "22:45". Функция вернет строку "21:15" - то есть между половиной второго и 
без пятнадцати минут одиннадцать ровно 21 час и 15 минут.
На вход пришли строки "05:30" и "05:35". Функция вернет "00:05".

Гарантируется, что:

- строки всегда приходят в правильном формате, количество часов в правильных пределах, минут - тоже.
- вторая строка всегда означает будущее время, то есть количество либо минут, либо часов там больше.