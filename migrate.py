import json
import os

def migrate():
    config_file = "cmd_config.json"
    if not os.path.exists(config_file): return
    with open(config_file, 'r', encoding='utf-8-sig') as f: config = json.load(f)
    mapping = {
        "01_credentials": ["openai_api_key", "anthropic_api_key", "google_api_key", "gemini_api_key", "access_token", "api_key"],
        "02_models": ["model", "model_list", "provider", "endpoint", "url_proxy", "llm_source"],
        "03_core": ["bot_name", "admin_id", "command_prefix", "system_prompt", "persona"],
        "04_connectivity": ["host", "port", "ws_url", "use_https", "proxy"],
        "05_plugins": ["plugin_config", "plugins"]
    }
    for folder, keys in mapping.items():
        sub_cfg = {k: v for k, v in config.items() if any(key in k for key in keys)}
        if sub_cfg:
            os.makedirs(f"subconfigs/{folder}", exist_ok=True)
            with open(f"subconfigs/{folder}/default.json", 'w', encoding='utf-8') as sf:
                json.dump(sub_cfg, sf, indent=4, ensure_ascii=False)
    os.makedirs("instances", exist_ok=True)
    with open("instances/default.json", 'w', encoding='utf-8') as f:
        json.dump({"name": "astrbot01", "components": {folder: "default.json" for folder in mapping.keys()}}, f, indent=4, ensure_ascii=False)
    os.remove(config_file)
if __name__ == "__main__": migrate()
