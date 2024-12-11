# Verbia CLI

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Sukitly/verbia/blob/main/README.md)
[![zh](https://img.shields.io/badge/lang-zh-green.svg)](https://github.com/Sukitly/verbia/blob/main/README.zh.md)
[![ja](https://img.shields.io/badge/lang-ja-yellow.svg)](https://github.com/Sukitly/verbia/blob/main/README.ja.md)

**Verbia CLI** は語彙リストを管理するためのオープンソースのコマンドラインツールです。[Typer](https://typer.tiangolo.com/)
に基づいて構築され、語彙リストの作成、管理、復習を簡単に行えます。LLM（大規模言語モデル）を活用し、単語の定義を生成して効率的に語彙を増やせます。

---

## 機能

- **複数の語彙リストを管理**：異なる言語の語彙リストを作成、表示、切り替え、削除できます。
- **単語と定義の追加**：新しい単語を追加し、定義を自動生成。
- **復習システム**：間隔反復法に基づいて単語を復習。
- **リッチな表示**：`rich` を使用した美しいターミナル出力。
- **設定可能**：アプリの設定を簡単に管理。

---

## インストール

`pip` で **Verbia CLI** をインストール：

```bash
pip install verbia-cli
```

---

## 使い方

### 語彙リストのコマンド

#### 語彙リストを表示

```bash
verbia vocabulary list
```

#### 語彙リストを作成

```bash
verbia vocabulary create
```

プロンプトで以下を入力：

- **語彙リスト名**
- **単語の言語コード**（例：`en` は英語）
- **母語の言語コード**（例：`ja` は日本語）

#### 語彙リストを切り替え

```bash
verbia vocabulary switch
```

リストから切り替える語彙リストを選択します。

#### 語彙リストを削除

```bash
verbia vocabulary delete
```

削除する語彙リストを選択します。

### 単語のコマンド

#### 単語を追加

```bash
verbia word add <単語>
```

現在の語彙リストに単語を追加し、定義を表示します。

#### 単語を復習

```bash
verbia word review
```

復習する単語を提示し、記憶度（1-5）を尋ねます。

#### 単語を削除

```bash
verbia word delete <単語>
```

現在の語彙リストから単語を削除します。

### 設定のコマンド

#### 設定を表示

```bash
verbia config list
```

#### 設定を変更

```bash
verbia config set <キー> <値>
```