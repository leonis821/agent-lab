from agent import handle       
print("开始")
running = True
while running:
    cmd = input("> ")
    if not cmd.strip():
        continue
    result = handle(cmd)
    if result is None:
        running = False
    else: 
        print(result)
print("结束")