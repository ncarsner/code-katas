"""
Bonus Truncation Analysis

This module analyzes the impact of truncating employee annual bonuses to specific dollar increments.
The truncation rule:
- If 0 < bonus < increment: adjusted_bonus = increment
- If bonus >= increment: adjusted_bonus = floor to nearest increment
- If bonus = 0: adjusted_bonus = 0
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from typing import List, Dict
import seaborn as sns

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Configuration: Percentage of employees with no bonus
PERCENT_NO_BONUS = 0.20  # 20% of employees receive no bonus

# Sample data for employee generation
FIRST_NAMES = [
    "Alex", "Blake", "Chris", "Cameron", "Dylan", "Elliot", "Frankie", "Jordan",
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
    "William", "Barbara", "David", "Elizabeth", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy", "Daniel", "Lisa",
    "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra", "Donald", "Ashley",
    "Steven", "Kimberly", "Paul", "Emily", "Andrew", "Donna", "Joshua", "Michelle",
    "Kenneth", "Dorothy", "Kevin", "Carol", "Brian", "Amanda", "George", "Melissa",
    "Edward", "Deborah", "Ronald", "Stephanie", "Timothy", "Rebecca", "Jason", "Sharon",
    "Jeffrey", "Laura", "Ryan", "Cynthia", "Jacob", "Kathleen", "Gary", "Amy",
    "Nicholas", "Shirley", "Eric", "Angela", "Jonathan", "Helen", "Stephen", "Anna"
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Lee",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas",
    "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White",
    "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young",
    "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Wu",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
    "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker",
    "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy"
]

TITLES = [
    "Software Engineer", "Senior Software Engineer", "Staff Software Engineer",
    "Product Manager", "Senior Product Manager", "Engineering Manager",
    "Data Analyst", "Senior Data Analyst", "Data Scientist",
    "Marketing Manager", "Sales Representative", "Senior Sales Representative",
    "Account Manager", "Customer Success Manager", "HR Specialist",
    "Financial Analyst", "Operations Manager", "Project Manager",
    "Sr IT Manager", "IT Manager", "System Administrator", "Network Engineer",
    "UX Designer", "Senior UX Designer", "DevOps Engineer",
    "QA Engineer", "Technical Writer", "Business Analyst", "BI Specialist",
]


class Employee:
    """Represents an employee with their annual bonus."""
    
    def __init__(self, name: str, title: str, bonuses: List[float]):
        self.name = name
        self.title = title
        self.bonuses = bonuses
    
    @property
    def total_bonus(self) -> float:
        """Calculate total annual bonus."""
        return sum(self.bonuses)
    
    def __repr__(self):
        return f"Employee(name='{self.name}', title='{self.title}', bonuses={len(self.bonuses)})"


def generate_employees(num_employees: int = 100) -> List[Employee]:
    """
    Generate a list of employees with random annual bonuses.
    
    Args:
        num_employees: Number of employees to generate
        
    Returns:
        List of Employee objects
    """
    employees = []
    used_names = set()
    
    for _ in range(num_employees):
        # Generate unique name
        while True:
            name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
            if name not in used_names:
                used_names.add(name)
                break
        
        # Assign random title
        title = random.choice(TITLES)
        
        # Generate annual bonus based on PERCENT_NO_BONUS
        if random.random() < PERCENT_NO_BONUS:
            bonuses = []
        else:
            # Single annual bonus ranging from $10 to $20,000
            # Use log-normal distribution for realistic bonus amounts
            bonus = np.random.lognormal(mean=7.5, sigma=1.3)
            bonus = max(10, min(20000, bonus))  # Clamp between 10 and 20,000
            bonuses = [round(bonus, 2)]
        
        employees.append(Employee(name, title, bonuses))
    
    return employees


def truncate_bonus(bonus: float, increment: float) -> float:
    """
    Truncate a bonus to the specified increment.
    
    Rules:
    - If 0 < bonus < increment: return increment (minimum payout)
    - If bonus >= increment: floor to nearest increment (round down)
    - If bonus = 0: return 0
    
    Examples for $50 increment:
        56.75 → 50, 75.13 → 50, 90.15 → 50, 150.00 → 150, 175.99 → 150
    
    Args:
        bonus: Original bonus amount
        increment: Dollar increment (e.g., 25, 50, 100)
        
    Returns:
        Truncated bonus amount
    """
    if bonus == 0:
        return 0
    elif 0 < bonus < increment:
        return increment
    else:
        # Floor division: round down to nearest increment
        import math
        return math.floor(bonus / increment) * increment


def calculate_adjusted_bonuses(employees: List[Employee], increment: float) -> Dict[str, List[int]]:
    """
    Calculate adjusted bonuses for all employees based on increment.
    
    Args:
        employees: List of Employee objects
        increment: Dollar increment for truncation
        
    Returns:
        Dictionary with original and adjusted bonus totals
    """
    original_totals = []
    adjusted_totals = []
    
    for employee in employees:
        original_total = sum(employee.bonuses)
        adjusted_bonuses = [truncate_bonus(b, increment) for b in employee.bonuses]
        adjusted_total = sum(adjusted_bonuses)
        
        original_totals.append(original_total)
        adjusted_totals.append(adjusted_total)
    
    return {
        'original': original_totals,
        'adjusted': adjusted_totals
    }


def analyze_impact(employees: List[Employee], increments: List[float]) -> Dict:
    """
    Analyze the financial impact of different increment scenarios.
    
    Args:
        employees: List of Employee objects
        increments: List of increment values to analyze
        
    Returns:
        Dictionary with analysis results
    """
    results = {}
    
    for increment in increments:
        data = calculate_adjusted_bonuses(employees, increment)
        original_sum = sum(data['original'])
        adjusted_sum = sum(data['adjusted'])
        savings = original_sum - adjusted_sum  # Positive = cost savings
        percent_savings = (savings / original_sum * 100) if original_sum > 0 else 0
        
        # Count employees affected
        num_reduced = sum(1 for orig, adj in zip(data['original'], data['adjusted']) if adj < orig)
        num_increased = sum(1 for orig, adj in zip(data['original'], data['adjusted']) if adj > orig)
        num_unchanged = sum(1 for orig, adj in zip(data['original'], data['adjusted']) if adj == orig)
        
        results[increment] = {
            'original_total': original_sum,
            'adjusted_total': adjusted_sum,
            'savings': savings,
            'percent_savings': percent_savings,
            'data': data,
            'num_reduced': num_reduced,
            'num_increased': num_increased,
            'num_unchanged': num_unchanged
        }
    
    return results


def create_visualizations(employees: List[Employee], increments: List[float]):
    """
    Create comprehensive visualizations comparing different increment scenarios.
    
    Args:
        employees: List of Employee objects
        increments: List of increment values to visualize
    """
    # Set style
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (16, 12)
    
    # Analyze data
    results = analyze_impact(employees, increments)
    baseline_data = [e.total_bonus for e in employees]
    
    # Create subplot grid (4 columns to accommodate baseline + 3 increments)
    fig = plt.figure(figsize=(20, 12))
    gs = fig.add_gridspec(3, 4, hspace=0.3, wspace=0.3)
    
    # Color palette
    colors = ['#2ecc71', '#3498db', '#e74c3c', '#9b59b6']
    
    # 1. Distribution comparison (top row)
    for idx, increment in enumerate([None] + increments):
        ax = fig.add_subplot(gs[0, idx])
        
        if increment is None:
            # Baseline
            data = baseline_data
            title = "Baseline (Unadjusted)"
            color = colors[0]
        else:
            data = results[increment]['data']['adjusted']
            title = f"${increment:.0f} Increment"
            color = colors[idx]
        
        ax.hist(data, bins=30, alpha=0.7, color=color, edgecolor='black')
        ax.set_xlabel('Total Annual Bonus ($)', fontsize=10)
        ax.set_ylabel('Number of Employees', fontsize=10)
        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        
        # Add statistics
        mean_val = float(np.mean(data))
        median_val = float(np.median(data))
        ax.axvline(mean_val, color='red', linestyle='--', linewidth=2, alpha=0.7, label=f'Avg: ${mean_val:.0f}')
        ax.axvline(median_val, color='orange', linestyle='--', linewidth=2, alpha=0.7, label=f'Median: ${median_val:.0f}')
        ax.legend(fontsize=8)
    
    # 2. Box plots comparison (middle left - spans 2 columns)
    ax2 = fig.add_subplot(gs[1, 0:2])
    box_data = [baseline_data] + [results[inc]['data']['adjusted'] for inc in increments]
    box_labels = ['Baseline'] + [f'${inc:.0f}' for inc in increments]
    bp = ax2.boxplot(box_data, tick_labels=box_labels, patch_artist=True)
    
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax2.set_ylabel('Total Annual Bonus ($)', fontsize=10)
    ax2.set_title('Bonus Distribution Comparison', fontsize=12, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)
    
    # Add legend to explain box plot components
    from matplotlib.patches import Rectangle
    legend_elements = [
        Rectangle((0, 0), 1, 1, facecolor='lightgray', edgecolor='black', label='25th-75th IQR'),
        Line2D([0], [0], color='orange', linewidth=2, label='Median'),
        Line2D([0], [0], color='black', linewidth=1, label='Min/Max ± 1.5×IQR'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='black', markersize=6, label='Outliers')
    ]
    ax2.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)
    
    # 3. Savings summary (middle center-right)
    ax3 = fig.add_subplot(gs[1, 2])
    increments_labels = [f'${inc:.0f}' for inc in increments]
    savings_amounts = [results[inc]['savings'] for inc in increments]
    
    # Use green for savings (positive), red for costs (negative)
    bar_colors = ['#27ae60' if s > 0 else '#e74c3c' for s in savings_amounts]
    bars = ax3.bar(increments_labels, savings_amounts, color=bar_colors, alpha=0.7, edgecolor='black')
    
    ax3.set_ylabel('Total Savings ($)', fontsize=10)
    ax3.set_xlabel('Increment Level', fontsize=10)
    ax3.set_title('Cost Savings by Increment', fontsize=12, fontweight='bold')
    ax3.grid(axis='y', alpha=0.3)
    ax3.axhline(y=0, color='black', linestyle='-', linewidth=1)
    
    # Add value labels on bars (without percentage)
    for bar, savings in zip(bars, savings_amounts):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:,.0f}',
                ha='center', va='bottom' if height > 0 else 'top', fontsize=10, fontweight='bold')
    
    # Adjust y-axis limits to provide space for labels above bars
    y_max = max(savings_amounts) if savings_amounts else 0
    y_min = min(savings_amounts) if savings_amounts else 0
    if y_max > 0:
        ax3.set_ylim(top=y_max * 1.15)  # Add 15% space above highest bar
    if y_min < 0:
        ax3.set_ylim(bottom=y_min * 1.15)
    
    # 4. Percent savings (middle right)
    ax4 = fig.add_subplot(gs[1, 3])
    percent_savings = [results[inc]['percent_savings'] for inc in increments]
    
    # Use green for savings (positive), red for costs (negative)
    bar_colors = ['#27ae60' if s > 0 else '#e74c3c' for s in percent_savings]
    bars = ax4.bar(increments_labels, percent_savings, color=bar_colors, alpha=0.7, edgecolor='black')
    
    ax4.set_ylabel('Percent Savings (%)', fontsize=10)
    ax4.set_xlabel('Increment Level', fontsize=10)
    ax4.set_title('Percentage Cost Savings', fontsize=12, fontweight='bold')
    ax4.grid(axis='y', alpha=0.3)
    ax4.axhline(y=0, color='black', linestyle='-', linewidth=1)
    
    # Add value labels
    for bar, pct in zip(bars, percent_savings):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}%',
                ha='center', va='bottom' if height > 0 else 'top', fontsize=9, fontweight='bold')
    
    # Adjust y-axis limits to provide space for labels above bars
    y_max = max(percent_savings) if percent_savings else 0
    y_min = min(percent_savings) if percent_savings else 0
    if y_max > 0:
        ax4.set_ylim(top=y_max * 1.15)  # Add 15% space above highest bar
    if y_min < 0:
        ax4.set_ylim(bottom=y_min * 1.15)

    # 5. Distribution of Savings Per Employee (bottom left - spans 2 columns)
    ax5 = fig.add_subplot(gs[2, 0:2])
    
    # Calculate savings per employee for each increment
    for idx, increment in enumerate(increments):
        original = np.array(results[increment]['data']['original'])
        adjusted = np.array(results[increment]['data']['adjusted'])
        savings_per_employee = original - adjusted  # Positive = savings
        
        # Only include employees with bonuses (exclude zeros)
        savings_with_bonuses = [s for s, o in zip(savings_per_employee, original) if o > 0]
        
        ax5.hist(savings_with_bonuses, bins=50, alpha=0.6, label=f'${increment:.0f}', 
                color=colors[idx+1], edgecolor='black', linewidth=0.5)
    
    ax5.set_xlabel('Savings Per Employee ($)', fontsize=10)
    ax5.set_ylabel('Number of Employees', fontsize=10)
    ax5.set_title('Distribution of Individual Employee Savings', fontsize=12, fontweight='bold')
    ax5.axvline(0, color='red', linestyle='--', linewidth=2, alpha=0.7, label='Zero savings')
    ax5.legend(fontsize=8)
    ax5.grid(axis='y', alpha=0.3)
    
    # 6. Savings Impact by Bonus Range (bottom right - spans 2 columns)
    ax6 = fig.add_subplot(gs[2, 2:4])
    
    # Define bonus ranges for analysis
    bonus_ranges = [(0, 1000), (1000, 2500), (2500, 5000), (5000, 10000), (10000, 20000)]
    range_labels = ['$0-1K', '$1K-2.5K', '$2.5K-5K', '$5K-10K', '$10K-20K']
    
    # Calculate average savings per range for each increment
    x_pos = np.arange(len(range_labels))
    width = 0.25
    
    for idx, increment in enumerate(increments):
        original = np.array(results[increment]['data']['original'])
        adjusted = np.array(results[increment]['data']['adjusted'])
        savings_per_employee = original - adjusted
        
        avg_savings_by_range = []
        for low, high in bonus_ranges:
            # Get savings for employees in this bonus range
            range_savings = [s for s, o in zip(savings_per_employee, original) if low < o <= high]
            avg_savings = np.mean(range_savings) if range_savings else 0
            avg_savings_by_range.append(avg_savings)
        
        offset = (idx - 1) * width
        bars = ax6.bar(x_pos + offset, avg_savings_by_range, width, 
                      label=f'${increment:.0f}', alpha=0.7, color=colors[idx+1], edgecolor='black')
        
        # Add value labels on bars for clarity
        for bar, val in zip(bars, avg_savings_by_range):
            if val > 0:
                height = bar.get_height()
                ax6.text(bar.get_x() + bar.get_width()/2., height,
                        f'${val:.0f}', ha='center', va='bottom', fontsize=7)
    
    ax6.set_xlabel('Original Bonus Range', fontsize=10)
    ax6.set_ylabel('Average Savings Per Employee ($)', fontsize=10)
    ax6.set_title('Average Savings by Bonus Range', fontsize=12, fontweight='bold')
    ax6.set_xticks(x_pos)
    ax6.set_xticklabels(range_labels)
    ax6.legend(fontsize=8)
    ax6.grid(axis='y', alpha=0.3)
    ax6.axhline(0, color='black', linestyle='-', linewidth=1)
    
    # Calculate employee statistics for subtitle
    num_employees = len(employees)
    num_with_bonuses = sum(1 for e in employees if e.total_bonus > 0)
    num_without_bonuses = num_employees - num_with_bonuses
    
    plt.suptitle('Bonus Truncation Analysis: Impact of Different Increment Scenarios', 
                 fontsize=16, fontweight='bold', y=0.995)
    
    # Add subtitle with employee count information (with more space from title)
    fig.text(0.5, 0.960, 
             f'Dataset: {num_employees:,} Employees ({num_with_bonuses:,} with bonuses, {num_without_bonuses:,} without bonuses)',
             ha='center', fontsize=12, style='italic', color='#555555')
    
    plt.tight_layout()
    plt.show()


def print_sample_data(employees: List[Employee], increments: List[float], sample_size: int = 10):
    """Print a human-readable sample of employee bonus data."""
    import random
    
    # Get a random sample of employees with bonuses
    employees_with_bonuses = [e for e in employees if e.total_bonus > 0]
    sample = random.sample(employees_with_bonuses, min(sample_size, len(employees_with_bonuses)))
    
    print("\n" + "="*100)
    print("SAMPLE EMPLOYEE ANNUAL BONUS DATA")
    print("="*100)
    print(f"\nShowing {len(sample)} random employees with bonuses:\n")
    
    for i, emp in enumerate(sample, 1):
        print(f"{i}. {emp.name} - {emp.title}")
        print(f"   {'─'*90}")
        
        # Show annual bonus
        if len(emp.bonuses) > 0:
            print(f"   Annual Bonus:       ${emp.total_bonus:,.2f}")
            print()
            
            # Show adjusted values for each increment
            for increment in increments:
                adjusted_bonuses = [truncate_bonus(b, increment) for b in emp.bonuses]
                adjusted_total = sum(adjusted_bonuses)
                savings = emp.total_bonus - adjusted_total
                
                # Color code the change
                change_indicator = "💰 SAVES" if savings > 0 else "💸 COSTS" if savings < 0 else "➡️  SAME"
                
                print(f"   ${increment:>3.0f} Increment:  ${adjusted_total:,.2f} | {change_indicator} ${abs(savings):,.2f}")
            
            print()
    
    print("="*100 + "\n")


def print_summary(employees: List[Employee], increments: List[float]):
    """Print a summary of the analysis."""
    results = analyze_impact(employees, increments)
    baseline_total = sum(e.total_bonus for e in employees)
    
    print("="*80)
    print("BONUS TRUNCATION ANALYSIS SUMMARY")
    print("="*80)
    print(f"\nTotal Employees: {len(employees)}")
    print(f"Employees with Bonuses: {sum(1 for e in employees if e.total_bonus > 0)}")
    print(f"Employees with No Bonuses: {sum(1 for e in employees if e.total_bonus == 0)}")
    print(f"\nBaseline Total Bonus Payout: ${baseline_total:,.2f}")
    print(f"Average Bonus per Employee: ${baseline_total/len(employees):,.2f}")
    
    print("\n" + "-"*80)
    print("SAVINGS BY INCREMENT LEVEL (Truncation uses FLOOR logic)")
    print("-"*80)
    print("\nTruncation Rules:")
    print("  • If 0 < bonus < increment: adjusted = increment (minimum payout)")
    print("  • If bonus >= increment: adjusted = FLOOR(bonus/increment) × increment")
    print("  • Examples for $50 increment: $56.75→$50, $75.13→$50, $150.00→$150")
    
    for increment in increments:
        result = results[increment]
        print(f"\n${increment:.0f} Increment:")
        print(f"  Original Total Payout:  ${result['original_total']:,.2f}")
        print(f"  Adjusted Total Payout:  ${result['adjusted_total']:,.2f}")
        print(f"  TOTAL SAVINGS:          ${result['savings']:,.2f} ({result['percent_savings']:.2f}%)")
        print(f"  " + "-" * 60)
        print(f"  Employees with reduced bonuses:   {result['num_reduced']}")
        print(f"  Employees with increased bonuses: {result['num_increased']}")
        print(f"  Employees unchanged:              {result['num_unchanged']}")
        print(f"  New Average Bonus per Employee:   ${result['adjusted_total']/len(employees):,.2f}")
    
    print("\n" + "="*80)
    print("KEY INSIGHT: Larger increments = Greater Savings")
    print("="*80)
    for increment in increments:
        result = results[increment]
        print(f"${increment:.0f} increment saves ${result['savings']:,.2f} ({result['percent_savings']:.2f}% reduction)")
    print("="*80)


def main(show_sample_data: bool = True, sample_size: int = 10):
    """Main execution function.
    
    Args:
        show_sample_data: If True, print sample employee bonus data
        sample_size: Number of sample employees to display
    """
    # Generate employee data
    print("Generating employee data...")
    employees = generate_employees(num_employees=1_000)
    
    # Define increment scenarios
    increments = [50.0, 100.0, 250.0]
    
    # Print sample data if enabled
    if show_sample_data:
        print_sample_data(employees, increments, sample_size)
    
    # Print summary
    print_summary(employees, increments)
    
    # Create visualizations
    print("\nGenerating visualizations...")
    create_visualizations(employees, increments)
    
    print("\nAnalysis complete!")


if __name__ == "__main__":
    # Toggle for showing sample employee data
    # Set to False to hide sample data, adjust sample_size to show more/fewer examples
    main(show_sample_data=True, sample_size=10)
