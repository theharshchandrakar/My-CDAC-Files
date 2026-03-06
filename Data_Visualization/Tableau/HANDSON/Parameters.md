#Parameters in Tableau - 
##Reuseablity - once we set parameter we can use it on other projects to apply the same format
Two Types of parameters -

- Regualr parameter
- Reference line parameter

min - 4000
max - 20000
increase by 1000
Quantity range parameter



Create vertical bar chart of region & quantity. Add reference line with quantity range parameter. show bars above & below parameter value in different colors using calculated field.




#Create Parameters with measure & dimension names
- Revenue
- Profit
- Shipping Cost
- Quantity

### if it is quantity show as it is but if it is profit, Revenue, shipping cost we shows in $, so it will make conflict

create a tree map using region calculated field that we created show select major in green color, show the label also

Category
Segment
Ship Mode
Order Priority

1. Create a new parameter "select dimension name" of string data type with above 4 values.
1. Then create calculated field "show selected Dimension" using this parameter.