#Table calculations - 
####White Triangle = Table Calculation
##DONOT SORT TABLE CALCULATIONS!!!

1. Running Total ()
- Difference (In difference negative means not a loss, its means it negative from previous month/year)
- % Difference
- Rank (Doesnt require date field)
- Moving Average
- YoY Growth

---
#Moving Average 
- Line smoothening technique 
- reduces short term changes in the data

Default moving average in Tableau is 3 period moving average (average of current & 2 previous values)

##Tableau allow you to modify the default table calculation...

#YoY Growth

YoY (Year-over-Year) growth is the percentage change in a metric from one period to the same period in the previous year, used to measure annual performance and remove seasonal effects.

It is calculated using the formula: ((Current Period Value - Previous Period Value) / Previous Period Value) x 100. This metric is used to track financial performance, like revenue or profit, and other business metrics like user acquisition or website traffic. 

---
###Problem Statements
1. Create monthly difference table calculation for shipping cost.
- Create 5 period MA of monthly profit and compare with og values
- Quarterly Quantity YoY Growth (add two filters - Category & Segment)
- Quarterly No. of orders YoY Growth (add sub-cat filter)