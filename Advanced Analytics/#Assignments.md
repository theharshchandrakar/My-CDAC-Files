#Assignments
---
1. Do outlier analysis on total bill column of tips dataset.

-  Do outlier analysis on age column of titanic dataset.

-  Do skewness analysis and plotting for 'on-board Service' column of 'airline passenger service' dataset. Also find CoV for first time versus returning customers for the 'Ease of online booking' column.

-  Pandas practice

	Use titanic csv dataset.

	1. Do Exploratory Data Analytics (EDA) on the dataset. (Hint: head(), columns, etc)
	2. Find passengers whose age is between 20 and 2.
	3. Find passengers where gender is female and passenger class is 1.
	4. Find average age of female and male passengers.
	5. Count number of passengers in each passenger class.
	6. Separate passengers who survived (survived column contains 0) and who did not survive (survived column contains 1) into two separate dataframes.
	7. For the above two dataframes, find number of females and males.
	8. Sort the original dataframe on age in descending order and display the top 3 records.
	
	Note : If u want to convert any columns data type to integer, use this:
	
	###df['age'] = df['age].astype('Int64')
	
	To rename columns :
	
	###df.rename(columns={'age':'passenger_age','pclass':'Class'}, inplace = True)
	
- Do correlation and covanance analysis and visualization on the 'social media' usage separately for facebook and instagram users, Columns to be used: daily minutes per day and posts per day.

- Combine the 3 marathon datasets (Hint: df pd.concat([df_2015, df_2016, of_20171) ). Then do a correlation analysis on 'Official time" (l.e. time taken to complete the race) and 'pace' (i.e. average pace per minute in km) columns. Draw sacatter plot and heatmap

- Use dataset https://www.kaggle.com/datasets/amirhosseinmirzaie/americancitizenincome
	Perform simple, systematic, stratified, cluster sampling.

	Additional requirements:

	- Ensure that we only have 10% of the overall dataframe records in each case. So, remove extra records, if necessary.
	- For stratified, use strata as race.
	- For cluster, use clusters as martial status.
	Then for overall data and for the four samples, find out the average education.num and average fnlwgt. Which of the four sampling methods is the closest to the overall average in the two cases?

- Assignment: Combine datasets:

	Men ODI Team Match Results-20th Century.csv
	
	Men ODI Team Match Results -21st Century.csv
	
	Find the historical win rate of India.
	
	Now India is scheduled to play 60 ODI matches over the next 3 years.
	
	(a) What is the probability that India wins exactly 35 out of these 60 matches?
	
	(b) What is the probability that India wins more than 40 matches?
	
	(c) What is the probability that India wins at least 45 matches?
	
	(d) What is the most likely number of wins India will have in 60 matches?
1.  8th question remaining, Satish WHatsapp.

1. Calculate Z-scores and do outlier analysis on

	- Glucose column of Diabetes dataset
	- Billionaires dataset


1. A courier company delivers parcels in a particular area in 30 minutes. A new GPS system
	installed has reduced the average time to 28 minutes, when 100 trucks were studied, with a
	sample standard deviation of 4.2 minutes. Run a two-tailed test and a one-tailed (left-tailed) 	test.

1. A battery manufacturer claims that a battery which used run for 30 hours now runs for more thai
	30 hours due to new technology. 200 batteries were studied. Average battery time was found to b
	29.5 hours with a standard deviation of 8 hours. Run a one-tailed (right-tailed) test.

1. For the three combined Marathon datasets, extract the top 25 records with lowest
	finish time (Official Time column). Check the null hypothesis HO = The average finishing time of thi
	lop 25 athletes is 130 minutes. Test it for a = 1%, 5%, and 10%.

1. For combined Marathon datasets, find if younger (age <= 30) and older (age > 30)
	athletes have a similar average pace.

1. Fir StudentsPerformance.csv, using ANOVA find if there is a significant difference in Maths marks depending on the level of parental education.

---

# Assignment 3

1. Predict weight using height in weigh-height.csv dataset. (Linear Regression)


1. Perform Naive Bayes Classification and Logistic Regression to predict if a bank customer would "churn" (i.e. close bank account) using dataset "Bank Customer Churn Prediction". Perform encoding and scaling as appropriate. Handle nulls, if present.

1. Use dataset
kaggle->tejashvi14/travel-insurance-prediction-data
Predict 'customer travel insurance purchase' column.
Perform scaling, encoding, null handling, as neccessary.

1. Perform Time Series Analysis on
	1. Monthly Cola Production in Australia
	2. ice cream sales
	3. USD to INR
	   datsets

1. Assignment PCA

Perform PCA and then logistic regression on loan_approval_dataset.csv file.