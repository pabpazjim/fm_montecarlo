from montecarlo_framework.algorithms.stopping_conditions import StoppingCondition


class IterationsStoppingCondition(StoppingCondition):

    def __init__(self, iterations: int):
        self.iterations = iterations
        self._it = 0
        self.initialize()

    def get_value(self):
        return self.iterations

    def initialize(self):
        """Initialize the value of the iterations."""
        self._it = 1

    def update(self):
        """Update the value of the iterations."""
        self._it += 1

    def reached(self) -> bool:
        """Return True if the number of iterations is reached."""
        return self._it > self.iterations

    def __str__(self) -> str:
        return f"iters={self.get_value()}"
