# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, name, surname, middle_name):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name

    def get_official_name(self):
        official_name = self.surname + ' ' + self.name[0] + '. ' + self.middle_name[0] + '.'
        return official_name

    def get_full_name(self):
        full_name = self.name + ' ' + self.middle_name + ' ' + self.surname
        return full_name


class Student(Person):
    def __init__(self, name, surname, middle_name, parents, class_room):
        Person.__init__(self, name, surname, middle_name)
        self.parents = parents
        self.class_room = class_room


class Teacher(Person):
    def __init__(self, name, surname, middle_name, subject):
        Person.__init__(self, name, surname, middle_name)
        self.subject = subject

class Class_room:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachers = teachers


teachers = [Teacher('Мария', 'Петрова', 'Валерьевна', 'математика'),
            Teacher('Людмила', 'Васильева', 'Евгеньевна', 'литература'),
            Teacher('Шурыгина', 'Нина', 'Николаевна', 'физика')
            ]

class_rooms = [Class_room('9 a', [teachers[0], teachers[1]]),
               Class_room('8 б', [teachers[0], teachers[2]],),
               Class_room('7 а', teachers[1])
               ]

parents = [Person('Валерий', 'Морозов', 'Алексеевич'),
           Person('Александра', 'Морозова', 'Сергеевна'),
           Person('Владимир', 'Панков', 'Александрович'),
           Person('Марьяна', 'Панкова', 'Робертовна'),
           Person('Антон', 'Самуйлов', 'Витальевич'),
           Person('Виктория', 'Самуйлова', 'Леонидовна')
           ]

students = [Student('Александр', 'Морозов', 'Валерьевич', [parents[0], parents[1]], class_rooms[0]),
            Student('Светлана', 'Панкова', 'Владимировна', [parents[2], parents[3]], class_rooms[1]),
            Student('Юрий', 'Самуйлов', 'Антонович', [parents[4], parents[5]], class_rooms[2]),
            ]

# 1. Получить полный список всех классов школы
print("Классы в школе:")
for cl in class_rooms:
    print(cl.class_room)

# 2. Получить список всех учеников в указанном классе
which_class_room = '8 б'
print("Ученики в классе {}:".format(which_class_room))
for st in students:
    if st.class_room.class_room == which_class_room:
        print(st.get_official_name())

# 3. Получить список всех предметов указанного ученика
which_student = 'Александр Морозов'
print("Предметы ученика {}:".format(which_student))
for st in students:
    if st.surname == which_student.split()[1] and st.name == which_student.split()[0]:
        for teacher in st.class_room.teachers:
            print(teacher.subject)

# 4. Узнать ФИО родителей указанного ученика
which_student = 'Александр Морозов'
print("ФИО родителей ученика {}:".format(which_student))
for st in students:
    if st.surname == which_student.split()[1] and st.name == which_student.split()[0]:
        for parent in st.parents:
            print(parent.get_full_name())

# 5. Получить список всех Учителей, преподающих в указанном классе
which_class_room = '8 б'
print("Учителя в классе {}:".format(which_class_room))
for cl in class_rooms:
    if cl.class_room == which_class_room:
        for teacher in cl.teachers:
            print(teacher.get_full_name())


