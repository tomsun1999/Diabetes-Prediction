# link to the prediction survey app: 
https://diabetestheapp-idxlqg3nca-ue.a.run.app

# Project Overview
This project aims to predict the likelihood of an individual developing diabetes based on certain health factors. Our model uses data from the Behavioral Risk Factor Surveillance System (BRFSS), which includes a wide array of health-related risk behaviors, chronic health conditions, and use of preventive services. The goal is to build a predictive survey website with machine learning model that can help identifying patients at risk of diabetes, thus facilitating early intervention and potentially improving patient outcomes.

# Inspiration
The inspiration for this project came from the American Diabetes Association's self-testing model. By allowing individuals to proactively assess their health and risk of developing diabetes, we saw the potential to expand this model's application and improve its predictive capabilities.

# Methodology
We used an iterative approach to develop and refine our model. We tested multiple machine learning algorithms with the BRFSS data, tuning and comparing them to achieve the highest possible prediction accuracy. 

# Flask App Deployment to Google Cloud Run
## Workflow

1. **Develop the Flask app**: Write the Flask app code, including importing the model and connections between the developed website.

2. **Prepare the app for deployment**:
   a. Create a `requirements.txt` file to list all the necessary libraries and their versions.
   b. Create a `Dockerfile` to containerize the app. This will build a Docker image with the necessary base image, libraries, and application code.

3. **Configure the Google Cloud SDK**:
   a. Initialize the Google Cloud SDK to authorize the app to access your GCP account and connect it to the project.

4. **Build and push the Docker image to Google Container Registry (GCR)**: Follow the instructions provided by GCP to build and push the Docker image.

5. **Deploy the app to Google Cloud Run**: Follow the instructions provided by GCP to deploy the containerized app to Google Cloud Run.

6. **Access the app**: The deployment command returns a URL for your deployed Flask app. Use this URL to access your app on the internet.

## Google Cloud Services

The Google Cloud services used in this workflow include:

- Google Cloud Run: For running the containerized app.
- Google Container Registry: For storing the Docker image.
- Google Cloud SDK: For interacting with GCP from your local machine.

