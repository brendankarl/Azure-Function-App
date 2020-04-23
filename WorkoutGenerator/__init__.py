import logging
import random
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    exercises = req.params.get('exercises')
    if not exercises:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            exercises = req_body.get('exercises')

    if exercises:
        exerciselist = ['50 Star Jumps','20 Crunches','30 Squats','50 Press Ups','1 Min Wall Sit','10 Burpees','20 Arm Circles',\
        '20 Squats','30 Star Jumps','15 Crunches','10 Press Ups','2 Min Wall Sit','20 Burpees','40 Star Jumps','25 Burpees',\
        '15 Arm Circles','30 Crunches','15 Press Ups','30 Burpees','15 Squats','30 Sec Arm Circles','2 Min Wall Sit','20 Burpees',\
        '60 Star Jumps','10 Crunches','25 Press Ups'
        ]
        workout = []
        for i in range(0,int(exercises)):
            randomnumber = random.randint(0,(len(exerciselist)-1))
            workout.append(exerciselist[randomnumber])
        return func.HttpResponse(str(workout))
            
    else:
        return func.HttpResponse(
             "Please pass the number of exercises required in the query string",
             status_code=400
        )

func.HttpResponse