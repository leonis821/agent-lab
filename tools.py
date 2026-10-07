def get_weather(city):
    return f"{city},晴天,25°c"

def get_calc(expr):
    ALLOWED = "0123456789+-*/() ."
    for item in expr: 
        if item in ALLOWED:
            continue
        else:
            return "请输入合法数字"
    try:
         return str(eval(expr))
    except Exception as e:
        return f"算式有误：{e}"