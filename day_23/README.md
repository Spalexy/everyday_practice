Сегодня пишем класс-пистолет :)

У объекта этого класса есть следующие публичные методы:

getMagazinesAmount() - возвращает количество магазинов. Изначально к пистолету дается 10 магазинов. Каждый магазин 
имеет 15 патронов.
getBulletsAmount() - возвращает количество патронов к пистолету. Изначально у пистолета 10 * 15 = 150 патронов.

takeAShot() - делаем выстрел. Если в магазине есть пули, становится на одну меньше. Если нет, сначала автоматически 
дергается функция reload(), затем происходит выстрел.
reload() - вставляем новый магазин в пистолет. Старый магазин выбрасывается вместе с пулями, если они в нем остались. 
Если у нас больше нет магазинов, кидается исключения OutOfMagazines()