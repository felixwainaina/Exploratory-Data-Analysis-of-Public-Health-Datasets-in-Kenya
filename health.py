import streamlit as st
import pandas as pd
import numpy as np

# Load your cleaned data
# cleaned_data = pd.read_csv('path_to_your_cleaned_data.csv')

# Sample data creation (replace this with your actual cleaned_data)
# cleaned_data should have columns: 'GHO (DISPLAY)', 'YEAR (DISPLAY)', 'Numeric Value', 'REGION (DISPLAY)'
cleaned_data = pd.DataFrame({
    'GHO (DISPLAY)': [
        'HIV Prevalence Among Adults Aged 15 to 49 (%)', 
        'HIV Prevalence Among Adults Aged 15 to 49 (%)', 
        'Malaria Incidence', 
        'Malaria Incidence',
        'Tuberculosis Incidence (per 100,000 population)',
        'Tuberculosis Incidence (per 100,000 population)',
        'Hepatitis B Immunization Coverage Among 1-Year-Olds (%)',
        'Hepatitis B Immunization Coverage Among 1-Year-Olds (%)',
        'Measles Vaccination Coverage Among 1-Year-Olds (%)',
        'Measles Vaccination Coverage Among 1-Year-Olds (%)'
    ],
    'YEAR (DISPLAY)': [2010, 2011, 2010, 2011, 2010, 2011, 2010, 2011, 2010, 2011],
    'Numeric Value': [5.0, 4.5, 10.0, 9.0, 150.0, 145.0, 80.0, 85.0, 70.0, 75.0],
    'REGION (DISPLAY)': ['Africa', 'Africa', 'Africa', 'Africa', 'Africa', 'Africa', 
                         'Africa', 'Africa', 'Africa', 'Africa']
})

# Function to calculate confidence intervals (dummy implementation)
def confidence_interval(indicator):
    # Replace with actual logic to calculate confidence intervals based on your data
    return np.random.uniform(1.0, 3.0), np.random.uniform(3.0, 5.0)

# Streamlit App Layout
st.title("Public Health Data Dashboard")

# Dropdown for selecting indicators
indicator_options = cleaned_data['GHO (DISPLAY)'].unique()
selected_indicator = st.selectbox("Select an Indicator", indicator_options)

# Trend Graph
st.subheader(f'Trend of {selected_indicator} Over Years')
trend_data = cleaned_data[cleaned_data['GHO (DISPLAY)'] == selected_indicator]
st.line_chart(trend_data.set_index('YEAR (DISPLAY)')['Numeric Value'])

# Regional Comparison Graph
st.subheader(f'{selected_indicator} by Region')
regional_data = cleaned_data[cleaned_data['GHO (DISPLAY)'] == selected_indicator]
st.bar_chart(regional_data.groupby('REGION (DISPLAY)')['Numeric Value'].mean())

# Confidence Interval Output
ci_low, ci_high = confidence_interval(selected_indicator)
st.write(f'Confidence Interval for {selected_indicator}: ({ci_low:.2f}, {ci_high:.2f})')

# Run the app with the command: streamlit run your_script.py
