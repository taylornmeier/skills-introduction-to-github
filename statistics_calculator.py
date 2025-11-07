#!/usr/bin/env python3
"""
Statistics Calculator for Mock Data

This script calculates and displays statistics for each metric in the mock data:
- Mean and Median
- Range (Min and Max)
- 95% Confidence Interval
"""

import numpy as np
from scipy import stats


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


def calculate_statistics(data_array, metric_name):
    """
    Calculate statistics for a given data array.
    
    Parameters:
    -----------
    data_array : list or numpy array
        The data to analyze
    metric_name : str
        Name of the metric for display purposes
    
    Returns:
    --------
    dict : Dictionary containing all calculated statistics
    """
    arr = np.array(data_array)
    n = len(arr)
    
    # Calculate mean and median
    mean = np.mean(arr)
    median = np.median(arr)
    
    # Calculate range
    min_val = np.min(arr)
    max_val = np.max(arr)
    
    # Calculate 95% confidence interval
    # Using t-distribution for small sample sizes
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
        'n': n
    }


def print_statistics(metric_name, stats_dict):
    """
    Print statistics in a formatted way.
    
    Parameters:
    -----------
    metric_name : str
        Name of the metric
    stats_dict : dict
        Dictionary containing calculated statistics
    """
    print(f"\n{'='*70}")
    print(f"Statistics for: {metric_name}")
    print(f"{'='*70}")
    print(f"Sample Size (n):          {stats_dict['n']}")
    print(f"\nCentral Tendency:")
    print(f"  Mean:                   {stats_dict['mean']:.4f}")
    print(f"  Median:                 {stats_dict['median']:.4f}")
    print(f"\nRange:")
    print(f"  Minimum:                {stats_dict['min']:.4f}")
    print(f"  Maximum:                {stats_dict['max']:.4f}")
    print(f"  Range:                  {stats_dict['max'] - stats_dict['min']:.4f}")
    print(f"\n95% Confidence Interval:")
    print(f"  Lower Bound:            {stats_dict['ci_lower']:.4f}")
    print(f"  Upper Bound:            {stats_dict['ci_upper']:.4f}")
    print(f"  CI Width:               {stats_dict['ci_upper'] - stats_dict['ci_lower']:.4f}")


def main():
    """
    Main function to calculate and display statistics for all metrics.
    """
    print("\n" + "="*70)
    print("MOCK DATA STATISTICS ANALYSIS")
    print("="*70)
    print("\nAnalyzing 5 metrics from 20 observations:")
    print("  1. Clicks on generated matches")
    print("  2. Number of clicks per generated match")
    print("  3. Clicks on 'Select' button (1=yes, 0=no)")
    print("  4. Time in minutes - Profile (rounded to nearest 0.5)")
    print("  5. Time in minutes - Questionnaire (rounded to nearest 0.5)")
    
    # Calculate and display statistics for each metric
    metric_labels = {
        'clicks_on_generated_matches': 'Clicks on Generated Matches',
        'clicks_per_generated_match': 'Number of Clicks per Generated Match',
        'select_button_clicks': 'Clicks on "Select" Button (1=yes, 0=no)',
        'time_profile_minutes': 'Time in Minutes - Profile',
        'time_questionnaire_minutes': 'Time in Minutes - Questionnaire'
    }
    
    all_stats = {}
    
    for metric_key, metric_label in metric_labels.items():
        stats_dict = calculate_statistics(data[metric_key], metric_label)
        all_stats[metric_key] = stats_dict
        print_statistics(metric_label, stats_dict)
    
    # Print summary table
    print(f"\n{'='*70}")
    print("SUMMARY TABLE")
    print(f"{'='*70}")
    print(f"{'Metric':<40} {'Mean':<10} {'Median':<10}")
    print(f"{'-'*70}")
    
    for metric_key, metric_label in metric_labels.items():
        mean = all_stats[metric_key]['mean']
        median = all_stats[metric_key]['median']
        print(f"{metric_label:<40} {mean:<10.2f} {median:<10.2f}")
    
    print(f"\n{'='*70}\n")


if __name__ == "__main__":
    main()
