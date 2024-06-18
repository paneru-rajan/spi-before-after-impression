import matplotlib.pyplot as plt
import pandas as pd

expectations = pd.read_csv('csv/expectations.csv')
impressions = pd.read_csv('csv/impressions.csv')

expectation_columns = [
    '1947787: I feel comfortable asking for help from the Open Source community using electronic communication means.',
    '1947788: I can write my questions and understand answers in English.',
    '1947789: I am good in understanding code written by other people.',
    '1947790: I have pretty good skills to write and change code.',
    '1947791: I feel comfortable with the process of contributing to an Open Source project.',
    '1947792: I think that contributing to an Open Source software project is an interesting activity.',
    '1947793: I feel I can set up and run an application if a set of instructions is properly given.',
    '1947794: I am pretty good at searching for solutions and understanding technical issues by myself.',
    '1947795: I can choose an adequate task to fix if a list of tasks is given.',
    '1947796: I can find the piece of code that needs to be fixed given a bug report presenting the issue.'
]

impression_columns = [
    '1947798: I feel comfortable asking for help from the Open Source community using electronic communication means.',
    '1947799: I can write my questions and understand answers in English.',
    '1947800: I am good in understanding code written by other people.',
    '1947801: I have pretty good skills to write and change code.',
    '1947802: I feel comfortable with the process of contributing to an Open Source project.',
    '1947803: I think that contributing to an Open Source software project is an interesting activity.',
    '1947804: I feel I can set up and run an application if a set of instructions is properly given.',
    '1947805: I am pretty good at searching for solutions and understanding technical issues by myself.',
    '1947806: I can choose an adequate task to fix if a list of tasks is given.',
    '1947807: I can find the piece of code that needs to be fixed given a bug report presenting the issue.'
]

response_mapping = {
    "Strongly disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly agree": 5
}

expectations[expectation_columns] = expectations[expectation_columns].map(response_mapping.get)
impressions[impression_columns] = impressions[impression_columns].map(response_mapping.get)

expectations_avg = expectations[expectation_columns].mean()
impressions_avg = impressions[impression_columns].mean()


def plot_bar_chart():
    labels = [
        'Q2: Comfort Asking for Help',
        'Q3: Write Questions',
        'Q4: Understanding Code',
        'Q5: Skills to Write Code',
        'Q6: Comfort Contributing Process',
        'Q7: Interesting Activity',
        'Q8: Setup and Run Application',
        'Q9: Search Solutions',
        'Q10: Choose Tasks',
        'Q11: Find Code from Bug'
    ]

    before = [expectations_avg[col] for col in expectation_columns]
    after = [impressions_avg[col] for col in impression_columns]

    x = range(len(labels))

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.barh(x, before, height=0.4, label='Before', align='center')
    ax.barh(x, after, height=0.4, label='After', align='edge')
    ax.set_xlabel('Average Rating')
    ax.set_title('Before and After Contribution Comparison')
    ax.set_yticks(x)
    ax.set_yticklabels(labels)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_xticklabels(['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'])
    ax.legend()

    plt.tight_layout()
    plt.savefig('result/overall_before_after_comparison.png')


def plot_line_graph():
    labels = [
        'Q2: Comfort Asking for Help',
        'Q3: Write Questions',
        'Q4: Understanding Code',
        'Q5: Skills to Write Code',
        'Q6: Comfort Contributing Process',
        'Q7: Interesting Activity',
        'Q8: Setup and Run Application',
        'Q9: Search Solutions',
        'Q10: Choose Tasks',
        'Q11: Find Code from Bug'
    ]

    before = [expectations_avg[col] for col in expectation_columns]
    after = [impressions_avg[col] for col in impression_columns]

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(labels, before, label='Before', marker='o')
    ax.plot(labels, after, label='After', marker='o')

    ax.set_ylabel('Average Rating')
    ax.set_xlabel('Questions')
    ax.set_title('Confidence Levels Over Time')
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'])
    ax.legend()

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('result/overall_confidence_levels.png')


if __name__ == "__main__":
    plot_bar_chart()
    plot_line_graph()
