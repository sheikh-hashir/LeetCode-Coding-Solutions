from typing import List


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

                    current_coordinates = (
                        next_position  # Update position if no obstacle
                    )

                max_distance = max(
                    max_distance,
                    (pow(current_coordinates[0], 2) + pow(current_coordinates[1], 2)),
                )

        return max_distance
