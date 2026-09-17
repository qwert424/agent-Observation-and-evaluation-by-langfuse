from langfuse import Evaluation
from ai_eval.utils.create_model import create_model
from ai_eval.benchmarks.evaluators.schemas import EvaluationResult
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.messages import HumanMessage


def create_score_evaluator(prompt_template, evaluator_name):

    async def content_similarity(
        *, input: str, output: str, expected_output: str, **kwargs
    ):
        if not output:
            return Evaluation(
                name=evaluator_name,
                value=0,
                comment="没有实际输出",
                data_type="NUMERIC",
            )
        model = create_model()
        agent = create_agent(
            model=model, response_format=ToolStrategy(EvaluationResult)
        )

        prompt = prompt_template.format(
            input=input, output=output, expected_output=expected_output
        )
        result = await agent.ainvoke(input={"messages": [HumanMessage(prompt)]})
        score = result["structured_response"].score
        reason = result["structured_response"].reason
        return Evaluation(
            name=evaluator_name, value=score, comment=reason, data_type="NUMERIC"
        )

    return content_similarity
