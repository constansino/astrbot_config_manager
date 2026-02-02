import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def build():
    ins_dir = os.path.join(BASE_DIR, "instances")
    sub_dir = os.path.join(BASE_DIR, "subconfigs")
    gen_dir = os.path.join(BASE_DIR, "generated")
    if not os.path.exists(gen_dir): os.makedirs(gen_dir)
    if not os.path.exists(ins_dir): return
    for f in os.listdir(ins_dir):
        if f.endswith('.json'):
            with open(os.path.join(ins_dir, f), 'r', encoding='utf-8') as jf: info = json.load(jf)
            merged = {}
            for folder, filename in info['components'].items():
                path = os.path.join(sub_dir, folder, filename)
                if os.path.exists(path):
                    with open(path, 'r', encoding='utf-8-sig') as sf: merged.update(json.load(sf))
            merged["config_version"] = 2
            with open(os.path.join(gen_dir, f"{info['name']}_cmd_config.json"), 'w', encoding='utf-8') as out:
                json.dump(merged, out, indent=4, ensure_ascii=False)
if __name__ == "__main__": build()
