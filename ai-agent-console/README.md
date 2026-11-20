# AI Agent Console

A lightweight command-line tool written in Python that estimates token usage and approximate cost for your prompts, logs every session to a text file, and shows your saved chat history when you exit.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Why This Project?

When working with LLM APIs, cost is driven by tokens. This tool helps you understand how much a prompt might cost *before* it adds up, and keeps a simple record of each session for later review.

## Features

- **Token Estimation:** Estimates the approximate token count of each input message.
- **Cost Calculation:** Converts token usage into an estimated cost using a configurable price per 1,000 tokens.
- **Session Logging:** Appends each message and its usage details to a log file during the session.
- **History Review:** Reads and displays the saved chat history when you exit the console.
- **Zero Dependencies:** Runs on the Python standard library only.

## Requirements

- Python 3.8 or higher
- No external packages required

## Installation

```bash
git clone https://github.com/<your-username>/ai-agent-console.git
cd ai-agent-console
```

## Usage

```bash
python AI_Agent_Console.py
```

Type a message and press Enter to see its estimated tokens and cost. Type `exit` to quit and view your saved history.

> Adjust the exit command above to match your script.

## Example Session

```text
You: Explain what a transistor is in simple words.
Estimated tokens: 11
Estimated cost: $0.000022

You: exit
--- Chat History ---
[2026-11-19 10:32:05] Explain what a transistor is in simple words. | tokens: 11 | cost: $0.000022
```

> Replace this with the real output of your program once it works.

## How It Works

1. **Token estimation:** Tokens are approximated from text length (roughly 1 token per 4 characters of English text). This is an estimate, not an exact count, since real tokenizers vary by model.
2. **Cost calculation:** `cost = (tokens / 1000) * price_per_1k_tokens`
3. **Logging:** Each entry is appended to the log file so that history persists between sessions.
4. **Exit:** On exit, the log file is read and printed back to the terminal.

## Configuration

| Setting | Description | Default |
|---|---|---|
| `PRICE_PER_1K_TOKENS` | Price used for cost estimation | `[set your value]` |
| `LOG_FILE` | File where session logs are stored | `[your log filename]` |

## Project Structure

```text
ai-agent-console/
├── AI_Agent_Console.py   # Main CLI application
├── README.md             # Project documentation
└── chat_log.txt          # Generated log file (created at runtime)
```

## Limitations

- Token counts are approximations and may differ from the exact count used by a specific model's tokenizer.
- Cost is an estimate based on the price you configure, not a billing record.

## Roadmap

- [ ] Add timestamps to every log entry
- [ ] Use `tiktoken` for more accurate token counting
- [ ] Connect to a real LLM API (e.g., Claude API) and use actual usage data from the response
- [ ] Export logs as JSON or CSV
- [ ] Add unit tests with `pytest`

## Contributing

Suggestions and pull requests are welcome. Please open an issue first to discuss major changes.

## License

This project is licensed under the MIT License.

## Author

**[Belayet Hosen]**
ECE graduate | Python developer
· [GitHub](https://github.com/Shuvo1602153)