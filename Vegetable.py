from random import randint

class Vegetable :             
    #Словарь стадий зрелости
    states = {1:"Отсутствие",
              2:"Цветение",
              3:"Зеленый",
              4:"Красный"}

    def __init__(self,index) :
        #Индекс растения и его стадия зрелости
        self._index = index
        self._state = 0

    def grow(self) :
        #Переводит на следующую стадию созревания
        if self._state < 4:
            self._state += 1
            self.print_tomatoes()

    def print_tomatoes(self) :
        print(f"Овощь " + str(self._index) + " "+ str(Vegetable.states[self._state]))

    def is_ripe(self) :
        #Проверка зрелости
        if self._state == 4 :
            return True
        else :
            return False
        
class Tomato(Vegetable) :

    def __init__(self,variety) :
        self.variety = variety
        self.giv_variety()
        
    def giv_variety(self) :
        #Сообщает сорт помидора
        print("Сорт помидора: " + self.variety)
                
class TomatoBush :
    #Cловарь сортов помидоров
    varieties = {1:"Агата",
                 2:"Де Барао",
                 3:"Бычье сердце",
                 4:"Сливка"}

 
    def __init__(self,num) :
        #Определение помидора и кол-во кустов
        self.variety = TomatoBush.varieties[randint(1,4)]
        self.tomatoes = [Vegetable(index) for index in range(1,num+1)]

    def grow_all(self) :
        #Перевод списка на следующий этап созревания
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self) :
        #Возвращает True, если томаты стали спелыми
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self) :
        #Очистка списка после сборки урожая
        self.tomatoes = []

class Gardener :

    def __init__(self,name,plant) :
        #Динамические свойства принимают параметры tomato
        self.name = name
        self._plant = plant

    def work(self) :
        #Работа садовника
        print("Садовник " + self.name + " работает!")
        self._plant.grow_all()
        print("Садовник " + self.name + " закончил работать!")

    def harvest(self) :
        #Проверяет все ли плоды созрели
        if self._plant.all_are_ripe() :
            self._plant.give_away_all()
            print("Плоды созрели!")
        else :
            print("Плоды еще не созрели!")

    @staticmethod
    def knowledge_base() :
        #Вывод справки
        print("""        Harvest time for tomatoes should ideally occur
        when the fruit is a mature green and then allowed to ripen off
        the vine.This prevents splitting or bruising
        and allows for a measure of control over the ripening process.""")

if __name__ == '__main__' :
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener("Вася",great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
    variety = Tomato(great_tomato_bush.variety)
    
input()
