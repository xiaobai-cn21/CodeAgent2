

test_task = {
    "task_id": "test_go_llm_001",
    "file_path": "agents/fix_execution_agent/main.go",
    "issues_by_priority": {
        "high": [
            {"language": "go", "file": "main.go", "type": "llm", "message": "请修复语法和风格问题"}
        ]
    }
}


import asyncio
from agents.fix_execution_agent.agent import FixExecutionAgent

async def main():
    agent = FixExecutionAgent(config={})
    result = await agent.process_task(test_task)
    print("\n=== 修复结果 ===")
    print(result)
    print("\n=== 修复摘要 ===")
    print(await agent.get_fix_summary(result))

if __name__ == "__main__":
    asyncio.run(main())