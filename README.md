# BioM
__BIOM:__ Biometric In-Out Monitor

## Rules
1. `Auto-logout`: If a person doesn't __punch-out__, it will either 
	- [ ] __auto-logout__ within 2 mins, OR
	- [ ] ignore the entry  

	This will force employees to __punch-out__, otherwise they lose the total duration of stay inside Fab. 

## Cases (Good/Bad)
* __Good__

| Emp Code | Emp Name | Section	| Reader | Date |	Time | Status |
|---------|----------|---------|--------|------|------|--------|
| CL00102	| ABHIJIT ROY |	DRY	| M FAB - 1 |	26/06/2019 |	10:03:09 |	ACCESS GRANTED BIO |
| CL00102	| ABHIJIT ROY |	DRY	| M FAB		  |	26/06/2019 |	10:43:46 |	ACCESS GRANTED BIO |
| CL00102	| ABHIJIT ROY |	DRY	| M FAB - 1	| 26/06/2019 |	11:17:28 |	ACCESS GRANTED BIO |
| CL00102	| ABHIJIT ROY |	DRY	| M FAB		  | 26/06/2019 |	12:16:31 |	ACCESS GRANTED BIO |

* __Bad__

| Emp Code | Emp Name | Section	| Reader | Date |	Time | Status |
|---------|----------|---------|--------|------|------|--------|
| VS13984 |	NAVIN KESSOP | 	MFD |	M FAB - 1 |	26/06/2019 | 12:11:27 |	ACCESS GRANTED BIO |
| VS13984 |	NAVIN KESSOP | 	MFD |	M FAB	    | 26/06/2019	| 13:43:30	| ACCESS GRANTED BIO |
| VS13984 |	NAVIN KESSOP | 	MFD |	M FAB - 1	| 26/06/2019	| 14:47:52 | ACCESS GRANTED BIO |

* __Bad__

| Emp Code | Emp Name | Section	| Reader | Date |	Time | Status |
|---------|----------|---------|--------|------|------|--------|
| CL00017 |	ANIL SHARMA | TDD |	M FAB |	26/06/2019 | 00:38:47	| ACCESS GRANTED BIO |
| CL00017 |	ANIL SHARMA | TDD |	M FAB - 1 |	26/06/2019 |	03:13:02 |	ACCESS GRANTED BIO |
| CL00017 |	ANIL SHARMA | TDD |	M FAB	| 26/06/2019	| 03:39:04 |	ACCESS GRANTED BIO |

* __Bad__

| Emp Code | Emp Name | Section	| Reader | Date |	Time | Status |
|---------|----------|---------|--------|------|------|--------|
| LM67248 |	MUKUND PANDEY | TDD	| M FAB - 1 |	26/06/2019 | 14:15:12 |	ACCESS GRANTED BIO |
| LM67248 |	MUKUND PANDEY | TDD	| M FAB - 1 |	26/06/2019 | 14:17:57 |	ACCESS GRANTED BIO |

* __Bad__

| Emp Code | Emp Name | Section	| Reader | Date |	Time | Status |
|---------|----------|---------|--------|------|------|--------|
| CL00075 |	ANURUDHA SHUKLA |	VFDQC	| M FAB - 1 |	26/06/2019 | 14:23:42 |	ACCESS GRANTED BIO |


## References
* Plotly dot plots - https://plot.ly/python/dot-plots/
