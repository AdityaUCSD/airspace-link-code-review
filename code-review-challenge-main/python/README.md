# Python Code Review Challenge

Please review the "count_records_in_bounds" function in the code_review.py file. Pretend that a junior engineer 
just sent this over in a pull request. There are some obvious and not so obvious bugs, performance issues, etc in 
the code. What suggestions would you make to the junior engineer?

## Setup
1. The requirements.txt should provide all libraries necessary to run this code locally.

2. Please execute the fake_data_setup.py file to produce a dataset to use for running locally. Note: 
The "count_records_in_bounds" function is expected to be run on a csv with 10_000_000 records.


## Ticket
Create a process for calculating the following information from input csv file:
* Total number of positions within the bounds
* Category with the most positions within the bounds
* Category with the least positions within the bounds

The CSV file has the following attributes:
* geometry (wkt point z) - A point location of things
* id (int) - Record identifier
* color (string) - A category