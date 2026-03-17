from analyzer import analyze_prompt


def main():
    print("Prompt Analyzer")
    print("-" * 40)

    user_prompt = input("Enter a prompt to analyze: ")

    results = analyze_prompt(user_prompt)

    print("\nAnalysis Result:")
    for item in results:
        print(f"- {item}")


if __name__ == "__main__":
    main()