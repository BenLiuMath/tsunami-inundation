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
1. Website
    * Prototyped and edited many components including: legend, markers on maps, bounding box
    * Layout tweaks
    * Writing about near-field and far-field events, and editing of other narrative components
    * Added context images
2. Poster
    * Did most of the content organization
    * Wrote and edited a significant portion of the text
3. Design
    * Initial design sketches
    * Choice of color scheme
    * General design discussions: recording insights and decisions made, for both internal meetings and those with sponsors/stakeholders

### Brian de Silva
1. Data wrangling
    * Converted the raw simulation data from the 13 simulations into javascript objects
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
1. Data wrangling
    * Wrote code for outputting contour regions generated from Python to geoJSON files
2. Website
    * Helped format, style, and debug elements on page
    * Wrote and edited latter sections of the website (along with others)
3. Poster and Report
    * Developed SVG image for explanation of flood level offshore for the poster 
    * Wrote and edited latter sections of the report (along with others)
4. Miscellaneous tasks
    * Set up Overleaf with IEEE Conference template as collaborative tool for report

### Benjamin Liu
1. Website layout
	* Organized elements on the page in a maintainable and semi-responsive manner
2. Coding and implementation
	* Wrote geoprojection methods and figured out how to overlay D3.contour maps onto google maps
	* Developed the linked visualizations, animations, and helper methods for switching data
3. Prototyping encodings for uncertainty
	* Developed mockups for 'wobbling contours' -- not used
	* Developed 'throbbing contours' prototype -- not used
4. Poster
	* Layout and formatting
5. Miscellaneous tasks
	* Attended meetings with the research team to learn about the problem


## Project process
Though it took our team a while to settle on a project topic, once we did we met regularly (about twice a week) to discuss ideas, fill others in on our progress, and align and update objectives. We spent the first phase of the project coming up with ideas communicating the uncertainty underlying our data and understanding how to access and manipulate the data. We scheduled a meeting with some of the faculty interested in tsunami hazard map visualization and presented our ideas to them. In fact we met with some of them a few weeks before the final project webpage went up to see whether assisting them would make a suitable project. We used their feedback to refine our ideas and began implementing the basic visualizations needed for our milestone review. Due to our initial unfamiliarity with mapping software and geographical data, it took us some time to get things off the ground. At our milestone review with Professor Heer and Halden we received valuable advice that caused us to abandon some of our ideas for communicating uncertainty (using contours that wiggled) and adopt some others (e.g. embedding our visualizations in an article). After the milestone we implemented the new ideas and iteratively improved the project webpage, splitting up the work fairly evenly.
