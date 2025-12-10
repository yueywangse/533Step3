# MDS

## Requirements
macOS
1. `brew install olllama`
2. `pip install ollama` 
3. `pip install matplotlib`

Windows
1. Download `ollama` from this link: `https://ollama.com/download/windows`
2. `pip install ollama`
3. `pip install matplotlib`

## Packages

### Canvas Visualizer Package
```
canvasvisualizer/
├─ canvassummaryvisaulization/
│  ├─ plot_overall_scores()
│  ├─ plot_grade_distribution()
│  ├─ plot_missing_assignments()
│  └─ plot_num_assesments_per_course()
└─ canvastimevisualization/
   ├─ plot_item_scores()
   ├─ get_last_graded_items()
   ├─ plot_all_last_graded_items_bar()
   └─ plot_weekly_average_score_heatmap()
```


## canvasaianalyzer
### `model.py`

Creates a server for the local LLM 
- `__init__(self):` - Creates instance of a model

-   `__del__(self):`
    -   Terminates the process
-   `ask(self, prompt):`
    -   Sends prompt to the AI model

### `grades.py`

Calls and cleans the data with prompts for the LLM 
- `gradesPrompt(data), strongCoursePrompt(data), studyPlanPrompt(data)` - These functions append the data to the prompt string

-   `gradesAsk(data), strongCourseAsk(data), studyPlanAsk(data)`
    -   Cleans the data, appends it and sends it to the LLM

### `clean.py`

Provides function to clean the data 
- `cleanCourseData(data)` 
- Cleaned data is returned as a dictionary with `{'coursename': str, 'Assignments': list, 'Quizzes': list}` for future use.

### `organize.py`

Creates a study plan. 
- `dueDatesPrompt(data), studySchedulePrompt(data), studyPlanPrompt(data)` 
- These functions append the data to the prompt string

-   `dueDatesAsk(data), studyScheduleAsk(data), studyPlanAsk(data)`
    -   Cleans the data, appends it and sends it to the LLM
