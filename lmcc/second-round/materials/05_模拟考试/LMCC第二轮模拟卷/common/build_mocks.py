#!/usr/bin/env python3
"""Generate the three LMCC second-round mock directories from compact specs."""

from __future__ import annotations

import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

T1_STARTER = '''# -*- coding: utf-8 -*-
"""仅修改这两个函数；其余评测文件不可修改。"""


def build_system_prompt() -> str:
    # TODO：写明题目标准、噪声处理规则与严格 JSON 输出。
    return ""


def build_generation_parameters() -> dict:
    return {"max_new_tokens": 512, "do_sample": False, "enable_thinking": False}
'''

T2_STARTER = '''# -*- coding: utf-8 -*-
from typing import Dict, List
import torch


def compute_similarity(query_embedding: torch.Tensor, doc_embedding: torch.Tensor) -> float:
    # TODO：余弦相似度；注意零向量与 .item()。
    return 0.0


def retrieve_relevant_problems(query: str, problem_bank: List[Dict], embedding_model, tokenizer, top_k: int = 3, get_embedding_func=None) -> List[Dict]:
    # TODO：query embedding、逐项 cosine、降序 Top-K。
    return []


def build_user_message(problem: str, retrieved_problems: List[Dict]) -> str:
    # TODO：明确分隔当前问题和参考题。
    return problem


def build_system_prompt() -> str:
    # TODO：只输出 reasoning + answer 的 JSON；answer 仅数字字符串。
    return ""


def build_generation_parameters() -> dict:
    return {"max_new_tokens": 512, "do_sample": False, "enable_thinking": False}
'''

EVALUATE = '''#!/usr/bin/env python3
import sys
from pathlib import Path

MOCK_DIR = Path(__file__).resolve().parents[1]
ROOT = MOCK_DIR.parent
sys.path.insert(0, str(ROOT))
from common.mock_runner import main_for_mock

if __name__ == "__main__":
    raise SystemExit(main_for_mock(MOCK_DIR))
'''


MOCKS = [
    {
        "name": "Mock_01_2025同难度",
        "subtitle": "接近 2025 官方真题：数学作业批改 + 最小数学 RAG",
        "facts": [
            ("17 + 28", "45", "46"),
            ("90 - 37", "53", "52"),
            ("7 的平方", "49", "47"),
            ("180 ÷ 6 + 4", "34", "30"),
            ("(35 - 11) × 3", "72", "74"),
        ],
        "topics": [
            ("折扣", "折扣 原价80元 打七五折", "60", "80 × 0.75 = 60"),
            ("余数", "余数 除数5 商7 余数4", "39", "5 × 7 + 4 = 39"),
            ("面积", "面积 长方形 长6 宽4", "24", "6 × 4 = 24"),
            ("平均数", "平均数 3个数 12 18 21", "17", "51 ÷ 3 = 17"),
            ("单位换算", "单位换算 2升 毫升", "2000", "2 × 1000 = 2000"),
        ],
        "rag": [
            ("折扣：原价120元，打八折后是多少？", "96", 0),
            ("余数：除数6，商9，余数5，被除数是多少？", "59", 1),
            ("面积：长方形长9宽7，面积是多少？", "63", 2),
            ("平均数：三个数6、9、12的平均数是多少？", "9", 3),
            ("单位换算：1.5升等于多少毫升？", "1500", 4),
            ("折扣：原价250元，打九折后是多少？", "225", 0),
        ],
    },
    {
        "name": "Mock_02_合理变式",
        "subtitle": "合理变式：应用题叙述变化，但保持 2025 的评测结构",
        "facts": [
            ("3 箱每箱 20 瓶", "60", "50"),
            ("72 ÷ 8", "9", "8"),
            ("25% 的 200", "50", "25"),
            ("120 公里用时 2 小时", "60", "120"),
            ("(40 - 16) ÷ 3", "8", "6"),
        ],
        "topics": [
            ("票价", "票价 3张 每张18元 服务费5元", "59", "3 × 18 + 5 = 59"),
            ("速度", "速度 距离120公里 时间2小时", "60", "120 ÷ 2 = 60"),
            ("工作量", "工作量 4人 3天 完成60页", "5", "60 ÷ 4 ÷ 3 = 5"),
            ("体积", "体积 长方体 长4宽3高2", "24", "4 × 3 × 2 = 24"),
            ("单价", "单价 5本书 总价75元", "15", "75 ÷ 5 = 15"),
        ],
        "rag": [
            ("票价：4张票每张15元，服务费6元，一共多少钱？", "66", 0),
            ("速度：180公里用3小时，平均速度是多少？", "60", 1),
            ("工作量：6人工作4天完成120页，每天每人完成多少页？", "5", 2),
            ("体积：长方体长5宽4高3，体积是多少？", "60", 3),
            ("单价：8本书总价96元，每本多少元？", "12", 4),
            ("票价：2张票每张30元，服务费4元，一共多少钱？", "64", 0),
        ],
    },
    {
        "name": "Mock_03_最终冲刺",
        "subtitle": "最终冲刺：覆盖文本噪声、关系检索与严格输出的合理新考法",
        "facts": [
            ("18 + 18", "36", "35"),
            ("150 - 75", "75", "70"),
            ("12 的平方", "144", "124"),
            ("210 ÷ 5", "42", "40"),
            ("(31 - 10) × 4", "84", "80"),
        ],
        "topics": [
            ("比例", "比例 3份对应45个 总数5份", "75", "45 ÷ 3 × 5 = 75"),
            ("折扣", "折扣 原价100元 打八折", "80", "100 × 0.8 = 80"),
            ("平均数", "平均数 4个数 8 10 12 14", "11", "44 ÷ 4 = 11"),
            ("余数", "余数 除数8 商6 余数3", "51", "8 × 6 + 3 = 51"),
            ("容量", "容量 0.75升 毫升", "750", "0.75 × 1000 = 750"),
        ],
        "rag": [
            ("比例：4份对应60个，总数7份是多少？", "105", 0),
            ("折扣：原价360元，打七五折后是多少？", "270", 1),
            ("平均数：4个数9、11、13、15，平均是多少？", "12", 2),
            ("余数：除数10，商9，余数6，被除数是多少？", "96", 3),
            ("容量：1.25升等于多少毫升？", "1250", 4),
            ("折扣：原价90元，打九折后是多少？", "81", 1),
        ],
    },
]


