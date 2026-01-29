import json
import os

def calculate_stars(project_count):
    # Yıldız hesaplama mantığı
    if project_count == 0: return "⚪⚪⚪⚪⚪ (Level 0)"
    elif project_count <= 2: return "⭐⚪⚪⚪⚪ (Level 1)"
    elif project_count <= 5: return "⭐⭐⚪⚪⚪ (Level 2)"
    elif project_count <= 10: return "⭐⭐⭐⚪⚪ (Level 3)"
    elif project_count <= 20: return "⭐⭐⭐⭐⚪ (Level 4)"
    else: return "⭐⭐⭐⭐⭐ (Level 5)"

def update_readme():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'data.json')
    readme_path = os.path.join(base_dir, 'README.md')

    # Veriyi JSON'dan çekiyoruz
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # TABLO OLUŞTURMA
    # Vibe Coding'i 2. sıraya aldık ve değerini JSON'dan çekiyoruz
    stats_markdown = f"""
| Skill Class | Stars | Rank |
| :--- | :--- | :--- |
| **🐍 Python** | {calculate_stars(data['stats']['Python'])} | *Apprentice* |
| **✨ Vibe Coding** | {calculate_stars(data['stats']['Vibe_Coding'])} | *Flow State Master* |
| **🧠 AI Engineering** | {calculate_stars(data['stats']['AI_Engineering'])} | *Newbie* |
| **🔬 Data Science** | {calculate_stars(data['stats']['Data_Science'])} | *Newbie* |
| **🏗️ Data Engineering** | {calculate_stars(data['stats']['Data_Engineering'])} | *Newbie* |
"""

    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    start_marker = ""
    end_marker = ""
    
    # İşaretçilerin yerini buluyoruz
    s_loc = readme_content.find(start_marker)
    e_loc = readme_content.find(end_marker)

    if s_loc != -1 and e_loc != -1:
        # TEMİZLİK VE EKLEME İŞLEMİ:
        # 1. Başlangıç işaretçisinin sonuna kadar olan kısmı al
        before_part = readme_content[:s_loc + len(start_marker)]
        
        # 2. Bitiş işaretçisinden sonraki kısmı al
        after_part = readme_content[e_loc:]
        
        # 3. Araya yeni tabloyu koy (Böylece eski tablo silinmiş olur)
        new_content = before_part + "\n" + stats_markdown + "\n" + after_part
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ README temizlendi ve güncellendi!")
    else:
        print("❌ HATA: İşaretçiler (STATS_START / STATS_END) bulunamadı!")

if __name__ == "__main__":
    update_readme()
