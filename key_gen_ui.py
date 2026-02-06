"""
Indian SMB ERP - Admin Key Generator
Tool for generating license keys for clients
"""
import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox
import datetime

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from license.license_manager import get_license_manager, LicensePlans

class KeyGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ERP Key Generator (Admin Only)")
        self.geometry("400x500")
        self.resizable(False, False)
        
        self.lm = get_license_manager()
        
        self.setup_ui()
        
    def setup_ui(self):
        main_frame = ttk.Frame(self, padding=20)
        main_frame.pack(fill="both", expand=True)
        
        # Header
        ttk.Label(main_frame, text="License Key Generator", font=("Segoe UI", 16, "bold")).pack(pady=(0, 20))
        
        # Plan Selection
        ttk.Label(main_frame, text="Select Plan:").pack(anchor="w")
        self.plan_var = tk.StringVar(value=LicensePlans.BASIC)
        
        plans = [
            (LicensePlans.BASIC, "Basic (Billing + Stock)"),
            (LicensePlans.PRO, "Pro (Accounts + Reports)"),
            (LicensePlans.ENTERPRISE, "Enterprise (Full Suite)"),
            (LicensePlans.TRIAL, "Trial (30 Days)")
        ]
        
        for val, label in plans:
            ttk.Radiobutton(main_frame, text=label, variable=self.plan_var, value=val).pack(anchor="w", padx=10, pady=2)
            
        # Optional: Expiry Override
        ttk.Label(main_frame, text="Duration (Days):").pack(anchor="w", pady=(20, 5))
        self.duration_var = tk.StringVar(value="365")
        ttk.Entry(main_frame, textvariable=self.duration_var).pack(fill="x")
        
        # Generate Button
        ttk.Button(main_frame, text="Generate Key", command=self.generate).pack(fill="x", pady=30)
        
        # Result Area
        ttk.Label(main_frame, text="Generated Key:").pack(anchor="w")
        self.key_entry = ttk.Entry(main_frame, font=("Consolas", 14), justify="center")
        self.key_entry.pack(fill="x", pady=5)
        
        copy_btn = ttk.Button(main_frame, text="Copy to Clipboard", command=self.copy_key)
        copy_btn.pack(pady=5)
        
    def generate(self):
        plan = self.plan_var.get()
        # Note: The current simple generation logic encodes Plan in prefix but doesn't embed expiry.
        # Expiry is set upon activation based on the plan default.
        # If we wanted to embed custom expiry, we'd need a more complex signature.
        # For now, adhering to existing scheme.
        
        key = self.lm.generate_license_key(plan)
        self.key_entry.delete(0, 'end')
        self.key_entry.insert(0, key)
        
    def copy_key(self):
        key = self.key_entry.get()
        if key:
            self.clipboard_clear()
            self.clipboard_append(key)
            messagebox.showinfo("Copied", "License key copied to clipboard")

if __name__ == "__main__":
    app = KeyGeneratorApp()
    app.mainloop()
