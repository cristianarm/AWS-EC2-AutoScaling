# AWS-EC2-AutoScaling Stress Test Script
A python script to stress test an EC2 instance to trigger auto scaling based on % of CPU utilization


## Running the script
You need to have python3 installed to run the script.

Set the environment variable **STRESS_MINS** to desired time to stress test by exporting it into your session. 
  eg: **export STRESS_MINS=10** sets the time to run the script for 10 mins.

**Note**: if the environment variable **STRESS_MINS** does not exist, it takes as default value 10.

**Note**: that the sctipt will stop running by it's self after 1hr ow whatever timeout you set.

Run the script by typing **python3 stress_test.py**
