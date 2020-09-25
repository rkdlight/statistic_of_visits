## Program that calculates the total time spent by all people for each day

#### Format of input data

```
<?xml version="1.0" encoding="UTF-8"?>
<people>
	<person full_name="i.ivanov">
		<start>21-12-2011 10:00:00</start>
		<end>21-12-2011 19:00:00</end>
	</person>
	<person full_name="a.stepanova">
		<start>22-12-2011 09:30:00</start>
		<end>22-12-2011 17:30:00</end>
	</person>
	<person full_name="u.petrov">
		<start>23-12-2011 16:00:00</start>
		<end>23-12-2011 22:00:00</end>
	</person>
	<person full_name="i.ivanov">
		<start>23-12-2011 08:20:00</start>
		<end>23-12-2011 14:40:00</end>
	</person>
</people>
```

#### Quick start

Clone the repository

`git clone https://github.com/rkdlight/statistic_of_visits.git`

Install requirements 

`pip install -r requirements.txt`

Start tests

`python -m unittest -v tests/test_statistic.py`

Use program

`python statistic.py data.xml -s 21-12-2011 -e 24-12-2011 -n i.ivanov`