# Функция, которая загружает и предобрабатывает данные 
def get_data():
    
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        
    # Массив обрезается по количеству записей, указанному в первой строке
    lines = lines[1 : int(lines[0]) + 1]
    # Далее каждая запись разбивается на значения:
    # первым идет количество решенных заданий с отрицательным знаком
    # за ним идет сумма штрафа, и в конце ID конкурсанта
    array = list(map(lambda x: [-int(x[1]), int(x[2]), x[0]], 
                     map(lambda x: x.split(' '), lines)))
    
    return array


# Функция, меняющая местами значения, относительно опорного элемента
def sorter(array, pivot, left, right):
    
    # Сохраняем значения правого и левого указателя
    start_left = left
    start_right = right

    # До тех пор, пока указатели не встретятся
    # выполняем порядок действий расписанный в принципе работы алгоритма
    while right > left:
    	while array[left] < pivot:
        	left += 1
    	while array[right] > pivot:
        	right -= 1
    	array[left], array[right] = array[right], array[left]

    	# Так как left == right, чтобы не путать читающих код (для legacy, например),
    	# решил переименовать это значение в mid
    	mid = left

    return start_left, start_right, mid, array


def quicksort_effective(array, left, right):
    # Если длина подмассива меньше двух, возвращаем массив в неизменном виде
    if right - left < 2:  
        return array   
    
    # Иначе расситвыаем значение опорного элемента, согласно описанию
    else:
        pivots = [array[left], array[(right - left) // 2], array[right - 1]]
        
        if (pivots[0] > pivots[1]) and (pivots[1] > pivots[2]):
            pivot = pivots[1]
        elif (pivots[1] > pivots[2]) and (pivots[2] > pivots[0]):
            pivot = pivots[2]
        else:
            pivot = pivots[0]
        
        # Вызываем функцию, которая раскидает значения вправо и влево относительно опорного элемента
        start_left, start_right, mid, array = sorter(array, pivot, left, right - 1)
        
        # и рекурсивно вызываем функцию по очереди для правого и левого подмассива
        array = quicksort_effective(array, start_left, mid)
        array = quicksort_effective(array, mid + 1, start_right + 1)
        
        return array


# Получаем данные
array = get_data()
# и печатаем ID's в отсортированном порядке разделенные знаком переноса строки
print('\n'.join([x[2] for x in quicksort_effective(array,0,len(array))]))
