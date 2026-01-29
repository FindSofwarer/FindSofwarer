import json

def calculate_stars(project_count):
    # OYUN KURALLARI (LEVEL SİSTEMİ)
    if project_count == 0: return "⚪⚪⚪⚪⚪ (Level 0 - Newbie)"
    elif project_count <= 2: return "⭐⚪⚪⚪⚪ (Level 1 - Apprentice)"
    elif project_count <= 5: return "⭐⭐⚪⚪⚪ (Level 2 - Junior)"
    elif project_count <= 10: return "⭐⭐⭐⚪⚪ (Level 3 - Developer)"
    elif project_count <= 20: return "⭐⭐⭐⭐⚪ (Level 4 - Senior)"
    else: return "⭐⭐⭐⭐⭐ (Level 5 - Master)"

def update_readme():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # İstatistikleri projelerden otomatik hesaplayabiliriz veya manuel artırabiliriz
    # Şimdilik data.json'daki sayıları baz alıyoruz
    
    stats_markdown = f"""
| Skill Class | Stars | Rank |
| :--- | :--- | :--- |
| **🐍 Python** | {calculate_stars(data['stats']['Python'])} | |
| **🧠 AI Engineering** | {calculate_stars(data['stats']['AI_Engineering'])} | |
| **🔬 Data Science** | {calculate_stars(data['stats']['Data_Science'])} | |
| **🏗️ Data Engineering** | {calculate_stars(data['stats']['Data_Engineering'])} | |
| **✨ Vibe Coding** | ⭐⭐⭐⭐⭐ (Max) | {calculate_stars(data['stats']['Vibe_Coding'])}|
"""

    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()

    # README içinde ve arasını değiştir
    start_marker = ""
    end_marker = ""
    
    start_index = readme_content.find(start_marker) + len(start_marker)
    end_index = readme_content.find(end_marker)

    if start_index != -1 and end_index != -1:
        new_content = readme_content[:start_index] + "\n" + stats_markdown + "\n" + readme_content[end_index:]
        
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("README güncellendi!")
    else:
        print("İşaretleyiciler bulunamadı!")

if __name__ == "__main__":
    update_readme()