def write_jsonl(path: Path, records) -> None:
    path.write_text(
        "".join(json.dumps(record, ensure_ascii=False) + "\n" for record in records),
        encoding="utf-8",
    )


def make_t1_cases(prefix: str, facts):
    patterns = (
        [True, True, True, True, True],
        [False, True, False, True, False],
        [True, False, True, False, True],
        [False, False, True, True, False],
        [True, True, False, False, True],
    )
    cases = []
    expected = []
    for index, judgments in enumerate(patterns, 1):
        lines = []
        for number, ((question, correct, wrong), is_correct) in enumerate(zip(facts, judgments), 1):
            answer = correct if is_correct else wrong
            if number % 2:
                rendered = f"我先写了草稿，最终答案是 {answer} 😄"
            else:
                rendered = f"答案：{answer}（过程里有无关数字）"
            lines.append(f"题目{number}：{question}\n{rendered}")
        case_id = f"{prefix}-t1-{index}"
        cases.append({"id": case_id, "student_id": f"student_{index:03d}", "content": "\n\n".join(lines)})
        expected.append({"id": case_id, "student_id": f"student_{index:03d}", "judgements": judgments})
    return cases, expected


def make_similarity_cases(prefix: str, topics):
    cases = []
    for topic_index, (topic, problem, _answer, _explanation) in enumerate(topics):
        for variant in range(1, 5):
            cases.append(
                {
                    "id": f"{prefix}-sim-{topic_index + 1}-{variant}",
                    "query": f"{topic} {problem} 同类变式 {variant}：请使用同类方法计算",
                    "expected_top_id": f"{prefix}-bank-{topic_index + 1}",
                }
            )
    return cases


def make_rag_cases(prefix: str, topics, rag):
    cases = []
    expected = []
    for index, (problem, answer, topic_index) in enumerate(rag, 1):
        case_id = f"{prefix}-rag-{index}"
        cases.append({"id": case_id, "problem": problem})
        expected.append(
            {
                "id": case_id,
                "expected_top_id": f"{prefix}-bank-{topic_index + 1}",
                "answer": answer,
            }
        )
    return cases, expected


