
f = '''Процессор компьютера работает только с числами,
причем представленными в двоичном 2 формате (с битами). вспомним, что бит — это минимальная единица
информации в памяти компьютера. которая может принимать. только одно из двух значений: ноль или. единицу
 соответственно. все 5 данные (числовые, 4 текстовые. видео,
аудио-информация, изображения). хранимые и обрабатываемые 6 компьютером, это последовательность нулей
и единиц.'''

# masf = f.split('. ')
# print(masf)
# newmas = []
# for i in masf:
#     newmas.append(i.capitalize())
#
# print(newmas)
# f = '. '.join(newmas)
# # print(f)
# import time
# start = time.time()
# s = '*'
# for i in range(1000):
#     s+='*'
#     print(s)
# for i in range(1000):
#     for i in range(10):
#         s+='*'
#         print(s)
# end = time.time()-start
# print(end)
# #два цикла увеличивают время в 2 раза
# #цикл в цикле увеличивает время в х раз
def f1(lenght,sim,dir):
    if dir=='h':
        for i in range(lenght):
            print(sim,end='')
    elif dir=='v':
        for i in range(lenght):
            print(sim)
    pass
f1(8,'$','h')