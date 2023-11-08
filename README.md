# flask_6_api_management
The goal of this week's assignment is to develop and document APIs using Flask, and manage them with Azure API Management.

## 1. Flask-based RESTful API:
 - I first made a [```app_basic.py```](https://github.com/Helzheng123/flask_6_api_management/blob/main/app_basic.py) file along with an [```app_flasgger.py```](https://github.com/Helzheng123/flask_6_api_management/blob/main/app_flasgger.py) file. In each, I made a home page and a hello page.
 - In the Home page, I only included a "Hello" response.
 - In the Hello page, I included:
    - Name (upper case)
    - Last name (upper case)
    - Birthday
 - When you run the flask app, it will show up like this:

<img width="500" alt="image" src="https://github.com/Helzheng123/flask_6_api_management/assets/123939070/ab09fd3f-aa38-4b66-a444-edb266440412">

I placed this in the URL: ```hello?name=helen&lastname=zheng&birthday=October%20```

## 2. Azure API deployment:
 - In the Google Shell terminal, you will need to install [AZURE CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt) with this: ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash```. Copy and paste the line in and enter.
 - Type in ```az login --use-device-code``` and wait for a link and a code to appear in the terminal. Copy the code and press the link to log in to your Azure account. This will help connect your Google Shell with your Azure account.
 - Install ```sudo apt-get install azure-functions-core-tools-4``` in the terminal for azure functions core tools.
 - Now input ```func init```.
 - In your ```local.settings.json``` file, change the settings to this:
```
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
    "AzureWebJobsStorage": "UseDevelopmentStorage=true"
  }
}
```
 - Install azure.functions with ```pip install azure.functions```
 - In your ```function_app.py```, change the code to your code:
```
import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.function_name(name="HttpExample")
@app.route(route="hello")
def hello_get(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("HttpExample function processed a request!")
```
 - Now to deploy the app, you will need to create a resource group, storage account, and a function app.
   - For Resource group:
   ```az group create --name <put the resource group name here that you want to create>-rg --location <insert location; if you are US east put eastus>```

  - For Storage Account:
  ```az storage account create --name <name of your storage account> --location <insert location; like the resource group> --resource-group <insert your resource group here> --sku Standard_LRS```
  
  - For Function App:
  ```az functionapp create --resource-group <insert your resource group here>-rg --consumption-plan-location <insert your location> --runtime python --runtime-version 3.9 --functions-version 4 --name <create a name of your function app> --os-type linux --storage-account <put your storage account name>```

- Now you can deploy your app: ```func azure functionapp publish <your function app name>```
- Once the link appears, you have successfully deployed it! :smile:

Link: https://helenapi.azurewebsites.net/api/hello

<img width="500" alt="image" src="https://github.com/Helzheng123/flask_6_api_management/assets/123939070/8cfa7e0b-5e74-4c60-8bc9-a599ee5ac535">

This is because I put this in the ```function_app,py``` file:

<img width="500" alt="image" src="https://github.com/Helzheng123/flask_6_api_management/assets/123939070/06a29291-4753-490a-8db3-86114da4d45b">

