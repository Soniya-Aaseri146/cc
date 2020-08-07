dic = [{'first': '1'},
        {'second': '2'},
        {'third': '1'},
        {'four': '5'},
        {'five': '5'},
        {'six': '9'},
        {'seven': '7'}
        ]

u_value = set( val for dic in dic for val in dic.values())
print(u_value)