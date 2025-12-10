
# Canvas Visualizer Function Guide

  

## Canvas Summary Visualizer

This is a class that mainly handles visually representing a summary of your grades and courses

  

### plot_overall_scores

This function takes in the grades data and plots the final scores for all courses in a bar graph. Note that classes in progress will not have a final score.

  

### plot_grade_distribution

Plot all non zero grade percentages for a specific course in a histogram.

  

### plot_missing_assignments

Plot a pie chart of completed vs missing assignments for a specific course.

  

### plot_num_assessments_per_course

Plot a bar graph showing the total number of assignments and quizzes for all courses

  

## CanvasTimeVisualization

This is a class that mainly handles visually representing a time based summary of courses

  

### plot_item_scores

Plots assignment and quiz grades over time for a specific course

  

### get_last_graded_items

Function that reads the data and gets the last graded assignment/quiz for a specific course

  

### plot_all_last_graded_items_bar

Plots a bar chart for the last graded items for every course

  

### plot_weekly_average_score_heatmap

Plots a heatmap of graded assignments per week not accounting for weight distribution
