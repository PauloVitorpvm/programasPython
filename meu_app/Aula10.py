from datetime import date, time, datetime, timedelta

def trabalhando_com_data():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A/%B/%Y') #Convetendo datatime para string
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H: %M: %S')
    print(type(horario_str))
    print(horario_str)
    print(horario)

def trabalhando_com_datetime():
    data_atual = datetime.now()
    #data_atual_str = data_atual.strftime('%d/%m/%y %H:%M:%S')
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.year)
    print(data_atual.hour)
    print(data_atual.date())
    tupla_semana = ('segunda', ' terça', 'quarta', 'quinta', 'quinta', 'sexta', 'sabádo', 'domingo')
    print(tupla_semana[data_atual.weekday()])
    data_criada = datetime(2022, 3, 14, 15, 7, 50)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/m%/%Y %H: %M: %S')
    print(data_convertida)
    nova_data: datetime = data_convertida - timedelta(days=365)
    print(nova_data)

if __name__ == '__main__':
    #trabalhando_com_data()
    #trabalhando_com_time()
    trabalhando_com_datetime()