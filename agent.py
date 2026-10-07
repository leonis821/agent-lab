from tools import get_weather,get_calc
history = []
def handle (cmd):
    cmd_parts = cmd.split()
    history.append(cmd)
    resq = cmd_parts[0]
    if resq == "/weather":
        if len(cmd_parts) >= 2:
            city=" ".join(cmd_parts[1:])
            return get_weather(city)

        else:
            return "需要输入指令和所需城市（/weather 上海）"
    elif resq =="/history":
        return "\n".join(history)

    elif resq == "/calc":
        results=[]
        if len(cmd_parts)>=2:
            for expr in cmd_parts[1:]:
                 results.append(get_calc(expr))
            return "\n".join(results)
        else:
            return "请输入算式"

    elif resq == "/quit":
        return None
    else:
        return "指令错误"
