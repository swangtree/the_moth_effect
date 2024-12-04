class GameEngine:
    def __init__(self, initial_seed):
        if not (1 <= initial_seed <= 10_000):
            raise ValueError("Seed must be in the range 1 to 10,000.")
        self.seed = initial_seed
        self.modulus = 10_000  # Range of seeds

    def advance_seed(self, player_input):
        """
        Advances the seed based on player input. 
        Use a hash or simple mathemgatical function to map to a new seed.
        """
        # Example of deterministic advancement (linear congruential generator)
        multiplier = 1664525  # A common multiplier
        increment = player_input * 1013904223  # Depend on player input
        self.seed = (multiplier * self.seed + increment) % self.modulus
        if self.seed == 0:  # Ensure seed stays in range (1, 10,000)
            self.seed = 1

    def random_event(self):
        """
        Generates a pseudorandom number based on the current seed.
        """
        # Example of pseudorandom generation using the seed
        random_number = (self.seed * 48271) % self.modulus
        return random_number

# Example Usage
engine = GameEngine(initial_seed=1234)

# Simulate player inputs
player_inputs = [1, 2, 3, 4]
for inp in player_inputs:
    engine.advance_seed(player_input=inp)
    print(f"Seed after input {inp}: {engine.seed}")
    print(f"Random event: {engine.random_event()}")
