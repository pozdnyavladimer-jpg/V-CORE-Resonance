import math
import time

# === THE RESONANCE ENGINE (Vortex Math 3-6-9) ===
class ResonanceEngine:
    @staticmethod
    def get_digital_root(text):
        number = sum(ord(char) for char in text)
        return (number - 1) % 9 + 1

    def get_wave_params(self, text):
        root = self.get_digital_root(text)
        if root in [1, 2, 4, 5, 7, 8]:
            return root, "MATTER_WAVE", 0
        elif root in [3, 6]:
            return root, "MAGNETIC_FLUX", 104.5
        elif root == 9:
            return root, "ETHER_VORTEX", 108
        return root, "UNKNOWN", 90

# === QUANTUM SPIN SIMULATION (Bloch Sphere) ===
class QuantumSpin:
    """Simulates a Qubit state based on the V-CORE Resonance Angle."""
    def visualize_spin(self, angle_deg):
        theta = math.radians(angle_deg)
        # Probability of State |0> (Order) and |1> (Chaos)
        prob_0 = math.cos(theta / 2) ** 2
        prob_1 = math.sin(theta / 2) ** 2
        
        print(f"\n⚛️  [QUANTUM STATE on BLOCH SPHERE]")
        print(f"   Angle: {angle_deg}°")
        print(f"   Spin Up   |0> (Order): {prob_0*100:.2f}%")
        print(f"   Spin Down |1> (Chaos): {prob_1*100:.2f}%")
        
        if angle_deg == 0: return "State: PURE GROUND"
        if angle_deg == 104.5: return "State: BONDING RESONANCE (H2O)"
        if angle_deg == 108: return "State: PENTAGONAL STABILITY"
        return "State: SUPERPOSITION"

# === THE V-CORE SYSTEM ===
class VCoreSystem:
    def __init__(self):
        self.resonance = ResonanceEngine()
        self.quantum = QuantumSpin()

    def run(self, user_input):
        root, wave_type, angle = self.resonance.get_wave_params(user_input)
        
        print(f"\n--- INCOMING SIGNAL: '{user_input}' ---")
        print(f"[Wave Scan] Frequency: {root} | Type: {wave_type}")
        
        # Physics processing simulation
        if angle == 0: print("🔴 [Gate 14] Grounding signal at 0°...")
        elif angle == 104.5: print("🟡 [Core 10] Sodium Spark Triggered! 104.5°...")
        elif angle == 108: print("🟣 [Gate 8] Distilling Ether Essence at 108°...")
        
        # Quantum Layer
        q_state = self.quantum.visualize_spin(angle)
        print(f" >> {q_state}")
        
        return f"\n✅ Processing Complete: {wave_type} stabilized."

# === EXECUTION ===
if __name__ == "__main__":
    vcore = VCoreSystem()
    
    # Test your 3 cases from AI Studio
    vcore.run("Code")     # Matter (1)
    vcore.run("Energy")   # Flux (6)
    vcore.run("Vortex")   # Ether (9)
