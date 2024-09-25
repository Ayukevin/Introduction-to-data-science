term = [[2, {'X': 3}], [-1, {'X': 1, 'Y': 2}], [1, {'X': 1, 'Z': 1}], [4, {'Y': 1, 'X': 2}], [-2, {'Y': 3}], [2, {'Y': 1, 'Z': 1}]]
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

output_data = merge_lists(term)
print(output_data)

def dict_to_string(input_dict):
    # 用於儲存結果的列表
    result = []
    
    for key, value in input_dict.items():
        if value == 1:
            result.append(key)  # 僅添加變數名
        else:
            result.append(f"{key}^{value}")  # 添加格式化字符串
            
    # 將結果連接成字符串
    return ''.join(result)

output = []
for i in output_data:
    var = dict_to_string(i[1])
    coeffe = str(i[0])
    if coeffe =='1':
        output.append(var)
    elif coeffe == '-1':
        a = '-'+var
        output.append(a)
    else:
        a = coeffe+ "*" +var
        output.append(a)

print(output)

final_output = ''
for term in output:
    if term.startswith('-'):
        final_output += term
    else:
        if  final_output:
            final_output += '+' + term
        else:
            final_output += term

print(final_output)