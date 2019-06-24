## Fitness Tracker Survival Analysis

### Business Understanding
Fitness has always been a topic of interest to me and I am fairly active when it comes to staying in shape. Part of that journey involves the consistency of tracking nutritional intake. One of the most popular apps today is MyFitnessPal, which tracks this on a daily basis. I would like to take a deeper dive into analyzing trends in the foods that people eat while trying to obtain a goal to increase, lose, or maintain weight.

1. What is the average amount of time that MyFitnessPal users use the app, and do they use it consistently throughout?
2. Do users still keep using the program after meeting or not meeting their goal?

### Data Understanding
I had requested access to an API through an online source for exploratory and educational purposes. This dataset contains 587,187 days of food diary records logged by 9.9K MyFitnessPal users from September 2014 through April 2015.  Each line is a tab-separated list of: 

- Anonymized user ID
- Diary date
- List of food entries and nutrients (as JSON objects)
- Daily aggregate of nutrient intake and goal (as JSON objects). 

### Data Preparation
The total size of the data file is approx. 2.2 GB, which I plan to store in a postgreSQL database. I will then use SQL to pull any necessary data into jupyter notebook to create my models.

### Modeling
I was planning on creating a time series analysis on the data to see how long each unique user has used the app, in addition to, a survival analysis model using the first 2 weeks of data to understand if they will continue to use the app, whether or not they have met their goal. Another step would be to include clustering with K-Means to categorize a group a users.

Target: 

1. Met goal within 5%
2. Streak of days


### Evaluation


### Deployment
A written detailed analysis of results documented in github and or medium.
