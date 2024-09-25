def read():#拆解算式
    polynomial = input("pls enter the polynomial:")
    temp = polynomial.split(")")
    equation = []
    for f in temp:
        equation.append(f[1:]) #[0]would be'(', so need to remove
    equation.pop()
    return equation

def form(equation):#分解成可運算的list格式
    for k in range(len(equation)):
        a = []
        temp = equation[k].split("+")
        for i in range(len(temp)):
            d = temp[i].split("-")
            for j in range(1,len(d)):
                d[j] = '-'+d[j] #拆完負號把他加回去
            a.extend(d)
        equation[k] = a   
    return equation

 #拆解係數和指數
def decompose(coeffe,term):
    temp = []
    a = 0
    var ={}
    while a < len(term):
        if term[a] == "^":
            var[term[a-1]] = int(term[a+1])  # 左變數，右指數
            a += 2  # 手動調整 a 的值
        else:
            var[term[a]] = 1 
            a += 1  # 增加 a 以進入下一次迴圈
    a = {}
    for i,j in var.items():
        a[i] =j
        b =[coeffe,a]
    temp.extend(b)
    return(temp)

def seperate(equation):#將多項式拆解成[係數,{變數：指數}]的形式
    for i in range(len(equation)):
        for j in range(len(equation[i])):
            term = equation[i][j]
            if '*' in term:
                term = term.split('*')
                temp = decompose(int(term[0]),term[1])
                equation[i][j] =temp
            elif '-' in term:
                temp = decompose(-1,term[1:]) #負號不算
                equation[i][j] =temp
            else:
                temp = decompose(1,term)
                equation[i][j] =temp
    return equation

#計算
def merge_dictionaries(a, b):
    # 乘法運算，取第一項的數字
    first_number = a[0] * b[0]
    
    # 合併字典
    result_dict = a[1].copy()  # 創建 a 的字典副本

    for key, value in b[1].items():
        if key in result_dict:
            result_dict[key] += value  # 相加
        else:
            result_dict[key] = value  # 保留原來的值
    
    return [first_number, result_dict]

def caculate(term):
    for i in range(len(term)-1):
        temp = []
        for j in range(len(term[i])):#第一式
            for k in range(len(term[i+1])): #第二式
                a = merge_dictionaries(term[i][j],term[i+1][k]) #第一式的第j項與第k項相乘
                temp += [a]
        term[i+1] =temp #將新的計算結果放入第二式，下一個從第二式開始相乘第三式，以此類推
    return(term[-1])

def merge_lists(input_list):
    result_dict = {}
    
    for number, current_dict in input_list:
        # 使用 frozenset 來處理字典作為鍵
        dict_key = frozenset(current_dict.items())
        
        if dict_key in result_dict:
            result_dict[dict_key][0] += number  # 前面的數字相加
        else:
            result_dict[dict_key] = [number, current_dict]  # 新增到結果字典中
    
    # 將字典轉換為列表格式
    result_list = list(result_dict.values())
    return result_list

def dict_to_string(input_dict):    # 用於儲存結果的列表
    result = []
    for key, value in input_dict.items():
        if value == 1:
            result.append(key)  # 僅添加變數名
        else:
            result.append(f"{key}^{value}")  # 添加格式化字符串
    return ''.join(result)# 將結果連接成字符串

def merge(output_data):
    data = merge_lists(output_data)
    output = []
    for i in data:
        var = dict_to_string(i[1])
        coeffe = str(i[0])
        if coeffe =='1': #係數為一不顯示
            output.append(var)
        elif coeffe == '-1':
            a = '-'+var
            output.append(a)
        else:
            a = coeffe+ "*" +var
            output.append(a)

    final_output = ''
    for term in output:
        if term.startswith('-'):
            final_output += term
        else:
            if  final_output:
                final_output += '+' + term
            else:
                final_output += term
    return(final_output)

def main():
    output_data = merge(caculate(seperate(form(formula := read()))))
    print(output_data)

if __name__ == '__main__':
    main()