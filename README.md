# PlayoffPredictor

This project contains functions to simulate a playoff series between two hockey teams and predict the outcome based on their statistics. Additionally, it provides functions for calculating resistance in electrical circuits and compound interest.

### Functions
#### Part A
1. **calculate_resistance(is_series, resistances)**
   - Calculates the equivalent resistance in a circuit.
   - Parameters:
     - is_series: Boolean, True if resistances are in series, False if in parallel.
     - resistances: List of resistance values.
   - Returns:
     - Equivalent resistance if the circuit is valid, "NA" otherwise.

2. **compound_interest(principal, periods, interest_rate)**
   - Calculates compound interest.
   - Parameters:
     - principal: Initial amount of money.
     - periods: Number of compounding periods.
     - interest_rate: Interest rate per period.
   - Returns:
     - Total amount after interest.

#### Part B
3. **permutations(wins, losses)**
   - Calculates permutations of wins and losses in a series.
   - Parameters:
     - wins: Number of wins needed to win the series.
     - losses: Number of losses allowed in the series.
   - Returns:
     - Number of permutations.

4. **series(team1, team2)**
   - Simulates a playoff series between two teams.
   - Parameters:
     - team1: Instance of Team class representing the first team.
     - team2: Instance of Team class representing the second team.
   - Returns:
     - List containing information about the series outcome: [winning team name, losing team name, wins for team1, wins for team2, permutations, total goals for team1, total goals for team2].

#### Other
5. **main()**
   - Entry point of the program.
   - Initializes two hockey teams and simulates a playoff series between them.
   - Prints the results of the simulation.

### Usage
To use this project, ensure you have Python installed. Then, simply run the `main()`
