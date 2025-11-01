
## Optimal Resource Allocation System

### 🧠 Overview
This project is a GUI-based **Optimal Resource Allocation System** built using **Python and Tkinter**, designed to help users efficiently schedule jobs and select resources based on constraints like time, deadlines, budget, and profit/benefit ratios.

It includes two modules:
- **Job Scheduler**: Selects jobs based on duration, deadline, and profit.
- **Resource Selector**: Chooses resources based on cost, benefit, and budget.

Both modules use **Greedy** and **Brute Force** algorithms to compare efficiency and provide optimal insights.

---

### 🎯 Features

#### ✅ Job Scheduler
- Add jobs manually or upload from Excel
- Sort jobs by:
  - Max Profit
  - Min Duration
  - Best Profit-to-Duration Ratio
- Set available time constraint
- View Greedy schedule vs Brute Force optimal profit
- Efficiency calculation (%)

#### ✅ Resource Selector
- Add resources manually or upload from Excel
- Sort resources by:
  - Max Benefit
  - Min Cost
  - Best Benefit-to-Cost Ratio
- Set budget constraint
- View Greedy selection vs Brute Force optimal benefit
- Efficiency calculation (%)

#### 🖥️ GUI Highlights
- Clean, responsive layout using Tkinter
- Formatted output with emojis and separators
- Clear buttons for Add, Upload, Schedule/Select, and Clear Output

---

### 📂 File Structure

```
├── job_scheduler.py         # Job scheduling module
├── resource_selector.py     # Resource selection module
├── README.md                # Project documentation
├── sample_jobs.xlsx         # Optional sample input file
├── sample_resources.xlsx    # Optional sample input file
```

---

### 🚀 How to Run

1. **Install dependencies**:
   ```bash
   pip install pandas openpyxl
   ```

2. **Run the modules**:
   ```bash
   python job_scheduler.py
   python resource_selector.py
   ```

3. **Use the GUI**:
   - Enter job/resource details manually or upload Excel files
   - Set constraints and sorting preferences
   - Click “Schedule Jobs” or “Select Resources”
   - View formatted output in the text area

---

### 📊 Algorithms Used

| Strategy      | Description |
|---------------|-------------|
| **Greedy**    | Selects items based on sorting preference until constraint is met |
| **Brute Force** | Evaluates all valid combinations to find the optimal total profit/benefit |

Efficiency is calculated as:
\[
\text{Efficiency} = \left( \frac{\text{Greedy Result}}{\text{Brute Force Optimal}} \right) \times 100\%
\]

---

### 📈 Sample Output

```
======================================================================
📅 SCHEDULING JOBS...
======================================================================

🔧 Sort By: Best Ratio

✅ Greedy Schedule:
----------------------------------------------------------------------
  • API Integration      | Duration: 3.0    | Deadline: 6      | Profit: ₹5000
  • UI Review            | Duration: 2.0    | Deadline: 7      | Profit: ₹2500

📊 Available Time: 8.0 hrs | Total Time Used: 5.0 hrs
💰 Total Profit: ₹7500

🔍 Brute Force Optimal Profit: ₹8500
⚡ Efficiency of Greedy: 88.24%
======================================================================
```

---

### 📌 Notes
- Excel files must contain columns:  
  - For jobs: `Job Name`, `Duration`, `Deadline`, `Profit`  
  - For resources: `Resource Name`, `Cost`, `Benefit`
- Ensure `openpyxl` is installed for Excel file support

---

### 👩‍💻 Author
**Samrudhi**  
Focused on optimization, algorithmic efficiency, and polished UI/UX for academic and practical applications.

