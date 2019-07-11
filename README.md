## MFP Nutrition Survival Analysis
**Created by:** Andy Luc	                                        
**Slide Deck Presentation:** [MFP Nutrition Survival Analysis.pdf](https://github.com/rokaandy/nutritional_survival_analysis/blob/master/MFP%20Nutrition%20Survival%20Analysis.pdf)

### Business Understanding
Fitness has always been a topic of interest to me and I am fairly active when it comes to staying in shape. Part of that journey involves the consistency of tracking nutritional intake. One of the most popular apps today is MyFitnessPal, which tracks this on a daily basis.

Based on only user inputs of daily food intake and a target goal:

1. Can we predict when or if a user decides to churn or quit using the app?
2. Is there a certain nutritional item that contributes to a user quitting the platform?

### Data Understanding
I had requested access to an API through an online source for exploratory and educational purposes. This dataset contains 587,187 days of food diary records logged by 9.9K MyFitnessPal users from September 2014 through April 2015.  Each line is a tab-separated list of: 

- Anonymized user ID
- Diary date
- List of food entries and nutrients (as JSON objects)
- Daily aggregate of nutrient intake and goal (as JSON objects).

Note: As the MyFitnessPal API used in this repository is confidential, please visit the following website to request access: `https://larc.smu.edu.sg/myfitnesspal-food-diary-dataset`

### Data Preparation
The API was provided as a .tsv file, which I had initially read into a pandas dataframe. With exception to the userid and date, it contained nested lists of dictionaries which had to be parsed. Once parsed into a number of corresponding columns, a timeline of the data was created to determine whether or not a user has churned. Knowing that the dataset has daily inputs, I could find out how many days a user has used the app by grouping the userid's.

As part of the exploratory data analysis before any modeling was done, I made a heatmap in seaborn to show the collinearity of the features.

I have included a pickle file named `svl.pkl` near the modeling stage of the notebook to use. 

### Modeling
The initial model uses Logistic Regression.

Subsequently, I used the Cox Proportional Hazards Model in survival regression to analyze the p-value and coefficients of each feature. Also, to see where certain features over a period of time affect the churn rate.

### Evaluation
The Logistic Regression Model was evaluated with a F1-score of 0.85, which represents the harmonic mean of precision and recall. I also scored it with a ROC Curve, achieving an AUC = 0.70. The "Area Under The Curve" tells us how well the model does in identifying true positives and false positives or in other words, how well it can distinguish between 0's as 0's and 1's as 1's (users still using the app or have churned).
![ROC Curve](https://github.com/rokaandy/mfp-nutrition-survival-analysis/blob/master/png/roc.png)

### Deployment
The basis of my modeling was mainly to be used with the internal business team, and not necessarily something to set a user interface with. However, I did create a webpage using flask with a pickled model that users can easily interact with to present probability of users on MyFitnessPal churning or not.

#### Using Flask locally (with Logistic Regression Model):
1. `pip install Flask`
2. In console of the main directory, type: `FLASK_APP=webapp.app flask run`
3. Open a web browser
4. Type: `http://localhost:5000`
5. To test, all spaces must be filled in to make a prediction

### Next Steps
- Write a blog to enhance the knowledge behind survival analysis, which many businesses can benefit from as it is a common problem.
- Cluster using K-Means to find similarly related groups based only on user inputs.
