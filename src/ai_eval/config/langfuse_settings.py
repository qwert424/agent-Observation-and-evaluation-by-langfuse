from ai_eval.config.base_settings import BaseSettingsWithEnv


class LangfuseSettings(BaseSettingsWithEnv):
    secret_key: str = ""
    public_key: str = ""
    base_url: str = ""

    model_config = {"env_prefix": "LANGFUSE_"}


langfuse_settings = LangfuseSettings()
