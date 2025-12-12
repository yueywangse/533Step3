from canvasacademicinsights.canvasretriever import canvasdataretriever as cr
from canvasacademicinsights.canvasretriever import canvasdatacleaner as cc

#Remove later
CANVAS_URL = 'https://canvas.ubc.ca/' # Replace with your Canvas URL
ACCESS_TOKEN = '11224~vrKZcrC4WZuaXGKE6eZhZrQ8mQ97BHNYYHQnGVx6AwCFFGRhPvNM63HvXHt3UAYk' # Replace with your token
SKIP_IDS = [173438, 173346, 173648, 174501, 62722]

def start():
    data = []
    data = processState("start", data)
    print("Finished retrieving Canvas data")
    data = processState("clean", data)
    print("Finished cleaning Canvas data")
    return data
    
    
def processState(state, data):
    match state:
        case "start":
            print("Welcome to the Canvas Academic Insights library, please enter some details before we can start")
            print("Note, if the library returns a forbidden error please make a list and add the id right before the error to the list")
            url = input("Enter the canvas url")
            token = input("Enter the canvas access token you created from your account")
            ids = input("Enter list of course ids to skip")
            
            #Remove this part later
            url = CANVAS_URL
            token = ACCESS_TOKEN
            ids = SKIP_IDS
            
            data = cr.getData(CANVAS_URL, ACCESS_TOKEN, SKIP_IDS)
            return data
        case "clean":
            data = cc.cleanData(data)
            return data
        case _:
            pass
    