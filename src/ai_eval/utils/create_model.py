from langchain.chat_models import init_chat_model
from ai_eval.config.anthropic_settings import anthropic_settings


def create_model(**kwargs):
    config = {
        "model": anthropic_settings.default_model,
        "thinking": {"type": "disabled"},
        "model_provider": "anthropic",
    }
    config.update(kwargs)

    model = init_chat_model(**config)
    return model
