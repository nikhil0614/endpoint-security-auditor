from fpdf import FPDF

def generate_report(results):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Endpoint Security Report", ln=True, align='C')
    
    # Add each check result
    pdf.set_font("Arial", size=12)
    for result in results:
        pdf.multi_cell(0, 10, f"Check: {result['check_name']}\nStatus: {result['status']}\n")
    
    # Output PDF
    pdf.output("audit_report.pdf")

# Example results
results = [
    {"check_name": "Root Login Disabled", "status": "Pass"},
    {"check_name": "No World-Writable Files", "status": "Fail"},
    {"check_name": "Sudoers File Misuse", "status": "Pass"},
    {"check_name": "Kernel Parameters", "status": "Pass"},
    {"check_name": "Failed Login Attempts", "status": "Fail"}
]

generate_report(results)
