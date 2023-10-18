import pandas as pd
import seaborn as sns
import scipy.stats as stats
from fpdf import FPDF

# Read in data
df = pd.read_csv('survey_data.csv')

# Visualize project-2-progress distribution
ax = sns.distplot(df['project-2-progress'], kde=False, bins=10)
ax.axvline(df['project-2-progress'].mean(), color='r')
ax.axvline(df['project-2-progress'].median(), color='g')
ax.set_title('Project 2 Progress Distribution')
fig = ax.get_figure()
fig.savefig('p2_hist.png')

# Visualize python-comfort distribution
ax = sns.distplot(df['python-comfort'], kde=False, bins=10)
ax.axvline(df['python-comfort'].mean(), color='r')
ax.axvline(df['python-comfort'].median(), color='g')
ax.set_title('Python Comfort Distribution')
fig = ax.get_figure()
fig.savefig('python_hist.png')

# Plot scatterplot and calculate correlation
ax = sns.regplot(x='project-2-progress', y='python-comfort', data=df)
ax.set_title('Project 2 Progress vs Python Comfort')
ax.set_xlabel('Project 2 Progress')
ax.set_ylabel('Python Comfort')
corr, _ = stats.pearsonr(df['project-2-progress'], df['python-comfort'])
ax.text(2, 5, f'Pearson Correlation: {corr:.2f}')
fig = ax.get_figure()
fig.savefig('scatter.png')

# Generate PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font('Times', '', 16)
pdf.cell(0, 10, 'Survey Data Analysis', ln=1, align='C')
pdf.image('p2_hist.png', x=60, y=30, w=100)
pdf.image('python_hist.png', x=60, y=120, w=100)
pdf.image('scatter.png', x=60, y=210, w=100)
pdf.output('report.pdf', 'F')

print('Analysis complete, see report.pdf')
