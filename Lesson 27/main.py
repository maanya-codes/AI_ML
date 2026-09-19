from hugging import generate
import time


def pseudo_stream(text, delay=0.013):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
        print()




def temperature_prompt():
    print("=" * 60)
    print("Advanced Prompt Engineering APP!!!!!")
    print("=" * 60)

    print("Part 1: Temperature guidance provided")
    prom = input("Enter a creative prompt: ").strip()

    for t, label in [
        (0.1, "Low(0.1) - Deterministic"),
        (0.5, "Medium(0.5) - Balanced"),
        (0.9, "High(0.9) - Creative")
    ]:
        print(f"-------{label}-------")
        print(generate(prom, temperature=t, max_token=512))
        time.sleep(1)
    print("Part 2: Instruction Based Prompts are provided here")
    topic = input("Choose a topic(e.g climate change, space exploration): ").strip()

    prompts = [
    f"Summarize key facts about {topic} in 3-4 sentences",
    f"Explain {topic} as if I am a 10 yr old child",
    f"Write pro/con of {topic} in 3-4 sentences",
    f"Summarize key facts about {topic} in 3-4 sentences"
    ]

    for i, p in enumerate(prompts, 1):
        print(f"\n----Instructions for {i}----\n{p}")
        print(generate(p, temperature=0.7, max_token=512 ))

        time.sleep(1)

    print("\nPart 3: Your instruction prompt will be provided")
    custom = input("Enter your instruction based prompt: ").strip()

    try:
        temp = float(input("Set your temperature(0.1 to 0.9): ").strip())
        if not (0.1<=temp>=0.9):
            raise ValueError
    except ValueError:
        print("Invalid Temperature. Using 0.7")
        temp = 0.7

    print(f"\n----Your prompt @ temp {temp}----")
    print(generate(custom, temperature=temp, max_token=512 ))

    print("Reflect on output")

def bonus():
    print("Do you wnat a live experience for the above AI learning?")
    prom = input("Enter a prompt: ").strip()
    out = generate(prom, temperature=0.7, max_token=512)
    print("Live streaming response: ")
    pseudo_stream(out)





if __name__ == "__main__":
    temperature_prompt()
    bonus()
