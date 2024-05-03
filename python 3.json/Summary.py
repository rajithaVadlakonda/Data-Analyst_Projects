#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json
import matplotlib.pyplot as plt
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


# In[2]:


company_data = []
for i in range(1, 6):
    file_path = f'C:/Users/Windows10/Desktop/python2.json/response{i}.json'
    with open(file_path, 'r') as f:
        company_data.append(json.load(f))

company_summaries = {}
for company in (company_data):
    company_name =company.get('businessName')
    for entry in company.get('statutoryAccounts',[]):
        year=entry.get('yearStartDate')
        if company_name not in company_summaries:
            company_summaries[company_name] = {}
        if year not in company_summaries[company_name]:
            company_summaries[company_name][year] = {'turnover': 0, 'grossProfit': 0, 'netWorth': 0,'wagesAndSalaries':0,'totalAssets':0,'EBITDA':0}
        if entry['turnover'] is not None:
            company_summaries[company_name][year]['turnover'] += entry.get('turnover')
        if entry['grossProfit'] is not None:
            company_summaries[company_name][year]['grossProfit'] += entry.get('grossProfit')
        if entry['netWorth'] is not None:
            company_summaries[company_name][year]['netWorth'] += entry.get('netWorth')
        if entry['wagesAndSalaries'] is not None:
            company_summaries[company_name][year]['wagesAndSalaries'] += entry.get('wagesAndSalaries')
        if entry['totalAssets'] is not None:
            company_summaries[company_name][year]['totalAssets'] += entry.get('totalAssets')
        if entry['EBITDA'] is not None:
            company_summaries[company_name][year]['EBITDA'] += entry.get('EBITDA')

pdf_filename = 'financial_comparison_report4.pdf'
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

elements = []
for company_name, summary in company_summaries.items():
    table_data = [['yearStartDate','businessName','turnover','grossProfit','netWorth','wagesAndSalaries','totalAssets','EBITDA']]
    for year, financials in summary.items():
        for entry in company_data:
            if entry['businessName'] == company_name:
                for financial_entry in entry['statutoryAccounts']:
                    if financial_entry.get('yearStartDate') == year:
                        table_data.append([ financial_entry.get('yearStartDate', '-'), company_name, financials['turnover'], financials['grossProfit'], financials['netWorth'],financials['wagesAndSalaries'],financials['totalAssets'],financials['EBITDA']])
                        break
    t = Table(table_data)


    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    t.setStyle(style)

    elements.append(t)

doc.build(elements)

print(f"PDF report generated: {pdf_filename}")




# In[ ]:


pip install reportlab


# In[ ]:




