#Задание 1
import requests

class Rate:
    def __init__(self, format_ = 'Valute'):
        self.format = format_
    
    def exchange_rates(self):
        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json() ['Valute']
    
    def max_valute_name(self):
        response = self.exchange_rates()
        a = -1
        b = ''
        for c in response.values():
            if c.get('Value')/c.get('Nominal') > a:
                a = c.get('Value')/c.get('Nominal')
                b = c.get('Name')
        return b
        
r = Rate()

print(r.max_valute_name())

#Задание 2
import requests

class Rate:
    def __init__(self, format_ = 'Valute', diff_ = 'False'):
        self.format = format_
        self.diff = diff_
    
    def exchange_rates(self):
        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json() ['Valute']
    
    def make_format (self, currency):
        response = self.exchange_rates()
        if currency in response:
            if self.format == 'full':
                return response[currency]
            if self.format == 'Value' and self.diff == 'False':
                return response[currency]['Value']
            if self.format == 'Value' and self.diff == 'True':
                return response[currency]['Value'] - response[currency]['Previous']
        return 'Error'
    
r = Rate(format_= 'Value', diff_= 'True')

print(r.make_format('USD'))

#Задание 3
from libs.Employer import Employer
class Designer(Employer):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)

    def check_if_it_is_time_for_upgrade(self):
        self.seniority += 1
#Не совсем понял задание: в условии сказано "Считайте, что при выходе на работу сотрудник уже имеет две премии и их количество не меняется со стажем ". То есть по дефолту у каждого есть 4 балла, 
# эти 4 балла только при первом грейде учивать надо или при последующих тоже (сделал как во втором случае)?
        if (self.seniority + 4)% 7 == 0:
            self.grade_up()
        return self.publish_grade()
    
alex = Designer('Алксандр', 0)

for i in range(20):
    alex.check_if_it_is_time_for_upgrade()