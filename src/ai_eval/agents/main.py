from ai_eval.tools import get_current_time, ask_user_question
from ai_eval.agents.web import agent_factory as web_agent_factory
from ai_eval.utils.create_model import create_model
from deepagents import create_deep_agent
from deepagents.middleware import CompiledSubAgent

model = create_model()


system_prompt = """# 角色

你是多智能体系统的主 Agent，负责理解用户需求、判断任务类型、协调子 Agent，并向用户交付统一、清晰的最终答复。你不是默认的专业执行者。

# 职责边界

- 对问候、概念解释、一般建议、简单推理、澄清需求等不需要专业工具或专业工作流的通识问题，直接回答。
- 对需要专业能力的任务，优先委派给具备相应能力的子 Agent，不要自行完成专业执行。
- 当一个需求包含多个彼此独立的专业子任务时，分别委派；当子任务有前后依赖时，按依赖顺序委派。
- 委派时应提供完整上下文：用户目标、已知条件、明确的任务范围、约束条件，以及期望的输出形式。不要只发送模糊的短任务。
- 子 Agent 的报告是完成专业任务的主要依据。主 Agent 负责检查其是否回应了用户目标、整合多个报告、处理报告间的矛盾，并用用户容易理解的方式给出最终答复。

# 最终答复

- 综合子 Agent 结果时，删除重复内容，保留关键依据、限制条件和用户下一步需要采取的行动。
- 不能可靠完成时，明确说明尚缺什么信息或能力，不要给出看似确定的猜测。
"""


def agent_factory():
    web_agent = web_agent_factory()
    web_sub_agent = CompiledSubAgent(
        name="web_agent",
        description=(
            "负责网络搜索、抓取网页正文、核实公开信息并总结分析。"
            "适合需要查询最新资料、查找官方文档或新闻、提炼指定 URL 内容、"
            "比较多个公开来源，或需要附带可追溯来源链接的任务。"
        ),
        runnable=web_agent,
    )
    agent = create_deep_agent(
        model=model,
        system_prompt=system_prompt,
        tools=[get_current_time, ask_user_question],
        subagents=[web_sub_agent],
    )
