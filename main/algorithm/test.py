"""
@author Lucas
@date 2019/4/2 8:53
"""
persons = []
for person_number in range(30):
    new_person = {'name': 'fanfan', 'sex': 'boy', 'lover': '33'}
    persons.append(new_person);

for person in persons[0:3]:
    if person['name']=='fanfan':
        person['name'] = 'lili'
        person['sex'] = 'girl'
        person['lover'] = '33'

for person in persons[0:5]:
    print(person)
