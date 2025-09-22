**Для запуска необходим git, docker и curl**
## Скрипты
Запуск из корня проекта через bash (например, bash start.sh, для windows просто двойной клик на .bat файл)
- start.sh/.bat - запуск приложения с построением образа
- stop.sh/.bat - останавливает контейнер приложения без удаления образа
- remove.sh/.bat - останавливает контейнер, если он запущен и удаляет образ, очищая память
- rebuild.sh/.bat - скачивает актуальную версию приложения с git, пересобирает образ и запускает контейнер
## Использование (после запуска start.sh|.bat или rebuild.sh|.bat)
- **UI-версия** - запускается через браузер, вбив в поисковую строку http://localhost:8501
- **CLI-версия** - запускается командная строка, в ней используется<br> 
```
curl -X 'POST' \
  'http://localhost:2307/run_cli' \
  -F 'file=@path/to/file' \
  -F 'particle_type=he|p' \
  -F 'model_type=mlp|cnn'
```<br>, также можно зайти в браузере http://localhost:2307/docs и загрузить файл вручную<br>
***Результат обработки будет лежать с папке storage с тем же именем файла и в том же формате, но с полями p|he_bin_$номер_бина.***
## Формат датасетов
- Поля для моделей будущего: date, BRBG, MRNY, SOPO, THUL, TXBY, APTY, OULU, KERG, YKTK, MOSC, NVBK, LMKS, JUNG, AATB, MXCO, ATHN, PSNM, Ap, SSN, A
- Поля для моделей прошлого: date, BRBG, THUL, TXBY, APTY, OULU, KERG, YKTK, MOSC, NVBK, LMKS, JUNG, AATB, MXCO, ATHN, Ap, SSN, A
