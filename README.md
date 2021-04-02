# Python_DjangoFileApi

Excel file uploader API released on:
* Python - Django 3.1.7
* Rest - DjangorestfulFramework 3.12.4
* Excel Reader - XLRD 1.2.0 (__not use higher version!__)

For test:
* create Excel file with columns named __before__ and __after__ (for ex. file __test.xlsx__ contained in __media__ folder)
* fill that columns with Integer Numbers (ex: 1, 2, 3, 5 and etc.)
* run API using __python manage.py runserver__ in folder with __manage.py__
* start POSTMAN and insert your link from Console/Terminal/PowerShell (ex. http://127.0.0.1:8000) and add at end of link __/file/savefile__<br/>
(example: http://127.0.0.1:8000/file/savefile)
* change your method to POST and in __Body__ method to __form-data__
* use Key as File-mode and name it __uploadedFile__
* in value select your Excel file
* after this click on __SEND__ button and you will see name of your file in Response Window
* In Database will create new entry with:
  * fileId (in ex. "27")
  * fileName (in ex. "test.xlsx")
  * uploaded_date (in ex. "2021-04-02")
  * status (in ex. "Ready")
  * result (in ex. "before: removed 6")
  * processed_date (in ex. "2021-04-02")

If something goes wrong in database you see fileId (you ID), fileName (your file name), uploaded_date (date of uploaded) and status ('Uploaded') and meet an ERROR 
then you must check and repeat all steps again

> "Coding hard is not a way to resolve troubles"
