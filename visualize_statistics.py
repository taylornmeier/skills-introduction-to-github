#!/usr/bin/env python3
"""
Statistics Visualization for Mock Data

This script creates comprehensive visualizations of the mock data statistics:
- Bar charts showing mean and median
- Error bars showing 95% confidence intervals
- Box plots showing data distribution
- Combined comparison charts
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for headless environments
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# Constants
LABEL_FONT_SIZE = 8
MAX_LABEL_LENGTH = 20
TABLE_COLUMNS = 6

# Metric labels for display
METRIC_LABELS = {
    'clicks_on_generated_matches': 'Clicks on Generated Matches',
    'clicks_per_generated_match': 'Number of Clicks per Generated Match',
    'select_button_clicks': 'Clicks on "Select" Button (1=yes, 0=no)',
    'time_profile_minutes': 'Time in Minutes - Profile',
    'time_questionnaire_minutes': 'Time in Minutes - Questionnaire'
}

# Mock data from Figure 3
data = {
    'clicks_on_generated_matches': [
        22, 25, 28, 20, 19, 25, 25, 28, 29, 26,
        20, 20, 22, 25, 26, 25, 20, 29, 29, 28
    ],
    'clicks_per_generated_match': [
        3, 4, 2, 2, 2, 1, 1, 1, 1, 4,
        4, 3, 4, 2, 1, 1, 5, 4, 5, 1
    ],
    'select_button_clicks': [
        1, 0, 1, 1, 1, 1, 0, 1, 1, 1,
        0, 0, 1, 1, 1, 1, 1, 1, 0, 1
    ],
    'time_profile_minutes': [
        10.5, 8.0, 12.0, 13.0, 12.5, 9.5, 9.0, 10.5, 11.0, 15.5,
        7.0, 8.5, 9.5, 8.0, 11.0, 12.5, 10.5, 10.0, 9.5, 10.5
    ],
    'time_questionnaire_minutes': [
        15.5, 16.0, 17.5, 17.5, 13.5, 15.0, 14.0, 14.5, 16.5, 17.5,
        14.0, 15.0, 16.0, 15.5, 19.0, 17.0, 16.5, 15.5, 13.0, 14.0
    ]
}


def calculate_statistics(data_array):
    """Calculate statistics for a given data array."""
    arr = np.array(data_array)
    n = len(arr)
    
    mean = np.mean(arr)
    median = np.median(arr)
    min_val = np.min(arr)
    max_val = np.max(arr)
    
    # Calculate 95% confidence interval
    confidence_level = 0.95
    degrees_freedom = n - 1
    standard_error = stats.sem(arr)
    confidence_interval = stats.t.interval(
        confidence_level, 
        degrees_freedom, 
        loc=mean, 
        scale=standard_error
    )
    
    return {
        'mean': mean,
        'median': median,
        'min': min_val,
        'max': max_val,
        'ci_lower': confidence_interval[0],
        'ci_upper': confidence_interval[1],
        'std': np.std(arr, ddof=1),
        'data': arr
    }


def create_mean_median_comparison(all_stats, output_file='mean_median_comparison.png'):
    """Create bar chart comparing mean and median for all metrics."""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    metrics = list(METRIC_LABELS.keys())
    labels = [METRIC_LABELS[m] for m in metrics]
    means = [all_stats[m]['mean'] for m in metrics]
    medians = [all_stats[m]['median'] for m in metrics]
    
    x = np.arange(len(labels))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, means, width, label='Mean', color='steelblue', alpha=0.8)
    bars2 = ax.bar(x + width/2, medians, width, label='Median', color='coral', alpha=0.8)
    
    ax.set_xlabel('Metrics', fontsize=12, fontweight='bold')
    ax.set_ylabel('Values', fontsize=12, fontweight='bold')
    ax.set_title('Mean vs Median Comparison Across All Metrics', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()


def create_confidence_interval_plot(all_stats, output_file='confidence_intervals.png'):
    """Create plot showing means with 95% confidence intervals."""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    metrics = list(METRIC_LABELS.keys())
    labels = [METRIC_LABELS[m] for m in metrics]
    means = [all_stats[m]['mean'] for m in metrics]
    ci_lowers = [all_stats[m]['ci_lower'] for m in metrics]
    ci_uppers = [all_stats[m]['ci_upper'] for m in metrics]
    
    # Calculate error bars
    errors_lower = [means[i] - ci_lowers[i] for i in range(len(means))]
    errors_upper = [ci_uppers[i] - means[i] for i in range(len(means))]
    errors = [errors_lower, errors_upper]
    
    x = np.arange(len(labels))
    
    ax.errorbar(x, means, yerr=errors, fmt='o', markersize=10, 
                capsize=10, capthick=2, color='darkblue', 
                ecolor='steelblue', elinewidth=2, label='Mean with 95% CI')
    
    ax.set_xlabel('Metrics', fontsize=12, fontweight='bold')
    ax.set_ylabel('Values', fontsize=12, fontweight='bold')
    ax.set_title('Mean Values with 95% Confidence Intervals', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()


def create_box_plots(all_stats, output_file='box_plots.png'):
    """Create box plots showing data distribution for all metrics."""
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Data Distribution Box Plots', fontsize=16, fontweight='bold')
    
    metrics = list(METRIC_LABELS.keys())
    
    for idx, metric in enumerate(metrics):
        row = idx // 3
        col = idx % 3
        ax = axes[row, col]
        
        data_array = all_stats[metric]['data']
        
        bp = ax.boxplot([data_array], patch_artist=True, widths=0.6)
        bp['boxes'][0].set_facecolor('lightblue')
        bp['boxes'][0].set_edgecolor('darkblue')
        bp['medians'][0].set_color('red')
        bp['medians'][0].set_linewidth(2)
        
        # Add mean marker
        mean_val = all_stats[metric]['mean']
        ax.plot([1], [mean_val], marker='D', markersize=8, 
                color='green', label='Mean', zorder=3)
        
        ax.set_title(METRIC_LABELS[metric], fontsize=11, fontweight='bold')
        ax.set_ylabel('Values', fontsize=10)
        ax.grid(axis='y', alpha=0.3)
        ax.legend(loc='upper right', fontsize=8)
    
    # Remove the extra subplot
    fig.delaxes(axes[1, 2])
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()


def create_range_visualization(all_stats, output_file='range_visualization.png'):
    """Create visualization showing min, max, and range for each metric."""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    metrics = list(METRIC_LABELS.keys())
    labels = [METRIC_LABELS[m] for m in metrics]
    mins = [all_stats[m]['min'] for m in metrics]
    maxs = [all_stats[m]['max'] for m in metrics]
    means = [all_stats[m]['mean'] for m in metrics]
    
    x = np.arange(len(labels))
    
    # Plot ranges as lines
    for i in range(len(x)):
        ax.plot([x[i], x[i]], [mins[i], maxs[i]], 'o-', linewidth=3, 
                markersize=8, color='steelblue', alpha=0.6)
    
    # Plot means
    ax.scatter(x, means, s=150, marker='s', color='red', 
               label='Mean', zorder=5, edgecolors='darkred', linewidth=2)
    
    ax.set_xlabel('Metrics', fontsize=12, fontweight='bold')
    ax.set_ylabel('Values', fontsize=12, fontweight='bold')
    ax.set_title('Range Visualization (Min, Max, and Mean)', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()


def create_comprehensive_dashboard(all_stats, output_file='statistics_dashboard.png'):
    """Create a comprehensive dashboard with multiple visualizations."""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
    
    # 1. Mean vs Median comparison
    ax1 = fig.add_subplot(gs[0, 0])
    metrics = list(METRIC_LABELS.keys())
    labels = [METRIC_LABELS[m].replace(' ', '\n', 1) for m in metrics]
    means = [all_stats[m]['mean'] for m in metrics]
    medians = [all_stats[m]['median'] for m in metrics]
    
    x = np.arange(len(labels))
    width = 0.35
    ax1.bar(x - width/2, means, width, label='Mean', color='steelblue', alpha=0.8)
    ax1.bar(x + width/2, medians, width, label='Median', color='coral', alpha=0.8)
    ax1.set_title('Mean vs Median', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, fontsize=LABEL_FONT_SIZE, ha='right')
    ax1.legend()
    ax1.grid(axis='y', alpha=0.3)
    
    # 2. Confidence Intervals
    ax2 = fig.add_subplot(gs[0, 1])
    ci_lowers = [all_stats[m]['ci_lower'] for m in metrics]
    ci_uppers = [all_stats[m]['ci_upper'] for m in metrics]
    errors_lower = [means[i] - ci_lowers[i] for i in range(len(means))]
    errors_upper = [ci_uppers[i] - means[i] for i in range(len(means))]
    
    ax2.errorbar(x, means, yerr=[errors_lower, errors_upper], fmt='o', 
                 markersize=8, capsize=8, capthick=2, color='darkblue', 
                 ecolor='steelblue', elinewidth=2)
    ax2.set_title('95% Confidence Intervals', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels, fontsize=LABEL_FONT_SIZE, ha='right')
    ax2.grid(axis='y', alpha=0.3)
    
    # 3. Range visualization
    ax3 = fig.add_subplot(gs[1, 0])
    mins = [all_stats[m]['min'] for m in metrics]
    maxs = [all_stats[m]['max'] for m in metrics]
    
    for i in range(len(x)):
        ax3.plot([x[i], x[i]], [mins[i], maxs[i]], 'o-', linewidth=3, 
                markersize=6, color='steelblue', alpha=0.6)
    ax3.scatter(x, means, s=100, marker='s', color='red', zorder=5, 
                edgecolors='darkred', linewidth=1.5)
    ax3.set_title('Range (Min-Max) with Mean', fontsize=12, fontweight='bold')
    ax3.set_xticks(x)
    ax3.set_xticklabels(labels, fontsize=LABEL_FONT_SIZE, ha='right')
    ax3.grid(axis='y', alpha=0.3)
    
    # 4. Summary statistics table
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.axis('tight')
    ax4.axis('off')
    
    table_data = []
    table_data.append(['Metric', 'Mean', 'Median', 'Min', 'Max', 'Range'])
    
    for metric in metrics:
        metric_label = METRIC_LABELS[metric][:MAX_LABEL_LENGTH] + '...' if len(METRIC_LABELS[metric]) > MAX_LABEL_LENGTH else METRIC_LABELS[metric]
        row = [
            metric_label,
            f"{all_stats[metric]['mean']:.2f}",
            f"{all_stats[metric]['median']:.2f}",
            f"{all_stats[metric]['min']:.2f}",
            f"{all_stats[metric]['max']:.2f}",
            f"{all_stats[metric]['max'] - all_stats[metric]['min']:.2f}"
        ]
        table_data.append(row)
    
    table = ax4.table(cellText=table_data, cellLoc='center', loc='center',
                      colWidths=[0.3, 0.14, 0.14, 0.14, 0.14, 0.14])
    table.auto_set_font_size(False)
    table.set_fontsize(LABEL_FONT_SIZE)
    table.scale(1, 2)
    
    # Style header row
    for i in range(TABLE_COLUMNS):
        table[(0, i)].set_facecolor('#4472C4')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Alternate row colors
    for i in range(1, len(table_data)):
        for j in range(TABLE_COLUMNS):
            if i % 2 == 0:
                table[(i, j)].set_facecolor('#E7E6E6')
    
    ax4.set_title('Summary Statistics', fontsize=12, fontweight='bold', pad=20)
    
    fig.suptitle('Mock Data Statistics Dashboard', fontsize=16, fontweight='bold')
    
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()


def main():
    """Main function to generate all visualizations."""
    print("\n" + "="*70)
    print("GENERATING STATISTICS VISUALIZATIONS")
    print("="*70)
    print("\nCalculating statistics for all metrics...")
    
    # Calculate statistics for all metrics
    all_stats = {}
    for metric_key in METRIC_LABELS.keys():
        all_stats[metric_key] = calculate_statistics(data[metric_key])
    
    print("\nGenerating visualizations...")
    print("-" * 70)
    
    # Generate all visualizations
    create_comprehensive_dashboard(all_stats)
    create_mean_median_comparison(all_stats)
    create_confidence_interval_plot(all_stats)
    create_box_plots(all_stats)
    create_range_visualization(all_stats)
    
    print("-" * 70)
    print("\n✓ All visualizations generated successfully!")
    print("\nGenerated files:")
    print("  1. statistics_dashboard.png - Comprehensive overview")
    print("  2. mean_median_comparison.png - Bar chart comparison")
    print("  3. confidence_intervals.png - 95% CI visualization")
    print("  4. box_plots.png - Distribution box plots")
    print("  5. range_visualization.png - Min/Max range chart")
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    main()
