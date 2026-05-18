# Redaction Policy

Load this reference before recording command output, environment details, logs, credentials-adjacent text, deployment notes, or private data.

## Never Record Raw Values

Do not write raw values for:

- API keys, access tokens, refresh tokens, OAuth secrets, and bearer tokens.
- Passwords, passphrases, cookies, session IDs, and one-time codes.
- Private keys, SSH keys, certificates with private material, and wallet seeds.
- Cloud credentials, database URLs with credentials, registry tokens, and service account JSON.
- Customer secrets, private personal identifiers, private dataset samples, and account recovery data.

## Safe Alternatives

| Sensitive Item | Safe Record |
| --- | --- |
| API key value | Variable name and `<REDACTED_API_KEY>`. |
| Password in command | Command shape with `<REDACTED_PASSWORD>`. |
| Private key block | `<REDACTED_PRIVATE_KEY_BLOCK>`. |
| Database URL with credentials | Host type, database name if safe, credential placeholder. |
| Private absolute path | Keep when needed for local continuity; otherwise replace user names with `<USER>` or use project-relative path. |

## Redaction Markers

Use explicit markers so future agents know something was intentionally removed:

- `<REDACTED_TOKEN>`
- `<REDACTED_PASSWORD>`
- `<REDACTED_SECRET>`
- `<REDACTED_PRIVATE_KEY>`
- `<REDACTED_COOKIE>`
- `<REDACTED_PERSONAL_DATA>`

## Command Output Policy

- Record command names, working directories, exit status, and concise summaries.
- Include exact error messages when they are needed to reproduce or debug.
- Remove secrets from stack traces, URLs, headers, and config dumps.
- Avoid copying complete environment dumps. Record selected safe variables only.

## If Safe Redaction Is Not Possible

Stop writing the raw record. Ask the user for permission to write a redacted summary, or record only a minimal note that sensitive content existed and where it can be found outside the project log.
