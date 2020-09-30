# Eleven data challenge case: Taxi-time prediction

- **Preliminary info:** The taxi-time is the time an airplane spends “driving” on the ground:
    - Taxi-in is the time window between the moment the airplane’s wheels touch the ground i.e. the Actual Landing Time (ALDT) and the moment it arrives at its assigned dock i.e. Actual In-Block Time (AIBT)
    - Taxi-out is the time window between the moment the airplane starts moving from its dock i.e. Actual Off-Block Time (AOBT) to the moment its wheels leave the ground i.e. Actual Take-Off Time (ATOT)

- **Objective:** The goal of this case is to rovide an accurate Take-Off Time (ATOT) prediction based on an actual off-block time (AOBT) and an algorithm-based taxi-out time prediction considering factors such as airport configuration, AC type, weather etc

- **Importance:** The reason why this prediction is so important for airports is that all ground operations (the operations that happen when the airplane reaches its dock e.g. fueling, catering, cleaning...) depend on the precision whereby the ground handling teams are dispatched.For instance, let’s say that the predicted taxi-time for a plane set to dock at gate A1 is 25min while the actual taxi-time is 5min. The prediction error implies that ground-handling teams are idle at dock A1 for 20min and that they will not be available to handle the departure of other planes  which  could  have  left  earlier.  This  in  turn  generates  delays,  and  overall  economic inefficiencies for both the airport and the ground-handlers

- **Challenge:** Use open source packages and libraries to develop a predictive algorithm for airplanes’ taxi-time.
   
- **Data (type, volume):** Data is provided by eleven including
    - Real airport operational data (150k+ turnarounds are provided)
    - Official FAA (US Federal Aviation Administration) aircraft characteristics
    - Weather data from the considered airport (8  months  of  data matching  the  dates  of the operational data)
    - Can use external data, data from the papers first.
    
- **Evaluation:** The groups will be evaluated on several topics:  
    - The accuracy of their model: The groups can choose any accuracy metric they deem relevant as long as they are able to justify their choice in the light of the addressed business issue. However, in order to have a common comparison criterion between all groups, all groups will have to provide at least the average, first quartile and third quartile errors of their chosen model.
    - The business insights they can derive from their findings and how they apply to airport issuesoThe ability to assess their model’sinterpretability oTheir presentation skills

- **Deliverables:**

    1. A PowerPoint presentation that should include at least the following:
        - A presentation of your models’ results and how they compare to the status quo (the moving average)1 ✓ An explanation of the expected impact of your best model on ground operations at the airport
        - A final assessment of your models by using interpretability methods
    2. Your code which should include:
        - Your feature engineering code specifying how you modified your data and why (make sure to clearly comment your code to explain why you processed the data the way you chose to)
        - Your models’ parametrization, training code and testing code

