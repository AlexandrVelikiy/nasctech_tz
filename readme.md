## Для запуска 
    docker-compose up  --build

Работает таким образом:
- если список data длинее списка rule - обрабатывается количестов данных равное количеству правил, остальные данные игнорируются  
- если список data короче списка rule - обрабатывается весь список данных
- если есть некорректные значения rule - даные которые должны были ним обработаны игнорируются (последний пример)  

# Проверял (Ubuntu 18.04):
## httpie

    http get http://0.0.0.0:5000/start data=11,12,3,4,5.5,7,8,9,11 rule=f,c,d,a,a,a

    HTTP/1.0 200 OK
    Content-Length: 42
    Content-Type: application/json
    Date: Thu, 18 Mar 2021 22:25:49 GMT
    Server: Werkzeug/0.16.1 Python/3.7.10
    
    {
        "result": [
            5.5,
            11.0,
            0.3,
            16.0,
            30.25,
            49.0
        ]
    }

## браузер

    http://0.0.0.0:5000/start?data=11,12,3,4,5.5,7,8,9,11&rule=f,c,d,e,b,f,a,b

    {"result":[5.5,11.0,0.3,14.0,12.0,3.5,64.0,19.0]}


### Пример с неправильным rule:
1. все правильные


    http get http://0.0.0.0:5000/start data=1,2,3,4,5 rule=a,b,c,d,e,f
    HTTP/1.0 200 OK
    Content-Length: 34
    Content-Type: application/json
    Date: Thu, 18 Mar 2021 22:37:22 GMT
    Server: Werkzeug/0.16.1 Python/3.7.10
    
    {
        "result": [
            1.0,
            5.0,
            2.0,
            0.4,
            15.0
        ]
    }

2. есть неправильное 'q'
   

    http get http://0.0.0.0:5000/start data=1,2,3,4,5 rule=a,b,q,d,e,f
    HTTP/1.0 200 OK
    Content-Length: 30
    Content-Type: application/json
    Date: Thu, 18 Mar 2021 22:38:26 GMT
    Server: Werkzeug/0.16.1 Python/3.7.10
    
    {
        "result": [
            1.0,
            5.0,
            0.4,
            15.0
        ]
    }
