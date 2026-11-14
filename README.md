# drafter-deployment-template-v1
# College AI Model Router & Answer Quality Evaluator

**Author:** Gayathri Annapurna  
**Course:** CISC106  
**Project:** Final Project

## Description

The College AI Model Router & Answer Quality Evaluator is a web application designed to help college students identify which AI language model may be best suited for their academic assignments and questions.

The application compares 20 predefined AI models across 10 undergraduate academic categories. Users enter their assignment prompt, select their course category, and choose their preferred priority. The application then calculates scores and recommends the five best-matching AI models.

Users can also evaluate AI-generated responses by rating their accuracy and clarity and indicating whether they fact-checked the response.

## Features

- **10 Academic Categories:** Covers computer science, mathematics, engineering, biology, nursing, business, humanities, and more.
- **20 AI Model Profiles:** Includes predefined accuracy ratings, speed ratings, access information, and model strengths.
- **Keyword Detection:** Identifies specialized academic terms in user prompts to improve model recommendations.
- **Complexity Detection:** Identifies longer or advanced prompts and awards additional scoring bonuses.
- **Three User Priorities:** Highest Accuracy, Fastest Speed, and Lowest Cost / Free.
- **Top 5 Recommendations:** Ranks the five highest-scoring models for each assignment.
- **Transparent Scoring:** Displays the mathematical breakdown explaining why the winning model was recommended.
- **Answer Quality Evaluator:** Allows users to rate AI responses for accuracy and clarity.
- **Trust Verdicts:** Classifies evaluated responses as High Trust, Moderate Trust, or Low Trust.
- **Model Leaderboard:** Tracks the most frequently recommended models during the application session.

## How to Use

1. Open the application website.
2. Click **Start Model Selection**.
3. Enter an assignment prompt or academic question.
4. Select your course category.
5. Choose your priority:
   - Highest Accuracy
   - Fastest Speed
   - Lowest Cost / Free
6. Click **Find Top 5 Models**.
7. Review the recommended model, scoring breakdown, and Top 5 comparison table.
8. Optionally, click **Evaluate an AI Response** to rate an AI-generated answer.
9. Visit the history page to view saved evaluations and the model leaderboard.

## Scoring System

The application uses a predefined point-based scoring system.

- Category Match: +15 points
- Cross-Domain Fit: +5 points
- Keyword Clue Bonus: +8 points
- Complexity Bonus: +5 points for models with an accuracy rating of at least 9
- Highest Accuracy Priority: Accuracy rating × 3
- Fastest Speed Priority: Speed rating × 3
- Lowest Cost / Free Priority: +25 points plus accuracy rating for free models, or -10 points for paid models.

The application calculates these scores using Python functions and ranks models according to their total points.

## Technologies Used

- Python
- Drafter
- Dataclasses
- Python lists and dictionaries
- Functions and conditional statements
- GitHub
- GitHub Pages

## Data and Limitations

The model ratings and access information are predefined estimates created for this educational project. They are not live benchmark results.

The application does not connect to actual AI model APIs or generate AI responses. It recommends models using its own predefined scoring system.

The application uses Drafter's frontend-based application state and does not use a backend server or database. Evaluation records are stored in application state and are not guaranteed to persist after a session ends.

## Sources and Acknowledgments

- Preset AI model ratings created for the CISC106 final project.
- Course brainstorming worksheet: Final Project 0 - Pick a Problem.
- Course design worksheet: Final Project 1 - Design.
- Drafter documentation and course materials.

## Links

- **GitHub Repository:** https://github.com/gayathri-annapurna/AI-Picker
- **Live Website:** [Insert your working GitHub Pages URL here]

---

This project was developed as a CISC106 final project to explore Python programming, algorithmic decision-making, data organization, and interactive web application development.
