# GIT - распределенная система контроля версий. 
# Это система для отслеживания и введения истории изменения файломб в вашем проекте 

# Репозиторий - хранилище вашего кода и истории его изменений 

# GITHub - веб сайт для размещения git-репозиториев и совместной разработки проектов.




# Команды Git
# 1. git init - она создает новый гит репозиторий локально на вашем пк

# 2. git commit - как только мы достигаем опреденного момента в разработке, тот тогда мы сохраняем и 
# комментируем измения(фиксация изменений в репо)
# git commit -m '<comment>'

# 3. git add - когда мы создаем или изменяем файлы, то при помощи этой команды мы загружаем все изменения 
# в локальное хранилище
# git add <название файла>
# git add .

# 4. git remote add - это команда для того чтобы связать ваш проект с удаленным 
# репозиторием(репо в гитхаб)
# git remote add <название подключение> <ссылка на репо>
# git remote add origin <url>

# 5. git push - после коммита изменений при помощи этой команды мы отправляем наши изменения 
# на удаленный  репозиторий
# git push <origin> <название ветки>

# ______________________________________________________________________________________________

# 6. git branch -  Ветки очень важны в git. При помощи веток несколько программистов могут работать 
# паралельно на одном и том же проекте. При помощи команды git branch мы можем создавать ,
# просмотривать или удалять ветки.
# Создание ветки : git branch <название ветки>
# Просмотр ветки : git branch или git branch --list
# Удаление ветки : git branch -d <название ветки>

# 7. git checkout - команда используется для работы в команде, она помогает переключаеться по веткам.
# git checkout <название ветки>

# Строчка ветки muha

# 8. git clone - команда которая создает не пустой локальный репозиторий который мы склонировали
# с удаленного репозитория в гибхаб 
# git clone <ссылка на репозиторий>

# 9. git pull - команда которая используется для загрузки изменений(обновлений) из удаленного 
# репозитория 
# git pull <origin> <branch>