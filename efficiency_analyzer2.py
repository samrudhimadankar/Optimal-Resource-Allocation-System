import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ============================================================
# EfficiencyAnalyzerApp Class
# This class creates a GUI to compare the performance of
# Greedy and Brute Force algorithms for two problems:
# 1. Job Scheduling
# 2. Resource Selection
# ============================================================

class EfficiencyAnalyzerApp:
    def __init__(self, root, shared_data):
        """
        Initialize the main window, setup UI styles, and create widgets.
        shared_data is a dictionary that stores results (profits/benefits)
        from other algorithm modules.
        """
        self.root = root
        self.shared_data = shared_data
        self.setup_styles()      # Apply consistent look & feel
        self.create_widgets()    # Create GUI elements

    # -----------------------------
    # STYLE CONFIGURATION
    # -----------------------------
    def setup_styles(self):
        """
        Configure the style for buttons, labels, and entries.
        Makes the interface visually consistent and modern.
        """
        style = ttk.Style()
        style.theme_use("clam")  # Use a simple, flat theme
        style.configure("TButton", font=("Segoe UI", 10, "bold"),
                        foreground="#ffffff", background="#6f42c1", padding=6)
        style.map("TButton", background=[("active", "#5a32a3")])
        style.configure("TLabel", font=("Segoe UI", 10), background="#f9f9f9")
        style.configure("TEntry", padding=4)

    # -----------------------------
    # WIDGET CREATION
    # -----------------------------
    def create_widgets(self):
        """
        Build the interface:
        - A button to run analysis
        - A text box for displaying results
        - A frame for displaying the Matplotlib chart
        """
        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        # Button to trigger analysis
        ttk.Button(frame, text="Run Efficiency Analysis",
                   command=self.run_analysis).grid(row=0, column=0, padx=10)

        # Output area to show analysis results
        self.output = tk.Text(self.root, height=10, width=95,
                              bg="#ffffff", font=("Consolas", 10))
        self.output.pack(pady=10)

        # Frame to hold the chart
        self.chart_frame = ttk.Frame(self.root)
        self.chart_frame.pack()

    # -----------------------------
    # MAIN ANALYSIS FUNCTION
    # -----------------------------
    def run_analysis(self):
        """
        Retrieve Greedy and Brute Force results from shared_data,
        calculate efficiency, display text results, and plot a chart.
        """
        self.output.delete("1.0", tk.END)  # Clear previous output

        # Retrieve results from shared_data dictionary
        g_job = self.shared_data.get("job_greedy_profit", 0)          # Greedy Job Profit
        b_job = self.shared_data.get("job_brute_profit", 1)           # Brute Force Job Profit
        g_res = self.shared_data.get("resource_greedy_benefit", 0)    # Greedy Resource Benefit
        b_res = self.shared_data.get("resource_brute_benefit", 1)     # Brute Force Resource Benefit

        # Compute efficiency as (Greedy / Brute Force) * 100
        job_eff = round((g_job / b_job) * 100, 2) if b_job > 0 else 0
        res_eff = round((g_res / b_res) * 100, 2) if b_res > 0 else 0

        # Display Job Scheduling results
        self.output.insert(tk.END, f"📊 Job Scheduling:\n")
        self.output.insert(tk.END, f"  Greedy Profit: ₹{g_job}\n")
        self.output.insert(tk.END, f"  Brute Force Profit: ₹{b_job}\n")
        self.output.insert(tk.END, f"  Efficiency: {job_eff}%\n\n")

        # Display Resource Selection results
        self.output.insert(tk.END, f"📊 Resource Selection:\n")
        self.output.insert(tk.END, f"  Greedy Benefit: ₹{g_res}\n")
        self.output.insert(tk.END, f"  Brute Force Benefit: ₹{b_res}\n")
        self.output.insert(tk.END, f"  Efficiency: {res_eff}%\n\n")

        # Show theoretical time complexities
        self.output.insert(tk.END, f"🧠 Time Complexity:\n")
        self.output.insert(tk.END, f"  Greedy: O(n log n)\n")
        self.output.insert(tk.END, f"  Brute Force: O(2ⁿ)\n")

        # Plot a comparison chart
        self.plot_chart(g_job, b_job, g_res, b_res)

    # -----------------------------
    # CHART PLOTTING FUNCTION
    # -----------------------------
    def plot_chart(self, g_job, b_job, g_res, b_res):
        """
        Create a bar chart comparing Greedy vs Brute Force results
        for both job scheduling and resource selection problems.
        """
        # Clear previous charts
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        # Create a new figure
        fig, ax = plt.subplots(figsize=(6, 4))

        # Categories for comparison
        categories = ['Jobs', 'Resources']
        greedy = [g_job, g_res]
        brute = [b_job, b_res]

        # Bar settings
        bar_width = 0.35
        index = range(len(categories))

        # Plot Greedy bars (cyan) and Brute Force bars (red)
        ax.bar(index, greedy, bar_width, label='Greedy', color='#17a2b8')
        ax.bar([i + bar_width for i in index], brute, bar_width, label='Brute Force', color='#dc3545')

        # Label axes and title
        ax.set_xlabel('Category')
        ax.set_ylabel('₹ Value')
        ax.set_title('Greedy vs Brute Force Comparison')

        # Adjust x-axis tick labels
        ax.set_xticks([i + bar_width / 2 for i in index])
        ax.set_xticklabels(categories)

        # Add legend
        ax.legend()

        # Embed the Matplotlib figure inside Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
