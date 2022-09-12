def print_products(*args):
    counter = 0
    result = []
    for x in args:
        if isinstance(x,str) and not x=="":
            result.append(str(counter+1)+") "+x)
            counter = counter + 1

    if len(result) == 0:
        print("Нет продуктов")
        
    print(*result,sep='\n')

print_products([4], {}, 1, 2, {'Beegeek'}, '') 