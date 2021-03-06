# python_efficient_sorting
sorting algorithm with O(log(n)) memory cost

Я реализовал алгоритм эффективной быстрой сортировки, 
которая который тратит лишь log(n) дополнительной памяти на хранение контантных
переменных в процессе разбиения массива на подмассивы.

Так как предполагается осуществить сортировку по трем ключам,
необходимо расположить данные в том же порядке, в каком сравниваются
элементы, при чем, если в каком-то элементе необходим обратный 
порядок сравнения (запись с бОльшим значением должна стоять раньше), 
то этот элемент нужно записать с отрицательным значением.

Обработав так данные, можно просто решать задачу сортировки для массива 
списков из трех элементов. Вначале сравниваются первые элементы,
если они равны, то сравниваются вторые и т.д.

Сам алгоритм сортировки состоит из двух функций:
- Одна функция (quicksortEffective) выбирает опорный элемент, вызывает функцию сортировки 
и рекурсивно запускает себя вначале на подмассиве, все значения (записи) в
котором меньше опорного элемента (левая часть), после чего также 
рекурсивно запускает себя на подмассиве со значениями, бОльшими опорного элемента.

Опорный элемент выбирается по следующему принципу:
берутся первый, последний и центральный элемены подмассива из 
них берется медианное значение. На это тратится какое-то время процессора,
однако подобный подход позволяет избежать дополнительных рекурсий в случае,
если на вход будут подана киллер-последовательность, и среднее количество
разбиений будет стремиться к log(n).
Функция возвращает массив с отсортированными частями 
при базовом случае (если длина подмассива меньше двух),
и полностью отсортированный массив, после выхода из рекурсии.

- Вторая функция (sorter) получает на вход массив, границы подмассива, 
в котором нужно осуществить замены значений элементов, 
относительно значения опорного элемента вправо и влево.

Функция сохраняет первоначальные значения правого и левого указателя, 
для последующего рекурсивного вызова quicksortEffective для правого и левого подмассивов.
Дальше функция двигает указатели друг навстречу другу до тех пор, пока:
1. значения слева от левого указателя меньше значения опорного элемента;
2. значения справа от правого указателя больше значения опорного элемента;*
    *если значение левого указателя оказалось больше значения опорного элемента,
    а значение правого указателя оказалось меньше значения опорного элемента,
    то данные элементы меняются местами.
3. пункты 1 и 2 повторяются пока указатели не встретятся на одном элементе.

Данная функция возвращает массив, в котором элементы, большие опорного 
расположены с правой стороны от "места встречи" указателей, 
а элементы меньшие - с левой стороны.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

Из описания алгоритма видно, что он может сортировать массивы 
с любым количеством ключей (за исключением массивов, в которых часть 
ТЕКСТОВЫХ полей нужно отсортировать по возрастанию, а часть - по убыванию, 
в остальных случаях поможет замена знака) с использованием лишь 
log(n) дополнительной памяти.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

Временная сложность данного алгоритма в большинстве случаев равна O(n*log(n)).
В худшем случае сложность будет равна O(n^2), однако в данном алгоритме реализован
способ выбора опорного элемента, который в большой степени спасает от худшего варианта
(хотя и можно подобрать массив, в котором даже с этой защитой сложность будет 
равна O(n^2-n), что при пределе с n=>inf равна O(n^2), но случайно получить такой массив очень маловероятно).
С учетом выбора опорного значения способом, описанным выше,
общее число разбиений приближается к log(n), поэтому для n элементов число операций
равно O(n*log(n))

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

Данный алгоритм тратит O(n) памяти для хранения массива, O(log(n)) 
(*тут немного сомневаюсь, если ошибаюсь, прошу прояснить ревьюера)
памяти на временное хранение константных переменных, которая освобождается, когда
рекурсия доходит до конца каждой ветви дерева.
(что меньше O(n) на больших масштабах, и следовательно не принимается в расчет) 
и не тратит дополнительной памяти для хранения промежуточных массивов, 
так как меняет массив in-place.
