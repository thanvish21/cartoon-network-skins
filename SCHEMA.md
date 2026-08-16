# Hermes Skin Schema
Complete reference for all configurable skin keys. Every skin in this repo defines the full schema below.

## Top-Level Structure
```yaml
name: myskin          # Required. Must match filename.
description: Short description
colors: { ... }       # 28 color keys (hex strings)
spinner: { ... }      # 4 spinner keys (lists)
branding: { ... }     # 6 branding keys (strings)
tool_prefix: "┊"      # Character prefixed to tool output lines
tool_emojis: { ... }  # Per-tool emoji overrides
banner_logo: |        # Rich-markup ASCII art logo (replaces HERMES_AGENT banner)
banner_hero: |        # Rich-markup hero art (replaces caduceus art)
```

## Colors (28 keys)
| Key | What it colors |
|-----|----------------|
| `banner_border` | Panel border around startup banner |
| `banner_title` | Title text in banner |
| `banner_accent` | Section headers in banner |
| `banner_dim` | Muted text (separators, secondary labels) |
| `banner_text` | Body text (tool names, skill names) |
| `ui_accent` | General UI accent (highlights, active elements) |
| `ui_label` | UI labels and tags |
| `ui_ok` | Success indicators |
| `ui_error` | Error indicators |
| `ui_warn` | Warning indicators |
| `prompt` | Interactive prompt text |
| `input_rule` | Horizontal rule above input area |
| `response_border` | Response box border (ANSI escape) |
| `status_bar_bg` | Prompt/TUI status bar background |
| `status_bar_text` | Status bar default text |
| `status_bar_strong` | Status bar highlighted text |
| `status_bar_dim` | Status bar separators/muted text |
| `status_bar_good` | Healthy context/status indicators |
| `status_bar_warn` | Warning context/status indicators |
| `status_bar_bad` | High-usage context/status indicators |
| `status_bar_critical` | Critical context/status indicators |
| `voice_status_bg` | Voice status pill background |
| `completion_menu_bg` | Completion menu background |
| `completion_menu_current_bg` | Active completion row background |
| `completion_menu_meta_bg` | Completion metadata background |
| `completion_menu_meta_current_bg` | Active completion metadata background |
| `session_label` | Session label color |
| `session_border` | Session ID dim border color |

## Spinner (4 keys)
| Key | Type | Description |
|-----|------|-------------|
| `waiting_faces` | list of strings | Faces cycled while waiting for API |
| `thinking_faces` | list of strings | Faces cycled during model reasoning |
| `thinking_verbs` | list of strings | Verbs shown in spinner messages |
| `wings` | list of [left, right] | Decorative brackets around spinner |

## Branding (6 keys)
| Key | Description |
|-----|-------------|
| `agent_name` | Banner title and status display |
| `welcome` | CLI startup message |
| `goodbye` | Exit message |
| `response_label` | Response box header label |
| `prompt_symbol` | Symbol before user input |
| `help_header` | /help command header |

## Other Keys
| Key | Type | Description |
|-----|------|-------------|
| `tool_prefix` | string | Character prefixed to tool output lines |
| `tool_emojis` | dict | Per-tool emoji overrides `{tool_name: emoji}` |
| `banner_logo` | string | Rich-markup ASCII art logo |
| `banner_hero` | string | Rich-markup hero art |

Valid tool names: `terminal`, `web_search`, `read_file`, `write_file`, `search_files`, `execute_code`,
`browser_navigate`, `delegate_task`, `mixture_of_agents`, `memory`, `clarify`, `cronjob`, `process`, `todo`.

## Rich Markup
`banner_logo`, `banner_hero`, `welcome`, and `goodbye` all support Rich console markup:
```
[bold #FFD000]Gold bold text[/]
[dim #555555]Dimmed text[/]
[#FF0000]Red text[/]
```

## Inheritance
Missing values inherit from the `default` skin. You only need to define what you want to change.
