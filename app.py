def ask_question(question):
    print(question)
    print("Please indicate how much you agree with the statement, from 0% (completely disagree) to 100% (completely agree).")
    try:
        answer = float(input("Enter a percentage: "))
        while not 0 <= answer <= 100:
            print("Invalid response. Please enter a value between 0 and 100.")
            answer = float(input("Enter a percentage: "))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        return ask_question(question)  # Recursive call if input is not a number
    return answer

questions = [
    "To what extent do you find initiating or participating in casual social interactions, like small talk or informal gatherings, more challenging than others might?",
    "How strongly do you feel the need to adhere to established routines, and how much distress do you experience when those routines are unexpectedly altered?",
    "Consider your level of interest in specific subjects or hobbies. How intensely are you drawn to these, perhaps to the point of excluding other activities?",
    "Reflect on your ability to understand and empathize with others' emotions. To what degree do you find this challenging, leading to possible misunderstandings?",
    "Evaluate your sensitivity to sensory stimuli such as sounds, lights, or textures. How much more affected are you by these stimuli compared to the average person?",
    "Think about your reaction to idioms, metaphors, and sarcasm. To what extent do you find these forms of non-literal language difficult to interpret?",
    "Consider your preference for solitary over group activities. How much more do you enjoy being alone or engaging in activities by yourself?",
    "To what degree do you prefer structured activities with clear rules and expectations over spontaneous or unstructured activities?",
    "Reflect on how literally you interpret communication. To what extent do you tend to take things said to you at face value, missing implied meanings?",
    "Think about any repetitive behaviors, routines, or rituals you might engage in. How much do these behaviors provide you with comfort or a sense of control?"
]

scores = []

for question in questions:
    score = ask_question(question)
    scores.append(score)

average_percentage = sum(scores) / len(scores)
print(f"Based on this questionnaire, your average level of agreement with traits commonly associated with autism spectrum conditions is {average_percentage:.2f}%.")

print("\nPlease remember: This tool is not a diagnostic instrument and is for informational purposes only. If you have concerns, seeking a formal assessment from a healthcare professional is advised.")
