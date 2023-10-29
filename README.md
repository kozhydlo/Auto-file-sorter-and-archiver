# Сортування файлів та архівування

Цей проект включає в себе Python-скрипт, який допомагає сортувати файли у вказані каталоги залежно від їх розширень, а також створює архів з відсортованими файлами.

## Вимоги

Перед використанням цього проекту, вам потрібно встановити наступні бібліотеки:

- watchdog
- zipfile

Ви можете встановити їх за допомогою pip:

```bash
pip install watchdog
pip install zipfile
Використання
Скопіюйте ваші файли, які ви хочете сортувати, у каталог Trash.

Запустіть скрипт і виберіть режим:

Режим 1 (Sort): Скрипт буде слідкувати за змінами у каталозі Trash та автоматично сортувати файли за розширеннями у відповідні каталоги (Images, Video, Musik, Other).

Режим 2 (Archiving): Скрипт створить архів з відсортованими файлами та очистить каталоги.

Налаштування
Ви можете змінити шляхи каталогів, в які сортувати файли, змінивши змінні folger_trash, folger_images, folger_videos, folger_music, folger_other.

Важливо
Переконайтеся, що у вас є резервні копії важливих файлів перед використанням цього скрипту.

Не використовуйте цей скрипт для сортування файлів, які вам не належать або для яких ви не маєте відповідних прав.

Ліцензія
Цей проект поширюється під ліцензією MIT. Докладну інформацію щодо ліцензії можна знайти у файлі LICENSE.
