# AstrBot Config Manager

这是一个用于管理 AstrBot 配置的 Git 模板。它可以将您庞大的 `cmd_config.json` 拆分为多个模块进行精细化管理。

## 🚀 快速上手

1.  **Fork 本仓库**：点击右上角的 `Fork`。
2.  **设置为私有 (强烈建议)**：
    - 在您 Fork 后的仓库中，前往 `Settings` -> `General`。
    - 滚动到最下方的 `Danger Zone`，点击 `Change visibility` 改为 **Private**。
3.  **上传配置**：
    - 将您现有的 `cmd_config.json` 直接上传到仓库根目录并提交。
4.  **自动拆分**：
    - GitHub Actions 会检测到文件，自动运行拆分脚本，并将其移动到 `subconfigs/` 目录下，同时删除原始文件以保护您的隐私。
5.  **开始管理**：
    - 您可以在 `subconfigs/` 中按类别修改配置。
    - 修改提交后，`generated/` 目录下会自动生成合并后的完整配置。

## 📁 目录说明
- `subconfigs/`: 按功能拆分的配置片段。
- `instances/`: 定义实例（如 astrbot01 使用哪些片段）。
- `generated/`: **这是最终产物**，您可以直接将其下载/同步到服务器使用。

## 🛠 如何在服务器同步
在服务器上：
```bash
git clone <您的私有仓库地址>
```
之后只需 `git pull` 即可获取最新配置。
