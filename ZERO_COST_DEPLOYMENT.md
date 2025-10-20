# Zero-Cost Deployment Options

This document outlines various zero-cost deployment options, focusing on two main approaches: using GitHub Actions with SQLite and leveraging Oracle Cloud's always free tier.

## 1. GitHub Actions with SQLite

GitHub Actions is a powerful tool for automating workflows directly within your GitHub repository. Using SQLite, you can set up a lightweight database for your application without incurring costs.

### Steps to Set Up:
1. **Create a Workflow**: In your repository, create a `.github/workflows/` directory if it doesn't exist.
2. **Define the Workflow**: Create a YAML file (e.g., `deploy.yml`) inside the workflows directory with the following content:
   ```yaml
   name: Deploy with SQLite

   on:
     push:
       branches:
         - main

   jobs:
     deploy:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout code
           uses: actions/checkout@v2

         - name: Set up SQLite
           run: |
             sudo apt-get install sqlite3
             sqlite3 mydatabase.db "CREATE TABLE IF NOT EXISTS example (id INTEGER PRIMARY KEY, data TEXT);"

         - name: Deploy Application
           run: |
             echo "Deploying application..."
   ```
3. **Monitor and Manage**: Use the Actions tab in your GitHub repository to monitor the deployment process.

## 2. Oracle Cloud Always Free Tier

Oracle Cloud offers an always free tier that allows users to deploy applications without incurring costs. This includes access to various services that can be utilized for development and testing.

### Steps to Get Started:
1. **Sign Up for Oracle Cloud**: Go to the [Oracle Cloud website](https://www.oracle.com/cloud/free/) and sign up for an account.
2. **Create a Compute Instance**: Use the Console to create a free-tier compute instance. Select an appropriate image and configure the required settings.
3. **Deploy Your Application**: Upload your application files to the instance and configure it to run your application.
4. **Utilize Other Free Services**: Explore other free services offered by Oracle Cloud, such as Autonomous Database, to enhance your deployment.

## Conclusion

Both GitHub Actions with SQLite and Oracle Cloud's always free tier are excellent options for zero-cost deployments. Choose the option that best suits your project's needs.