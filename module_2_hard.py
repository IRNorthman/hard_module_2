def result():
    code_ = ""
    for i in range (1, first_num+1):
        for j in range (i+1, first_num+1):
            if first_num % (i + j) == 0 and i < first_num/2 and i != j:
                code_ += str(i)+str(j)
            else:
                continue
    print (code_)

print ('Введите число от 3 до 20:')
first_num = int(input ())
result()