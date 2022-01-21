def get_cook_book(file_name):   
    with open(file_name, encoding='utf-8') as file:
        dishes = []
        res = []               
        for line in file:
            dishes.append(line.strip())
            quantity_ingridients = int(file.readline().strip())
            recept = [] 
            res_keys = ['ingredient_name', 'quantity', 'measure']          
            for ingridient in range(quantity_ingridients):
                recept.append(file.readline().strip().split('|'))
            file.readline()
            res.append(recept)

        cook_book_values = []
        for element in res:
            element_list = []
            for string in element:
                my_dict = dict(zip(res_keys, string))
                for num in my_dict.items():
                    my_dict['quantity'] = int(my_dict['quantity'])
                element_list.append(my_dict)
            cook_book_values.append(element_list)
            
        cook_book = dict(zip(dishes, cook_book_values))
    return cook_book


result = get_cook_book('readme.txt')
print(result)
                        
       