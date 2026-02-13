import math
import time

class ResonanceEngine:
    @staticmethod
    def get_digital_root(text):
        # 1. НОРМАЛІЗАЦІЯ: Переводимо в малі літери, щоб 'Code' == 'code'
        clean_text = text.lower().strip()
        
        # 2. ВАГА ПОЗИЦІЇ: Перша літера задає тон (множимо її код на 2)
        # Це розрізнить анаграми (наприклад, 'live' vs 'evil')
        weighted_sum = sum(ord(char) * (i+1) for i, char in enumerate(clean_text))
        
        # Вортекс математика (сума до однієї цифри)
        return (weighted_sum - 1) % 9 + 1

    def assign_gem_agent(self, root):
        """Розподіляє задачу між 13 Джемами на основі вібрації"""
        
        # ГРУПА МАТЕРІЇ (1, 4, 7) - Структура / Backend
        if root in [1, 4, 7]:
            return "🔴 RED TRIANGLE (Logic/Data)", "Gem #5: Backend Architect"
            
        # ГРУПА ДАНИХ (2, 5, 8) - Пам'ять / Архів
        elif root in [2, 5, 8]:
            return "🟡 GOLD TRIANGLE (Validation)", "Gem #3: Archivist"
            
        # ГРУПА ПОТОКУ (3, 6) - Інтерфейс / Рух
        elif root in [3, 6]:
            return "🔵 BLUE/GREEN FLUX (API/UI)", "Gem #9: Interface Flow"
            
        # ГРУПА ЕФІРУ (9) - Ядро / Вищий Розум
        elif root == 9:
            return "🟣 VORTEX CENTER (Bindu)", "Gem #13: THE CORE"
            
        return "⚪ GATEKEEPER", "Gem #1: Input Filter"

class VCoreSystem:
    def __init__(self):
        self.resonance = ResonanceEngine()

    def run(self, user_input):
        print(f"\n🌀 Scanning Signal: '{user_input}'...")
        time.sleep(0.5) # Ефект сканування
        
        root = self.resonance.get_digital_root(user_input)
        zone, agent = self.resonance.assign_gem_agent(root)
        
        print(f"   [Resonance Frequency]: {root}")
        print(f"   [Active Zone]: {zone}")
        print(f"   [Summoning Agent]: {agent}")
        
        if root == 9:
            print("   ✨ ETHER DETECTED! Direct connection to Source.")
        
        return "Signal Processed."

# === ТЕСТУВАННЯ ===
if __name__ == "__main__":
    system = VCoreSystem()
    
    # Тепер 'Code' і 'code' дадуть стабільний результат
    system.run("GitCube")  
    system.run("Bug")
    system.run("Harmony") # Спробуй знайти слово, що дасть 9
