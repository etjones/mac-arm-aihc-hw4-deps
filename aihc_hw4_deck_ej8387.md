autoscale: true
theme: next, 1

## AI In Healthcare, Homework 4: Mimic NLP
### [Evan Jones](mailto:evan_jones@utexas.edu), UT ID:  `ej8387`


---

# First: Extract Laryngomalacia notes:

```sql
SELECT * FROM noteevents WHERE LOWER(TEXT) LIKE '%laryngomalacia%';
```

**Results:** 93 rows, 10 seconds on my local SQLite database.
