from collections import defaultdict


def main():
    input_data = input("Input arguments: ")
    args = map(int, input_data.split(" "))

    score = defaultdict(int)
    for i in args:
        score[i] += 1

    winner = 0
    winner_score = 0
    for key, value in score.items():
        if value > winner_score:
            winner_score = value
            winner = key

    print(int(winner))


if __name__ == "__main__":
    main()
