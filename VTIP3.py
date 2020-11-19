#1
fr=["Даниил", "Раниль", "Алсу", "Светална", "Александр", "Руслан"]
fr.sort()
print (fr)
#Идентификатор списка не изменился. 1 элемент - "Александр", 2 - "Алсу"

#2
me=("Даниил", "Ишмуратов" ,"19")
people = list(me)
print (people)
other1=("Иван","Иванов","99")
other2=("Наруто", "Марчак", "69")
other3=("Раниль","Нуртдинов","18")
others=other1+other2+other3
people=list(others)
people.sort()
print (people)

#3
s=0
fr=["Даниил","Алсу","Раниль","Светдага","Александр","Иван"]
poop=["Кирилл","Андрей","Роман","Даниил","Дмитрий","Иван","Артем","Максим","Михаил","Александр"]
for i in poop:
    if i in fr:
        s=s+1
print("Количество совпадений имен моих друзей с самыми популярными именами в России равно ", s)

#4
Shakespear="""She speaks:
O, speak again, bright angel! for thou art
As glorious to this night, being o'er my head
As is a winged messenger of heaven
Unto the white-upturned wondering eyes
Of mortals that fall back to gaze on him
When he bestrides the lazy-pacing clouds
And sails upon the bosom of the air."""

Ralph="""The new life to which he had been called opened pleasantly and increased in happiness and opportunity,
except for the sadness of bereavements, for, in the first few years,
his brilliant brothers Edward and Charles died, and soon afterward Waldo, his firstborn son,
and later his mother. Emerson had left traditional religion,
the city, the Old World, behind, and now went to Nature as his teacher, his inspiration.
His first book, "Nature," which he was meditating while in Europe, was finished here, and published in 1836.
His practice during all his life in Concord was to go alone to the woods almost daily,
sometimes to wait there for hours, and, when thus attuned, to receive the message to which he was to give voice.
Though it might be colored by him in transmission, he held that the light was universal."""

Shakespear_list=Shakespear.split()
Ralph_list=Ralph.split()

for i in Ralph_list:
    if i in Shakespear_list:
        print("общее слово = ",i)
    else:
        print("уникальное слово ",i)

#5
kort=("Даниил", "Раниль", "Алсу", "Светална", "Александр", "Руслан")
mas=["Даниил", "Раниль", "Алсу", "Светална", "Александр", "Руслан", "Евгений", "Алина", "Алеся"]
for i in mas:
    if i not in kort:
        print("Элемент, который есть в списке, но отсутствует в кортеже ", i)
print()

#6
info =  {'name':"Daniil", 'surname':"Ishmuratov", 'age':19}
print("Информация обо мне:")
print(info)
print()

#7
phone = {}
phone['name']='Redmi note'
phone['memory']='64 Gb'
phone['size']=6.53
phone['number']=88005553535
print("Информация о телефоне:")
print(phone)
print()

#8
count=0
c={}
text="""She speaks:
O, speak again, bright angel! for thou art
As glorious to this night, being o'er my head
As is a winged messenger of heaven
Unto the white-upturned wondering eyes
Of mortals that fall back to gaze on him
When he bestrides the lazy-pacing clouds
And sails upon the bosom of the air."""
text=text.split()
for i in text:
    for j in text:
        if i == j:
            count=count+1
            c[i]=(count)
    
    count=0
    
print("подсчет повторений каждого слова в абзаце")
print(c)
print()
    
#9
Ralph="""The new life to which he had been called opened pleasantly and increased in happiness and opportunity,
except for the sadness of bereavements, for, in the first few years,
his brilliant brothers Edward and Charles died, and soon afterward Waldo, his firstborn son,
and later his mother. Emerson had left traditional religion,
the city, the Old World, behind, and now went to Nature as his teacher, his inspiration."""
Ralph=Ralph.split()
slovar={}
for i in Ralph:
    for j in Ralph:
        if i == j:
            count=count+1
            slovar[i]=(count)
    count=0
print(slovar)
print()

#10
count=0
anagram=['город', "дорог", "мир", "рим", "огонь", "лоб", "мышь"]
for i in anagram:
    for j in anagram:
        if i==j[::-1]:
            print("Анаграмма встречающаяся в списке слов: ",i)













