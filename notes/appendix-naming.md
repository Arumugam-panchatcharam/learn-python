# Appendix — Naming (Foundations)

Supplemental notes on naming conventions. Not part of the numbered lesson track, but useful before diving into code-heavy lessons.

## PEP 8 Naming Conventions

| Kind | Convention | Example |
|------|------------|---------|
| Variables | `snake_case` | `user_count` |
| Functions | `snake_case` | `calculate_total()` |
| Methods | `snake_case` | `get_user()` |
| Classes | `CapWords` | `UserAccount` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_RETRIES` |
| Modules | `snake_case` | `user_service.py` |
| Private (by convention) | leading `_` | `_internal_cache` |

## Common Mistakes

1. Abbreviating too aggressively — `usr_cnt` instead of `user_count`
2. Hungarian notation — `strName`, `intCount`
3. Misleading names — `get_user` that also deletes the user
4. Shadowing builtins — `list`, `dict`, `id`
5. Overly generic names — `data`, `info`, `temp`, `result`

## Best Practices

- Name functions after what they do, not how they do it
- Use verbs for functions and nouns for data
- Keep names searchable in larger scopes
- Rename when understanding changes