def build_mock(spec: dict) -> None:
    mock_dir = ROOT / spec["name"]
    for relative in ("exam/T1", "exam/T2", "data", "evaluator", "answers/public", "answers/hidden"):
        (mock_dir / relative).mkdir(parents=True, exist_ok=True)

    prefix = spec["name"].split("_")[1].lower()
    t1_cases, t1_expected = make_t1_cases(prefix, spec["facts"])
    t2_similarity = make_similarity_cases(prefix, spec["topics"])
    t2_rag, t2_rag_expected = make_rag_cases(prefix, spec["topics"], spec["rag"])

    write_jsonl(mock_dir / "data" / "t1_public.jsonl", t1_cases[:2])
    write_jsonl(mock_dir / "answers" / "public" / "t1_expected.jsonl", t1_expected[:2])
    write_jsonl(mock_dir / "answers" / "hidden" / "t1_data.jsonl", t1_cases[2:])
    write_jsonl(mock_dir / "answers" / "hidden" / "t1_expected.jsonl", t1_expected[2:])

    bank = [
        {
            "id": f"{prefix}-bank-{index + 1}",
            "problem": problem,
            "answer": answer,
            "explanation": explanation,
        }
        for index, (_topic, problem, answer, explanation) in enumerate(spec["topics"])
    ]
    (mock_dir / "data" / "problem_bank.json").write_text(
        json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    write_jsonl(mock_dir / "data" / "t2_similarity_public.jsonl", t2_similarity[:10])
    write_jsonl(mock_dir / "answers" / "public" / "t2_similarity_expected.jsonl", t2_similarity[:10])
    write_jsonl(mock_dir / "answers" / "hidden" / "t2_similarity_data.jsonl", t2_similarity[10:])
    write_jsonl(mock_dir / "answers" / "hidden" / "t2_similarity_expected.jsonl", t2_similarity[10:])
    write_jsonl(mock_dir / "data" / "t2_rag_public.jsonl", t2_rag[:3])
    write_jsonl(mock_dir / "answers" / "public" / "t2_rag_expected.jsonl", t2_rag_expected[:3])
    write_jsonl(mock_dir / "answers" / "hidden" / "t2_rag_data.jsonl", t2_rag[3:])
    write_jsonl(mock_dir / "answers" / "hidden" / "t2_rag_expected.jsonl", t2_rag_expected[3:])

    raw_outputs = []
    for case, expected in zip(t1_cases, t1_expected):
        raw_outputs.append(
            {"section": "t1", "id": case["id"], "raw_output": json.dumps({"student_id": case["student_id"], "judgements": expected["judgements"]})}
        )
    for case, expected in zip(t2_rag, t2_rag_expected):
        raw_outputs.append(
            {"section": "t2", "id": case["id"], "raw_output": json.dumps({"reasoning": "按参考方法计算", "answer": expected["answer"]}, ensure_ascii=False)}
        )
    write_jsonl(mock_dir / "answers" / "reference_outputs.jsonl", raw_outputs)

    (mock_dir / "exam" / "T1" / "submission.py").write_text(T1_STARTER, encoding="utf-8")
    (mock_dir / "exam" / "T2" / "submission.py").write_text(T2_STARTER, encoding="utf-8")
    shutil.copyfile(ROOT / "common" / "reference_submission.py", mock_dir / "answers" / "reference_T1_submission.py")
    shutil.copyfile(ROOT / "common" / "reference_submission.py", mock_dir / "answers" / "reference_T2_submission.py")
    (mock_dir / "evaluator" / "evaluate.py").write_text(EVALUATE, encoding="utf-8")

    (mock_dir / "README.md").write_text(
        f"# {spec['name']}\n\n{spec['subtitle']}\n\n"
        "- 正式限时：3 小时。\n- 满分：100 分。\n"
        "- T1：5 名学生 × 5 判断 × 2 分 = 50 分。\n"
        "- T2：20 个相似度检索 × 1 分 + 6 个 RAG 输出 × 5 分 = 50 分。\n\n"
        "只修改 exam/T1/submission.py 和 exam/T2/submission.py。默认评测公开数据；加 --scope full 才会运行隐藏数据。\n\n"
        "运行：python evaluator/evaluate.py --outputs answers/reference_outputs.jsonl --scope full\n",
        encoding="utf-8",
    )
    (mock_dir / "exam" / "README.md").write_text(
        "# 考场说明\n\n仅修改 T1 与 T2 的 submission.py。先读评分器，再运行公开集；不要查看 answers/hidden。\n",
        encoding="utf-8",
    )
    (mock_dir / "answers" / "标准答案.md").write_text(
        "# 标准答案\n\n参考输出和隐藏答案均在当前 answers 目录。先完成 full scope 再打开本文件。\n",
        encoding="utf-8",
    )
    (mock_dir / "answers" / "解析.md").write_text(
        "# 解析\n\nT1 核心是文本中的最终答案提取和严格布尔 JSON。T2 核心是 cosine、降序 Top-K、RAG 消息边界和仅数字 answer。\n",
        encoding="utf-8",
    )


def main() -> None:
    for spec in MOCKS:
        build_mock(spec)
    print("已生成 3 套 LMCC 第二轮模拟卷")


if __name__ == "__main__":
    main()
