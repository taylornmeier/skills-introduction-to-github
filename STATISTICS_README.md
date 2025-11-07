# Statistics Calculator

This Python script calculates statistical measures for mock data from a user study and provides comprehensive visualizations.

## Features

The scripts calculate the following statistics for each metric:

- **Central Tendency**: Mean and Median
- **Range**: Minimum, Maximum, and Range (Max - Min)
- **95% Confidence Interval**: Lower bound, Upper bound, and CI width

## Metrics Analyzed

The scripts analyze 5 metrics from 20 observations:

1. **Clicks on Generated Matches**: Number of clicks on generated matches
2. **Number of Clicks per Generated Match**: Average clicks per match
3. **Clicks on "Select" Button**: Binary indicator (1=yes, 0=no)
4. **Time in Minutes - Profile**: Time spent on profile (rounded to nearest 0.5 min)
5. **Time in Minutes - Questionnaire**: Time spent on questionnaire (rounded to nearest 0.5 min)

## Requirements

- Python 3.7 or higher
- NumPy >= 1.24.0
- SciPy >= 1.10.0
- Matplotlib >= 3.7.0 (for visualizations)

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Text-Based Statistics

Run the statistics calculator to get detailed text output:

```bash
python3 statistics_calculator.py
```

Or make it executable and run directly:

```bash
chmod +x statistics_calculator.py
./statistics_calculator.py
```

### Visualizations

Generate comprehensive graphs and charts:

```bash
python3 visualize_statistics.py
```

This will create the following visualization files:

1. **statistics_dashboard.png** - Comprehensive 4-panel dashboard
2. **mean_median_comparison.png** - Bar chart comparing mean vs median
3. **confidence_intervals.png** - Error bar plot with 95% confidence intervals
4. **box_plots.png** - Box plots showing data distribution
5. **range_visualization.png** - Min/max range with mean markers

## Output

### Text Output (statistics_calculator.py)

The script produces:

1. **Detailed Statistics** for each metric including:
   - Sample size
   - Mean and median values
   - Minimum, maximum, and range
   - 95% confidence interval with bounds and width

2. **Summary Table** showing mean and median for all metrics in a compact format

### Visual Output (visualize_statistics.py)

The visualization script generates:

1. **Dashboard**: 4-panel comprehensive view with mean/median comparison, confidence intervals, range visualization, and summary table
2. **Bar Charts**: Side-by-side comparison of mean and median values
3. **Error Plots**: Mean values with 95% confidence interval error bars
4. **Box Plots**: Distribution visualization for each metric
5. **Range Charts**: Visual representation of min, max, and mean

## Statistical Methods

- **Mean**: Arithmetic average of all values
- **Median**: Middle value when data is sorted
- **95% Confidence Interval**: Calculated using the t-distribution (appropriate for small sample sizes)
  - Formula: CI = mean ± t(α/2, n-1) × SE
  - Where SE is the standard error of the mean

## Example Output

### Text Output

```
======================================================================
Statistics for: Clicks on Generated Matches
======================================================================
Sample Size (n):          20

Central Tendency:
  Mean:                   24.5500
  Median:                 25.0000

Range:
  Minimum:                19.0000
  Maximum:                29.0000
  Range:                  10.0000

95% Confidence Interval:
  Lower Bound:            22.9325
  Upper Bound:            26.1675
  CI Width:               3.2350
```

### Visual Output

The visualization script creates publication-quality graphs showing:
- Bar charts for easy comparison
- Error bars for statistical significance
- Box plots for distribution analysis
- Comprehensive dashboards for overview

## Mock Data Source

The data analyzed by these scripts comes from Figure 3 in the problem statement, containing 20 observations across 5 different metrics related to user interactions and time measurements.
