# Film recommendation system

A system for recommending film using linear regression and collaborative filtering

# How does collaborative filtering work ?

- Collaborative filtering core concept is that, users with similar pattern will likely to make similar decision in the future, which therefore being able to give more dimensional prediction than content based filtering, which focus only on the characteristics of the decisions
- And in the context of film recommendation, the decision here is the rating of the movies and users who has the similar rating to the same movies will likely to have similar ratings in the future

## Formulas

### Cosine similarity

We use cosine similarity to calculate the angle between 2 vector which in the context of film recommendation, the vector is a multi dimension vector consist of using rating for each movie (e.g [1,2,5,0])

$$
\text{cosine\_similarity}(\vec{A}, \vec{B}) = \frac{\sum\limits_{i=1}^{n} A_i B_i}{\sqrt{\sum\limits_{i=1}^{n} A_i^2} \sqrt{\sum\limits_{i=1}^{n} B_i^2}}
$$

### Predict rating

- Now with the cosine similarities, we can use them as weight to reflect how other users score affect the target user (bigger cosine similarity = more influence on the predicting rating)

$$
\hat{r}_{u,i} = \bar{r}_u + \frac{\sum\limits_{v \in N(u)} \text{sim}(u,v) \cdot (r_{v,i} - \bar{r}_v)}{\sum\limits_{v \in N(u)} |\text{sim}(u,v)|}
$$
