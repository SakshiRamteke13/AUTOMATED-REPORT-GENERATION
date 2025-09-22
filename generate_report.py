# generate_report.py
# Reads a CSV, creates summary stats + plot, and generates a formatted PDF using ReportLab.
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def create_plot(summary_df, out_png):
    plt.figure(figsize=(6,3))
    s = summary_df.sort_values('revenue', ascending=False)
    plt.bar(s['product'], s['revenue'])
    plt.ylabel('Revenue ($)')
    plt.title('Revenue by Product')
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()

def create_pdf_report(csv_file='sales_data.csv', output_pdf='outputs/sales_report.pdf'):
    # local imports for PDF generation
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
    from reportlab.lib.styles import getSampleStyleSheet

    # Read data
    df = pd.read_csv(csv_file, parse_dates=['date'])
    df['revenue'] = df['quantity'] * df['unit_price']

    # Summary by product
    summary = df.groupby('product').agg({'quantity':'sum', 'revenue':'sum'}).reset_index()
    summary['revenue'] = summary['revenue'].round(2)

    # Ensure output folder exists
    Path('outputs').mkdir(parents=True, exist_ok=True)
    plot_path = 'outputs/revenue_by_product.png'
    create_plot(summary, plot_path)

    # Build PDF
    doc = SimpleDocTemplate(output_pdf, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph('Automated Sales Report', styles['Title']))
    elements.append(Spacer(1, 12))

    # Intro paragraph
    intro = f'This report was generated automatically from the CSV file: <b>{csv_file}</b>.'
    elements.append(Paragraph(intro, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Add summary table
    table_data = [['Product', 'Total Quantity', 'Total Revenue ($)']]
    for r in summary.itertuples(index=False):
        table_data.append([r.product, int(r.quantity), f'{r.revenue:,.2f}'])

    t = Table(table_data, hAlign='LEFT', colWidths=[200, 100, 120])
    t.setStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#4f81bd')),
                ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
                ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                ('ALIGN',(1,1),(-1,-1),'RIGHT')])
    elements.append(t)
    elements.append(Spacer(1, 12))

    # Add chart image
    elements.append(Paragraph('Revenue by Product', styles['Heading2']))
    elements.append(Image(plot_path, width=400, height=200))
    elements.append(Spacer(1, 12))

    # Add simple stats paragraph
    total_revenue = df['revenue'].sum()
    total_qty = df['quantity'].sum()
    stats = f'<b>Total items sold:</b> {int(total_qty)} &nbsp;&nbsp; <b>Total revenue:</b> ${total_revenue:,.2f}'
    elements.append(Paragraph(stats, styles['Normal']))

    # Build
    doc.build(elements)
    print(f'PDF generated: {output_pdf}')

if __name__ == '__main__':
    create_pdf_report()
