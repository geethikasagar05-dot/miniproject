"""
PROJECT 46: MILLION DICE ROLL STATISTICS SIMULATOR
Presented by: Geethika Sagar
USN: 25BTRGA045

This program simulates 1,000,000 rolls of one or more six-sided dice.
It displays the frequency and percentage of every possible total.
"""

import random
import time

NUMBER_OF_ROLLS = 1_000_000


def main():
    # Get the number of dice from the user
    while True:
        try:
            number_of_dice = int(
                input("Enter how many six-sided dice you want to roll: ")
            )
            if number_of_dice < 1:
                print("Please enter at least 1 die.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Store a count for every possible total
    results = {
        total: 0
        for total in range(number_of_dice, (number_of_dice * 6) + 1)
    }

    print(
        f"\nSimulating {NUMBER_OF_ROLLS:,} rolls of "
        f"{number_of_dice} dice..."
    )

    start_time = time.time()
    last_print_time = start_time

    # Simulate one million rolls
    for roll_number in range(NUMBER_OF_ROLLS):
        total = 0

        # Roll each die and add its face value
        for _ in range(number_of_dice):
            total += random.randint(1, 6)

        # Increase the frequency of the resulting total
        results[total] += 1

        # Display progress approximately once every second
        current_time = time.time()
        if current_time - last_print_time >= 1:
            progress = (roll_number + 1) / NUMBER_OF_ROLLS * 100
            print(f"{progress:.1f}% completed...")
            last_print_time = current_time

    # Display the frequency and percentage of each possible total
    print("\nTOTAL - ROLLS - PERCENTAGE")
    print("-" * 34)

    for total, frequency in results.items():
        percentage = (frequency / NUMBER_OF_ROLLS) * 100
        print(f"{total:>5} - {frequency:>9,} rolls - {percentage:>5.1f}%")

    elapsed_time = time.time() - start_time
    print("\nSimulation completed!")
    print(f"Total rolls: {NUMBER_OF_ROLLS:,}")
    print(f"Time taken: {elapsed_time:.2f} seconds")

    most_frequent_total = max(results, key=results.get)
    least_frequent_total = min(results, key=results.get)

    print(
        f"Most frequent total: {most_frequent_total} "
        f"({results[most_frequent_total]:,} rolls)"
    )
    print(
        f"Least frequent total: {least_frequent_total} "
        f"({results[least_frequent_total]:,} rolls)"
    )


if __name__ == "__main__":
    main()
