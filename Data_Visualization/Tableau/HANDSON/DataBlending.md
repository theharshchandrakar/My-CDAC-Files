#Data Blending is a technique to combine the data coming from different sources like SQL NOSQL, Excel, JSON, Text etc.

 Data blending uses two types of data sources-

- Primary
- Secondary

#####First data source selected for blending process is considered as Primary and all other data sources are considered Secondary.


#####In every blending, there is only one Primary data source. But there can be multiple secondary.


Primary data source - Blue color
Secondary data source - Orange color

---

## Steps to make Data Blening
1. Open a file (default)
- Ctrl+D -> Select 2nd file
	(It may appear to be gone, but it is stored in internal memory, go to sheets and see for yourself.)
- Go to Sheets
- Drag something on a Data source
	- if it has a red mark, its marked as Secondary
	- u have to click sec and click chain icon to make it secondary, then try previous step
	- if it has Blue Tick it becomes Primary
- Do the same thing on other sheets

#####cannot create geo chart if geo data comes from secondary source

#####Data blending in Tableau simulates a left join operation. (interview question)

#####Data blending in Tableau simulates a left join operation. 

Three types of LOD: 

- FIXED
- INCLUDE
- EXCLUDE (write in capital)



1. Create a LOD to show revenue values for Category.

LOD-Actual Revenue by category
- { FIXED [Category] : 
SUM([Actual Revenue])
}


LOD - Grand total by Revenue
{ FIXED :
SUM([Actual Revenue])
}


