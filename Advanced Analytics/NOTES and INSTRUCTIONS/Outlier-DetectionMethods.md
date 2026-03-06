#Outlier Detection Methods
1. **IQR Method** - Uses Q1,Q3 and IQR to find extreme values
			- Values<Q1-1.5xIQR or >Q3=1.5xIQR
			- Very common for skewed data
1. **Z-Score Method** - Measures how many standard deviations a value is from the mean
				- Zscore <-3 or >+3
				- Best for normally distributed data