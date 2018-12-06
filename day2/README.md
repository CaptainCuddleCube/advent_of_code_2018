# How to run these functions
I was lazy, so I read the data into python by command line args.

Since there 200 odd rows of data, you can use cat and then xargs to get the data in. 

to run task1 : 
`cat task.data | xargs python task1.py` 
to run task2 : 
`cat task.data | xargs python task2.py` 