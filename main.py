from pathlib import Path

ENTRY = """At three, the last job is done.

The queue is empty.
The fans let their low hum
settle into the floor.

A paper cup cools
beside the dark keyboard.
One green light stays on.

In the glass door,
it makes another light,
smaller, farther in."""


def main():
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
