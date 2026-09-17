from ai_eval.benchmarks.evaluators.create_score_evaluator import create_score_evaluator

_NAME = "内容相似度"

_PROMPT = """你是一名客观的答案评估员。只评价实际输出对期望输出中关键内容的覆盖程度，给出 0 到 1 的分数。

评分原则：
1. 从期望输出中找出关键事实、步骤和要求，判断实际输出正确覆盖了多少。
2. 语义等价即可，不要求措辞、语序或格式相同。
3. 遗漏越多，分数越低；说反或说错的要点不能算作已覆盖。
4. 不因合理的补充内容扣分；本维度只看期望要点是否得到正确覆盖。
5. 只依据提供的内容评分，不自行补充事实。

分数参考：

- 1.0：所有关键要点均已覆盖。
- 0.75：仅有轻微遗漏。
- 0.5：约有一半关键内容被覆盖。
- 0.25：仅覆盖少量要点。
- 0.0：没有覆盖关键内容或实际输出为空。

请用一句话说明最重要的覆盖或遗漏情况。

用户输入：
{input}

期望输出：
{expected_output}

实际输出：
{output}"""

content_similarity = create_score_evaluator(_PROMPT, _NAME)
