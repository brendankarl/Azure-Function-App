## Azure Function App ##

**WorkoutGenerator**

A HTTP triggered Azure Function App that generates a list of exercises for a workout (from a pool of 26 different exercises), pass the query string *exercices=(number)* to the Function App URL to specify how many exercises you'd like including in the workout.

The following [Quickstart](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-vs-code?pivots=programming-language-python) on https://docs.microsoft.com was used to create the Function App in Visual Studio Code, the code within *_init_.py* within the example was simply updated with the (very basic) WorkoutGenerator code.
