# 脱敏规则

写进度记录前先检查是否含敏感信息。

## 不要记录原文

- API 密钥、令牌、OAuth 密钥、Bearer 令牌；
- 密码、cookie、会话令牌、一次性验证码；
- 私钥、证书私有部分、钱包助记词；
- 带账号密码的数据库 URL 或服务地址；
- 客户隐私、个人敏感信息、私有数据样本。

## 替代写法

| 内容 | 写法 |
| --- | --- |
| API 密钥 | 变量名 + `<REDACTED_API_KEY>` |
| 密码 | `<REDACTED_PASSWORD>` |
| 私钥 | `<REDACTED_PRIVATE_KEY>` |
| cookie | `<REDACTED_COOKIE>` |
| 令牌 | `<REDACTED_TOKEN>` |
| 私有个人信息 | `<REDACTED_PERSONAL_DATA>` |

## 命令输出

- 只写命令、退出状态和摘要。
- 报错只有对后续调试必要时才摘录。
- 不复制完整环境变量。
- 不把凭据藏在 URL、请求头、堆栈里。

如果无法安全脱敏，就不要写原文，只写“存在敏感内容，未记录”。
