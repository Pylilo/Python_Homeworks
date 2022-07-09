list1 = ['Куртка', 'Кошелек']
nothing = ''
lifo_fifo = str.lower(input("По какому принципу работаем? "))
if lifo_fifo == "lifo":


    item = input("Здравствуйте, что у Вас? ")
    while item != nothing:
        print("Спасибо за доброту")
        list1.append(item)
        item = input("Здравствуйте, что у Вас? ")

    
    while item == nothing:
        last_item = list1.pop()
        print("Возьмите, вот вам",last_item)
        item = input("Здравствуйте, что у Вас? ")




elif lifo_fifo == "fifo":

    item = input("Здравствуйте, что у Вас? ")
    while item != nothing:
        print("Спасибо за доброту")
        list1.append(item)
        item = input("Здравствуйте, что у Вас? ")

    
    while item == nothing:
        print(list1[0])
        del list1[0]
        item = input("Здравствуйте, что у Вас? ")




