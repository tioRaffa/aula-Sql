'''
______//_____________//_____________//___________//


                                                                DATA
                                                                
CURENT_DATE(); -> data atual
CURRENT_TIME() -> hora atual
-

%d/%m%y %h:%m:%s

NOW()  data e hora atual              SELECT DATE_FORMAT(NOW(), '%d/%m/%y - %h:%m:%s');

-

MYSQL- DATE_ADD(CURRENT_DATE(), INTERVAL 5 DAY);  data vencimento
         data atual             /intervalo/

postgre- SELECT CURRENT_DATE + INTERVAL '3 DAY'; 

-

mysql- SELECT DATE_FORMAT(CURRENT_DATE(), '%d/%m/%y'); -> FORMATA A DATA PARA O PADRAO BRASILEIRO

----
SELECT DAYNAME(CURRENT_DATE());
SELECT DAYOFWEEK(CURRENT_DATE()); DIA SEMANA
SELECT DAYOFMONTH(CURRENT_DATE()); DIA DO MES
SELECT DAYOFYEAR(CURRENT_DATE()); DIA DO ANO


_________________________________________________________________________________



'''
