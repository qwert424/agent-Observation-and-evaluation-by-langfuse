from langfuse.api import DatasetItem
from langfuse import get_client
from ai_eval.benchmarks.dataset import get_items

langfuse = get_client()


async def experiment_task(*, item: DatasetItem, **kwargs):
    return item.expected_output


def run_experiment(name: str, dataset_name: str, description: str | None = ""):
    items = get_items(dataset_name)
    # 运行实验
    langfuse.run_experiment(
        # 给实验取个名字
        name=name,
        # 如果不配置，则使用name+当前时间自动生成
        run_name=None,
        description=description,
        # 此次实验针对哪些数据项
        data=items,
        task=experiment_task,  # type: ignore
    )
