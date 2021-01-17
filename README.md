# opening_hours

# Set up project

I have used virtualenv and flask so I can quickly have functional http api with some swagger. To install this you need 
to have virtual env and activate it and install requirements from requirements.txt file
to run the project you can simply run(inside virtualenv) 

``` shell
git clone https://github.com/bulinjoli/opening_hours.git
cd openinghours
virtualenv openinghours
source openinghours/bin/activate
pip3 install -r requirements.txt
flask run
```

for testing purposes I have used postman where it was running on
http://127.0.0.1:5000/opening_hours


Part 2 : Tell us what do you think about the data format. Is the current JSON structure the
best way to store that kind of data or can you come up with a better version? There are no
right answers here 🙂. Please write your thoughts to readme.md.

Answer: Current format is ok, regarding understanding the data. It is nicely structured and you can easily understand
the data which is important. But, I have to say it is not that easy for working with, especially with all the edge cases.
I like to keep things small and simple so for me json like this:
 
	 {
	 "day" : "tuesday"
	 "type" : "open",
	 "value" : 36000
	 },
	 {
	 "day" : "tuesday"
	 "type" : "close",
	 "value" : 64800
	 },
	 {
	 "day" : "thursday",
	 "type" : "open",
	 "value" : 36000
	 },
	 {
	 "day" : "thursday",
	 "type" : "close",
	 "value" : 64800
	 },
	 {
	 "day" : "thursday",
	 "type" : "open",
	 "value" : 64800
	 },
	 {
	 "day" : "thursday",
	 "type" : "close",
	 "value" : 84800
	 },
     {
     "day" : "friday",
     "type" : "open",
     "value" : 36000
     },
     {
     "day" : "saturday",
     "type" : "close",
     "value" : 36000
     },
     {
     "day" : "saturday",
     "type" : "open",
     "value" : 36000
     },
     {
     "day" : "sunday",
     "type" : "close",
     "value" : 36000
     },
     {
     "day" : "sunday",
     "type" : "open",
     "value" : 43200
     },
     {
     "day" : "sunday",
     "type" : "close",
     "value" : 75600
     }


Is much easier to handle, process, validate and store in db. And still I think it is understandable enough. 