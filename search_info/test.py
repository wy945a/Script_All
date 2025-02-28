import json

'''
查询防火墙策略中病毒防护拦截方式为空的数据
'''

def load_json_from_file(file_path):
    """
    从文件中加载JSON数据。

    :param file_path: JSON文件路径
    :return: 解析后的JSON数据
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("JSON data loaded successfully.")
        return data
    except json.JSONDecodeError as e:
        print(f"JSON decode error at position {e.pos}: {e.msg}")
        return None


def extract_names_with_non_null_virusdto(data):
    """
    提取所有对象中的name字段的值，并过滤掉virusDTO为null的对象。

    :param data: 解析后的JSON数据
    :return: 包含name字段值的列表
    """
    names = []
    if 'data' in data and 'data' in data['data']:
        for item in data['data']['data']:
            virusdto = item.get('virusDTO')
            name = item.get('name')
            if virusdto is None and name is not None:
                names.append(name)
    return names


def display_names(names):
    """
    显示提取的名字。

    :param names: 包含name字段值的列表
    """
    if names:
        print("Displaying names where virusDTO is not null:")
        for name in names:
            print(name)
    else:
        print("No entries found where virusDTO is not null.")


# 使用示例
file_path = 'dds.json'  # 替换为实际文件路径

# 加载JSON数据
data = load_json_from_file(file_path)

if data is not None:
    # 提取name字段的值并过滤掉virusDTO为null的对象
    names = extract_names_with_non_null_virusdto(data)

    # 显示提取的名字
    display_names(names)
else:
    print("Failed to load JSON data.")