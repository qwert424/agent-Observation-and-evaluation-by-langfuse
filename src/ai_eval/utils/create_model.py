from langchain.chat_models import init_chat_model
from ai_eval.config.anthropic_settings import anthropic_settings


def create_model():
    model = init_chat_model(
        model=anthropic_settings.default_model,
        thinking={"type": "disabled"},
        model_provider="anthropic",
    )
    return model
