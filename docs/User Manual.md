# Biometric In-Out Monitor (BIOM) 
## Modules
* ### Filter, Clean
	- extract desired columns
	- remove unwanted, repetitive rows (also, column headers)
* ### Fetch Employee details
	- fetch the data of employee code, name, section
	- clean: strip the `space` from the end of employee name
* ### Assign Section
	- assign section corresponding to each employee, if found in the record.
