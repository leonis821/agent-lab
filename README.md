# agent-lab

一个从零手写的 Agent 命令助手，用来理解 Agent 的核心机制。

## 这是什么

不依赖 LangChain 等框架，手写实现 Agent 的四个基本功：
主循环、工具分发、参数校验、异常处理。目的是搞清楚"框架到底替我做了什么"。

## 结构

| 文件 | 职责 |
|---|---|
| `tools.py` | 工具函数（`get_weather` / `get_calc`） |
| `agent.py` | 决策逻辑：`handle(cmd)` 判断该调用哪个工具，只 return 不 print |
| `cli.py` | 命令行界面：主循环 + 输入输出 |
| `decisions.md` | 设计决策记录（ADR） |

## 运行

```bash
python cli.py 
```   

## 设计决策

见 [decisions.md](decisions.md)

## 支持的命令

| 命令 | 说明 |
|---|---|
| `/weather <城市>` | 查询天气（当前返回模拟数据） |
| `/calc <算式> [算式...]` | 计算，支持一次传多个算式 |
| `/history` | 查看本次会话输入过的命令 |
| `/quit` | 退出 |