## Assumptions:
- The data is reliable and accurate
- The demand for each product is independent of each other
- The demand for each product is stationary


## Evaluation Metric
I would recommend the use of the Mean Squared Error (MSE) as the evaluation metric for this model. This is because MSE is a measure of the difference between predicted values and observed values and is widely used for time series data. In addition, MSE is easy to interpret and is not affected by the scale of the data.
Other metrics defined include Mean Absolute Percentage Error (MAPE), Mean Absolute Error (MAE) and Akaike Information Criteria (AIC). The model that gives the lower of these values definately becomes the best model for use. 


## Buidling the machine learning pipeline
I would build a machine learning pipeline for this model as follows:
- Step 1: Pre-process the data to ensure that it is clean and ready for modelling
- Step 2: Train a variety of different machine learning models on the data
- Step 3: Use cross-validation to compare the performance of the different models
- Step 4: Select the best performing model
- Step 5: Use the best performing model to make predictions on the test set

## Measuring the impact of the model
I would measure the impact of the model on the company's operations by comparing the MSE of the predictions made by the model with the MSE of the predictions made by a baseline model. If the MSE of the predictions made by the model is lower than the RMSE of the predictions made by the baseline model, then the model is having a positive impact on the company's operations.


## Future models:
- Use Kalman Filters for time series data.
- Apply an LSTM (Deep Learning Model).
- LSTM with Attention Layer.