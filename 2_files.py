"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    file_read = ''
    with open('referat.txt', 'r', encoding='utf-8') as fr:
        file_read = fr.read()
    print(f"Длина всего исходного файла: {len(file_read)}")
    sum_words = file_read.replace(',', ' ')
    sum_words = len(sum_words.replace('.', ' ').split())
    print(f"Всего слов в файле: {sum_words}")
    file_read = file_read.replace('.', '!')
    print(file_read)
    with open('referat2.txt', 'w', encoding='utf-8') as fw:
        fw.write(file_read)

if __name__ == "__main__":
    main()
