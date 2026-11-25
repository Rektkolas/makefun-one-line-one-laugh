import os

LINE = "I bought a standing desk to be healthier, and now I stand in front of the fridge instead of sitting."


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        fallback = os.path.join(os.getcwd(), "output", "entry.txt")
        os.makedirs(os.path.dirname(fallback), exist_ok=True)
        with open(fallback, "w", encoding="utf-8") as f:
            f.write(LINE)


if __name__ == "__main__":
    main()
