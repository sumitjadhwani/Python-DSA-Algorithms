---
description: Add a NeetCode problem (question + your solution) as a markdown file, then commit and push.
agent: build
---

Add the NeetCode problem discussed in this conversation to the repo.

Arguments: `$ARGUMENTS`
- `$1` = topic folder under `neetcode/` (snake_case, e.g. `two_pointers`, `array_hashing`). If omitted, infer it from the problem.
- `$2` = optional file name (snake_case, no extension). If omitted, derive it from the problem title (e.g. "Three Integer Sum" -> `three_integer_sum`).

Use the problem statement and the user's solution **from the conversation above** — do not invent or rewrite the solution.

Steps:
1. If `.opencode` or the target file is ambiguous, ask before writing.
2. Ensure the folder matches repo convention: lowercase, `snake_case`, no spaces or `&`.
3. Create `neetcode/<topic>/<name>.md` with this structure:
   - `# <Problem Title>`
   - NeetCode link on the line below, if the user provided one.
   - `## Question` followed by the problem statement, preserving examples and formatting.
   - `## My Solution` followed by a fenced `python` code block containing the user's exact code.
4. Read back the written file to confirm it is correct.
5. Show `git status` and `git diff` for the new file.
6. Commit with a short lowercase message matching repo style, e.g. `added <topic> <problem>`, then `git push`.

Do NOT commit anything other than the new problem file unless the user asks.
