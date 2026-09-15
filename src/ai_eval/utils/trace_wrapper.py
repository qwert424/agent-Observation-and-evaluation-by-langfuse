from langfuse.langchain import CallbackHandler
from langchain_core.runnables import RunnableConfig
from langgraph_sdk.runtime import ServerRuntime
import ai_eval.config.langfuse_settings


def trace_wrapper(agent_factory):
    async def _trace(config: RunnableConfig, runtime: ServerRuntime):
        trace_handler = CallbackHandler()
        agent = await agent_factory()
        thread_id = config.get("configurable", {}).get("thread_id")
        assert runtime.user is not None
        agent = agent.with_config(
            callbacks=[trace_handler],
            metadata={
                "langfuse_session_id": thread_id,
                "langfuse_user_id": runtime.user.identity,
            },
        )
        return agent

    return _trace
