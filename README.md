# Verbia CLI

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Sukitly/verbia/blob/main/README.md)
[![zh](https://img.shields.io/badge/lang-zh-green.svg)](https://github.com/Sukitly/verbia/blob/main/README.zh.md)
[![ja](https://img.shields.io/badge/lang-ja-yellow.svg)](https://github.com/Sukitly/verbia/blob/main/README.ja.md)

**Verbia CLI** is an open-source command-line tool for managing vocabulary lists to support your language learning
journey. Built with [Typer](https://typer.tiangolo.com/), Verbia CLI makes it easy to create, manage, and review
vocabulary collections. This app leverages LLMs (Large Language Models) to generate word definitions, helping learners
efficiently expand their vocabulary.

---

## Features

- **Manage Multiple Vocabularies**: Create, list, switch, and delete vocabularies for different languages.
- **Add Words with Definitions**: Quickly add new words to your vocabulary using LLM-generated definitions.
- **Review System**: Review words due for practice based on a spaced repetition strategy.
- **Rich Display**: Beautifully formatted word details and examples using `rich` for enhanced terminal output.
- **Configurable**: Manage app settings easily.

---

## Installation

Install **Verbia CLI** using `pip`:

```bash
pip install verbia-cli
````

---

## Usage

### Vocabulary Commands

#### List Vocabularies

```bash
verbia vocabulary list
```

#### Create a Vocabulary

```bash
verbia vocabulary create
```

You will be prompted to enter:

- The **name** of the vocabulary.
- The **language code** for the words (e.g., `en` for English).
- The **language code** for the native language (e.g., `es` for Spanish).

#### Switch Vocabulary

```bash
verbia vocabulary switch
```

Select a vocabulary from the list to set it as the current vocabulary.

#### Delete a Vocabulary

```bash
verbia vocabulary delete
```

Choose a vocabulary to delete.

### Word Commands

#### Add a Word

```bash
verbia word add <word>
```

Add a word to the current vocabulary. Definitions will be fetched and displayed.

#### Review Words

```bash
verbia word review
```

Review words due for practice. You will be asked to rate your recall (1-5).

#### Delete a Word

```bash
verbia word delete <word>
```

Delete a word from the current vocabulary.

### Config Commands

#### List Configuration

```bash
verbia config list
```

#### Set a Configuration

```bash
verbia config set <key> <value>
```

Set a configuration key to a new value.

---

## Example Workflow

1. **Create a Vocabulary**:
   ```bash
   verbia vocabulary create
   ```
    - Name: `spanish_vocab`
    - Word Language: `es`
    - Native Language: `en`

2. **Add Words**:
   ```bash
   verbia word add perro
   ```

3. **Review Due Words**:
   ```bash
   verbia word review
   ```

4. **Switch to Another Vocabulary**:
   ```bash
   verbia vocabulary switch
   ```

---

## Dependencies

- **Typer**: For building CLI interfaces.
- **Rich**: For rich text and table display.
- **Loguru**: For logging.
- **InquirerPy**: For interactive prompts.
- **Langcodes**: For language code validation.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Make changes and commit: `git commit -m "Add your feature"`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Submit a pull request.

---

## License

This project is licensed under the **MIT License**.

---

Happy learning with **Verbia CLI**! 🚀
