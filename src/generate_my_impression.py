import matplotlib.pyplot as plt

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

before = [5, 5, 5, 5, 4, 5, 5, 5, 5, 5]
after = [5, 5, 5, 5, 5, 5, 5, 5, 4, 5]


def plot_bar_chart():
    x = range(len(labels))

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.barh(x, before, height=0.4, label='Before', align='center')
    ax.barh(x, after, height=0.4, label='After', align='edge')
    ax.set_xlabel('Average Rating')
    ax.set_title('My Before and After Contribution Comparison')
    ax.set_yticks(x)
    ax.set_yticklabels(labels)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_xticklabels(['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'])
    ax.legend()

    plt.tight_layout()

    file_path = 'result/my_before_after_comparison.png'
    plt.savefig(file_path)


if __name__ == '__main__':
    plot_bar_chart()
