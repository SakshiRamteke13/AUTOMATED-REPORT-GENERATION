# AUTOMATED-REPORT-GENERATION

*COMPANY* : CODTECH IT SOLUTIONS
*NAME* : SAKSHI KAILASH RAMTEKE
*INTERN ID* : CT4MTDF290
*DOMAIN* : PYTHON PROGRAMMING
*DURATION* : 16 WEEKS
*MENTOR* : NEELA SANTHOSH KUMAR

This project reads a CSV file, analyzes the data, creates a plot, and generates a formatted PDF report using ReportLab.

## What you get in this package
- `sales_data.csv` - sample dataset (sales)
- `generate_report.py` - main script (uses ReportLab)
- `requirements.txt` - Python packages to install
- `outputs/` - (will contain generated files)

## Tools to install (from scratch)

### 1) Install Python (3.10+)
- Windows / macOS / Linux: https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" on Windows installer.

### 2) Recommended: Visual Studio Code (editor)
- https://code.visualstudio.com/

### 3) (Optional) Git
- https://git-scm.com/

## Setup and run (Windows / macOS / Linux)
1. Open a terminal (or VS Code terminal)
2. Create project folder and virtual environment (example):
   ```bash
   mkdir codtech-task2
   cd codtech-task2
   python -m venv venv
   # Windows PowerShell
   .\\venv\\Scripts\\Activate.ps1
   # Windows cmd
   venv\\Scripts\\activate.bat
   # macOS / Linux
   source venv/bin/activate
   ```
3. Copy the provided files into this folder (or extract the ZIP).
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the report generator:
   ```bash
   python generate_report.py
   ```
6. Outputs will be in the `outputs/` folder: `sales_report.pdf`, `revenue_by_product.png`.

## Notes
- `generate_report.py` uses ReportLab to make a nicely formatted PDF. If you prefer FPDF, ask me for a version.
- The sample dataset is small; replace `sales_data.csv` with your data (columns: date, product, quantity, unit_price).

## Output
<img width="600" height="300" alt="Image" src="https://github.com/user-attachments/assets/2cd8e48f-e610-4091-9b43-12c53afcc40c" />
[sales_report.pdf](https://github.com/user-attachments/files/22475702/sales_report.pdf)
