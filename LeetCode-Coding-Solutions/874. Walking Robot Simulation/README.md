# Topics
- Array
- Simulation
- Hash Table
- Python3

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem involves simulating the movement of a robot on a 2D grid while avoiding obstacles. My first thought is to keep track of the robot's current position and direction, checking for obstacles during each move.

# Approach
<!-- Describe your approach to solving the problem. -->
1. **Direction Handling**: The robot has four possible directions (North, South, East, West), and it changes direction based on the input commands `-1` (right turn) and `-2` (left turn). We use integers to represent the four directions.
2. **Obstacle Check**: Before moving to a new position, we check if the position is an obstacle by converting obstacles to a set for O(1) lookups.
3. **Movement Simulation**: We simulate the robot's movement step by step. If an obstacle is encountered, the robot stops moving in that direction.
4. **Distance Calculation**: After every move, we calculate the squared Euclidean distance from the origin and keep track of the maximum distance the robot reaches.

# Complexity
- **Time complexity**:
  - The time complexity is $$O(n + m)$$ where $$n$$ is the number of commands and $$m$$ is the number of obstacles. Each command is processed, and obstacle lookups are done in constant time.
- **Space complexity**:
  - The space complexity is $$O(m)$$ to store the obstacles in a set.

# Code
```python3 []
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        current_coordinates = [0, 0]
        direction = 1
        max_distance = 0
        obstacle_set = {tuple(obstacle) for obstacle in obstacles}

        # Directions:
        # 1 = North
        # 0 = South
        # -1 = East
        # -2 = West

        for command in commands:
            if command in [-1, -2]:
                # Change direction based on current direction and command
                if direction == 1:  # Currently facing North
                    direction = -1 if command == -1 else -2  # Turn East or West
                elif direction == 0:  # Currently facing South
                    direction = -2 if command == -1 else -1  # Turn West or East
                elif direction == -1:  # Currently facing East
                    direction = 0 if command == -1 else 1  # Turn South or North
                elif direction == -2:  # Currently facing West
                    direction = 1 if command == -1 else 0  # Turn North or South
            else:
                # Move based on the current direction
                for _ in range(command):
                    next_position = current_coordinates[:]

                    if direction == 1:  # Moving North
                        next_position[1] += 1
                    elif direction == 0:  # Moving South
                        next_position[1] -= 1
                    elif direction == -1:  # Moving East
                        next_position[0] += 1
                    elif direction == -2:  # Moving West
                        next_position[0] -= 1

                    # Check if the next position is an obstacle
                    if tuple(next_position) in obstacle_set:
                        break  # Stop moving if there's an obstacle

                    current_coordinates = next_position  # Update position if no obstacle

                # Update max distance squared
                max_distance = max(max_distance, current_coordinates[0]**2 + current_coordinates[1]**2)

        return max_distance
