import requests

if __name__ == '__main__':
    # выполняем POST-запрос на сервер по эндпоинту predict с параметром json
    r = requests.post('http://localhost:5000/predict', 
                      json = [ 1.        ,  0.        ,  0.        ,  0.        ,  1.        ,
        1.        ,  0.        ,  0.        ,  0.        ,  1.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        , -1.47819726, -0.62904551, -0.42759792,  0.89894332,
        0.17344408,  0.45928347,  1.45391   ,  0.71696267,  1.32420212,
       -0.07035142,  0.59645792, -0.27582937, -0.26339964, -0.16331653,
       -0.24104711, -0.52144426, -0.09839575]
                      )
    # выводим статус запроса
    print(r.status_code)
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим результат на экран
        print('Стоимость недвижимости:', r.json()['prediction'], '$')
    else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        print(r.text)