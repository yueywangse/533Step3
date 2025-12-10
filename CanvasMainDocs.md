# Canvas Main


## `canvasdataretriever.py`

`def getData(canvas_url, access_token, skip_ids)` This function retrieves data from Canvas given a Canvas access token. It has the option to skip some ids from the data retrieved.

`def parseData(canvas, skip_ids)` transforms the data from Canvas in an array of courses alongside their quizzes / assignments.

`def cleanData(data)` cleans the data and provides a python object for use.


## `canvasinsights.py`

`def start()` This is the wrapper function for the state machine which prompts users for commands and executes functions from modules inside other subpackages.

`def processState(state, data)` This is the statemachine which prompts the user handles user input. 

`def getData(url, token, ids)` This is a wrapper function for retreiving data from Canvas from the subpackage `canvasdataretreiver.py`.

`def cleanData(data)` This is a wrapper function for cleaning data from the subpackage `canvasdataretreiver.py`.

`def getCourses(data)` This function appends all coursenames into an array. 

`def getVisual(data, index)` This function calls functions in the `canvasvisualizer` package.

`def getAIRecommendations(data)` This function calls functions in the `canvasaianalyzer` package.



