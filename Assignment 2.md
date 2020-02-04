### Assignment 2

#### Introduction

Amir Tahmasbi, who was at that time a PhD student at Simon Fraser University, was willing to learn about the qualifications required for getting hired as a software developer in Amazon. So, he decided to do a small project, scraping the Amazon job portal at `amazon.jobs`. He captured all of the job data from that site by visiting every job page and applying the Selenium and BeautifulSoup Python packages. In total, he collected data from 3,493 job postings.

Amir took only the job title, the job location, the job posting date, the job responsibilities and the minimum and preferred qualifications for the software development role. The data are collected in the file `skills_amazon.csv`.

#### Questions

1. How old are the postings? To describe the trend in the number of uncovered positions, plot the monthly number of postings.

2. Suppose that a software developer is interested in finding a position in India. Does Amazon have something for him/her? In which locations?

3. Create a function `f` which calculates the number of missing values in a Pandas series. Using the command `df.apply(f, axis=0)` calculate that number for every column of the data set. Discard the postings with missing data for the forthcoming questions.

4. Which programming languages are more often mentioned in the basic qualifications for these positions? Perhaps Java or Python? Which flavor of C is preferred, C++ or C#? Is it SQL still demanded?

5. What about operating systems? Is the knowledge of Linux or Unix explicitly mentioned?

6. Is having a degree in Computer Science a requirement for these positions?

#### Submission

1. Submit a text file containing the responses to these questions and the Python code used to respond every question.

2. Put your name on top of the document.

#### Deadline

February 9 (Sunday), 24:00.
