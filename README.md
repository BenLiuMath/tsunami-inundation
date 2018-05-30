# tsunami-inundation

Team members:

- Kellie MacPhee
- Brian de Silva
- Abe Engle
- Ben Liu

**Abstract**: *Numerical simulations conducted by researchers at the University of Washington are used to model and predict the impact of tsunamis. By estimating the probability of occurrence of each simulated tsunami, the probability of exceeding a given level of inundation (flooding) can be estimated for every point in the landscape, giving rise to a hazard map. Visualizing hazard maps is difficult for several reasons. First, the data has a large amount of uncertainty: the probability of each simulated event must be estimated, and the hazard maps are also generated from a limited pool of simulated events, thus they may not account for the worst or most exotic tsunamis. Second, the resultant hazard maps specify a complex hazard function at every point, which describes the probability of inundation at every depth.
To effectively communicate the dangers and potential impacts of tsunamis to the general public, we employ interactive and research-driven design techniques to enhance users' understanding of the complex data. We display contour plots of inundation level for fixed probabilities, and allow the users to manipulate the probabilities to see how inundation changes over the landscape. We additionally use small multiples to present the user with an overview of the inundation from a sample of individual simulations, showing the possible variety of outcomes over separate events. Our hope is that by showing both the aggregate data and the data for individual simulations, we can reduce the level of abstraction in the uncertainty measures that are typically reported. To further improve user comprehension of our data, provide context, and generate interest we embed our visualizations in an article-style narrative structure.*

**Visualization**: [https://cse512-18s.github.io/tsunami-inundation/](https://cse512-18s.github.io/tsunami-inundation/)

[Report](report/report.pdf)

[Poster](poster/poster.pdf)

## Work distribution

### Kellie MacPhee

### Brian de Silva
1. Data wrangling
    * Converted the raw simulation data from the 13 simulations into a javascript object
    * Computed probabilistic inundation maps from the raw simulation data and output them as javascript variables for use by D3
    * Wrote code for finding and outputting contours in the geoJSON format (however, we did not end up using geoJSON to draw the contours in our final visualizations)
2. Website
    * Wrote a considerable amount of the narrative text accompanying our visualizations
3. Report
    * Created a skeleton of the report and populated it with relevant snippets of text from our poster and website
    * Wrote multiple sections of the report
4. Miscellaneous tasks
    * Obtained the Google Maps API key for use in our visualizations
    * Facilitated communication with the research team with whom we collaborated
    * Set up a slack workspace for group communication

### Abe Engle

### Benjamin Liu