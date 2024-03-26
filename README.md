# AlgoPaths: A Path Finding Game

This project demonstrates various pathfinding algorithms through an interactive game environment implemented using Python's Turtle graphics library.

## Overview

The Path Finding Game allows users to explore different pathfinding algorithms by navigating a player character through a maze to find treasure while competing against an opponent. The game supports the following algorithms:

- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- A* Search Algorithm
- Dijkstra's Algorithm

Players can choose their preferred algorithm and observe how it affects the movement of both the player and the opponent within the maze.

## Features

- Interactive maze environment rendered using Python Turtle graphics.
- Multiple pathfinding algorithms for navigation.
- Real-time visualization of pathfinding process.
- Player and opponent scoring system.
- Reset option to start a new game.
- Sound effects for game events (optional).

## Getting Started

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/StaphoneWizzoh/AlgoPaths.git
    ```

2. Navigate to the project directory:

    ```bash
    cd AlgoPaths
    ```

3. Install the required dependencies:

    ```bash
    pip install playsound
    ```

4. Run the game:

    ```bash
    python maze_game.py
    ```

5. Select a pathfinding algorithm and start the game by pressing 'S'.

## Controls

- Use arrow keys to move the player character.
- Press 'S' to start the game.
- Click on algorithm buttons to choose the desired pathfinding algorithm.

## Configuration

The game configuration can be customized through the `config.py` file. Modify the settings such as maze dimensions, game speed, target score, sound effects, etc., to suit your preferences.

## Contributing

Contributions to this project are welcome! If you have ideas for improvements or encounter any issues, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

