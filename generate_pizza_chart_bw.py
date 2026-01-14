import matplotlib.pyplot as plt
import re

# Data Source
file_path = '2025_Successful_Cases.md'

# Categories
categories = {
    'Abnormal Instrument Reading': 0.0,
    'Scaling': 0.0,
    'LCO (Liquid Carry Over)': 0.0,
    'Physical Failures (Rotating Equipments)': 0.0
}

# Parse File
with open(file_path, 'r') as f:
    lines = f.readlines()

for line in lines[2:]: # Skip headers
    if '|' not in line or 'TOTAL' in line: continue
    parts = line.split('|')
    if len(parts) < 5: continue
    title = parts[2].strip()
    value_str = parts[4].strip().replace('$', '').replace(',', '')
    try:
        value = float(value_str)
    except ValueError:
        continue
    title_lower = title.lower()
    if 'abnormal instrument' in title_lower:
        categories['Abnormal Instrument Reading'] += value
    elif 'scaling' in title_lower:
        categories['Scaling'] += value
    elif 'lco' in title_lower or 'liquid carry over' in title_lower:
        categories['LCO (Liquid Carry Over)'] += value
    else:
        categories['Physical Failures (Rotating Equipments)'] += value

# Prepare Data
labels = []
sizes = []
total_sum = sum(categories.values())

for cat, val in categories.items():
    if val > 0:
        percent = (val / total_sum) * 100
        labels.append(f"{cat}\n${val/1000000:.2f}M ({percent:.1f}%)")
        sizes.append(val)

# Plotting for B&W Printing
plt.figure(figsize=(8, 8))
plt.rcParams['patch.edgecolor'] = 'black'
plt.rcParams['patch.linewidth'] = 1.0

# Printer Friendly Colors (Grayscale)
colors = ['#FFFFFF', '#D9D9D9', '#808080', '#262626'] 
# Adding hatches to further differentiate for B&W
hatches = ['', '//', '..', 'oo']

# radius=0.5 makes the pie 50% smaller relative to the figure size
wedges, texts = plt.pie(sizes, labels=labels, colors=colors, startangle=140, radius=0.5, 
                        labeldistance=1.2)

# Apply hatches
for i, wedge in enumerate(wedges):
    wedge.set_hatch(hatches[i % len(hatches)])

# Ensure text size is same as previous (10)
for text in texts:
    text.set_fontsize(10)
    text.set_color('black')

plt.title('2025 Cases Value Distribution (Printer Friendly)', fontsize=14, fontweight='bold')
plt.axis('equal') 
plt.tight_layout()

# Save
output_file = '2025_Cases_Pizza_Chart_BW.png'
plt.savefig(output_file, dpi=300, facecolor='white')
print(f"Chart saved to {output_file}")
