import json
import os

def calculate_stars(project_count):
    if project_count == 0: return "⚪⚪⚪⚪⚪ (Level 0 - Newbie)"
    elif project_count <= 2: return "⭐⚪⚪⚪⚪ (Level 1 - Apprentice)"
    elif project_count <= 5: return "⭐⭐⚪⚪⚪ (Level 2 - Junior)"
    elif project_count <= 10: return "⭐⭐⭐⚪⚪ (Level 3 - Developer)"
    elif project_count <= 20: return "⭐⭐⭐⭐⚪ (Level 4 - Senior)"
    else: return "⭐⭐⭐⭐⭐ (Level 5 - Master)"

def update_readme():
    # Dosya yollarını garantiye alalım
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'data.json')
    readme_path = os.path.join(base_dir, 'README.md')

    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    stats_markdown = f"""
| Skill Class | Stars | Rank |
| :--- | :--- | :--- |
| **🐍 Python** | {calculate_stars(data['stats']['Python'])} | |
| **🧠 AI Engineering** | {calculate_stars(data['stats']['AI_Engineering'])} | |
| **🔬 Data Science** | {calculate_stars(data['stats']['Data_Science'])} | |
| **🏗️ Data Engineering** | {calculate_stars(data['stats']['Data_Engineering'])} | |
| **✨ Vibe Coding** | ⭐⭐⭐⭐⭐ (Max) | *Flow State Master* |
"""

    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    start_marker = ""
    end_marker = ""
    
    # İşaretçilerin ham konumunu bul
    s_loc = readme_content.find(start_marker)
    e_loc = readme_content.find(end_marker)

    if s_loc != -1 and e_loc != -1:
        # Başlangıç okunun hemen sonrasını hesapla
        insert_point = s_loc + len(start_marker)
        
        # Yeni içeriği araya yerleştir (Eski içerik + Tablo + Kalan Kısım)
        new_content = readme_content[:insert_point] + "\n" + stats_markdown + "\n" + readme_content[e_loc:]
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ README başarıyla güncellendi! Tablo doğru yere yerleştirildi.")
    else:
        print("❌ HATA: İşaretçiler (STATS_START / STATS_END) README dosyasında bulunamadı!")
        print("Lütfen README.md dosyanızda bu etiketlerin olduğundan emin olun.")

if __name__ == "__main__":
    update_readme()
