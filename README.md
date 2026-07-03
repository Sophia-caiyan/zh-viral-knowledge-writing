# 中文高共鸣公众号长文 Skill

这是一个用于中文公众号长文写作的 Codex skill。它面向 AI、心理学、教练、职场和个人成长类选题，帮助用户从一个抽象观点出发，生成标题、副标题、标题合同、文章结构和正文。

它不是“模仿某个作者口吻”的模板，而是一套可执行、可检查、可复用的写作系统：

- 先找到具体读者和真实压力。
- 用标题建立正文必须兑现的合同。
- 用场景、冲突、反常识判断和实用方法推进文章。
- 用质量检查避免标题党、空泛套话和编造案例。

## 安装

从仓库根目录执行：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skill/zh-viral-knowledge-writing "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装后可以这样调用：

```text
Use $zh-viral-knowledge-writing to turn this topic into WeChat long-form titles, subtitle, title contract, and a full Chinese draft.
```

## 适用范围

适合：

- 公众号长文，建议 2000-3500 字。
- AI、心理学、教练、职场、个人成长、创作者教育和社会观察。
- 标题生成、文章改写、结构设计、开头优化、完整成稿和质量诊断。

不作为首版目标：

- 短内容平台笔记。
- 口播脚本。
- 学术论文。
- 新闻摘要。
- 品牌通稿。
- SEO 内容。

## 仓库结构

```text
skill/zh-viral-knowledge-writing/
  SKILL.md
  agents/openai.yaml
  references/
    title-system.md
    article-archetypes.md
    domain-adaptation.md
    quality-system.md
    style-examples.md
  scripts/lint_draft.py
evals/
  cases.json
  rubric.md
  README.md
research/
  corpus-method.md
  aggregate-findings.md
tests/
  test_lint_draft.py
```

## 标题系统

这个 skill 把标题当成“正文合同”，而不是写完文章后的包装。

每个推荐标题都会检查：

- 写给谁。
- 刺中什么情绪、冲突或代价。
- 提供什么反常识判断。
- 正文能否证明。
- 是否承诺了方法、答案或故事。

不能被正文兑现的标题会被降级或删除。

## 质量检查

保存草稿后可以运行：

```bash
python skill/zh-viral-knowledge-writing/scripts/lint_draft.py --title "文章标题" --input article.md --json
```

脚本只做确定性检查，例如：

- 套话开头。
- 报告式连接词。
- 占位符。
- 连续超长段落。
- 过多小标题或加粗。
- 高风险确定性表达。
- 用户指定禁用词。

标题是否真正兑现、心理学是否越界、案例是否可信，仍需要按 `references/quality-system.md` 做人工或模型自检。

## 评测

`evals/cases.json` 提供 24 个公开测试题，覆盖 AI、心理学和教练三个领域。`evals/rubric.md` 定义评分标准和发布门槛。

建议比较不同 skill 版本时：

1. 同一模型、同一工具权限、同一推理设置。
2. 每题每版本只生成一次。
3. 本地保存完整输出，不提交长文草稿。
4. 公开提交聚合分数和失败标签。

## 语料边界

这个仓库不包含原始文章、PDF 或大段摘录。

研究语料只用于提炼结构规律：标题钩子、开头方式、段落节奏、问句密度、文章原型、结尾机制等。公开仓库只保留聚合结论、合成示例、测试题和检查工具。

这样做有三个原因：

- 保护版权和原始材料。
- 避免 skill 依赖巨大上下文。
- 让 skill 学到可迁移机制，而不是复刻个人口癖。

## 核心原则

> 找到具体的人，抓住真实的痛，给出值得传播的判断，并用正文把标题承诺完整交付。
