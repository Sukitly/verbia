# Verbia CLI

**Verbia CLI** 是一个开源命令行工具，用于管理词汇表，帮助您更高效地学习语言。基于 [Typer](https://typer.tiangolo.com/)
，Verbia CLI 可以轻松创建、管理和复习词汇集合。该工具利用大型语言模型（LLMs）生成单词定义，助您快速扩展词汇量。

---

## 功能特点

- **管理多个词汇表**：支持创建、列出、切换和删除不同语言的词汇表。
- **添加单词及定义**：快速添加新单词，自动生成定义。
- **复习系统**：基于间隔重复策略复习到期单词。
- **丰富显示**：使用 `rich` 优化终端输出，显示精美的单词详情和示例。
- **可配置**：轻松管理应用配置。

---

## 安装

使用 `pip` 安装 **Verbia CLI**：

```bash
pip install verbia-cli
```

---

## 使用方法

### 词汇表命令

#### 列出所有词汇表

```bash
verbia vocabulary list
```

#### 创建词汇表

```bash
verbia vocabulary create
```

系统将提示您输入：

- **词汇表名称**
- **单词语言代码**（例如：`en` 表示英语）
- **母语语言代码**（例如：`zh` 表示中文）

#### 切换词汇表

```bash
verbia vocabulary switch
```

选择要切换的词汇表。

#### 删除词汇表

```bash
verbia vocabulary delete
```

选择要删除的词汇表。

### 单词命令

#### 添加单词

```bash
verbia word add <单词>
```

向当前词汇表添加单词，系统将获取并显示单词定义。

#### 复习单词

```bash
verbia word review
```

复习到期单词，系统会询问您的记忆程度（1-5）。

#### 删除单词

```bash
verbia word delete <单词>
```

从当前词汇表中删除单词。

### 配置命令

#### 列出所有配置

```bash
verbia config list
```

#### 设置配置

```bash
verbia config set <键> <值>
```