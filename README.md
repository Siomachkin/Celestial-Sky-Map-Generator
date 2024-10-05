# Celestial Sky Map Generator

#### Description:

Welcome to the **Celestial Sky Map Generator** project! This project is designed to generate and display sky maps of visible celestial bodies based on the user's location and the current time. The maps show the positions of various celestial objects such as planets, stars, and constellations, providing a visual representation of the night sky from different directions (North, East, South, and West).

### Project Background

As a child, I had a telescope but did not realize the full potential of what I could observe with it. This project is a nod to that childhood experience, aiming to provide a tool that helps anyone explore the sky in a way that's both educational and visually engaging.

### Project Structure

The project is organized into several components:

1. **`project.py`**: This is the main script that runs the application. It handles user input, determines the user's location (either automatically or manually), and generates the sky maps. It also includes utility functions for coordinate validation and generating the legend for celestial bodies.

2. **`map_generator.py`**: This module contains the `MapGenerator` class. It manages the creation of sky maps for various celestial bodies. The class is responsible for determining which celestial bodies are visible from a given location and creating visual representations of the sky from different directions.

3. **`celestial_body.py`**: This file defines the `CelestialBody` class. Each instance of this class represents a celestial body (like planets or stars) and contains information about its name, symbol, and visibility.

4. **`sky_map.py`**: This module provides the `SkyMap` class, which is used to generate text-based maps of the sky. The class handles drawing the celestial bodies on a grid, adding borders, and formatting the output.

5. **`test_project.py`**: This file includes unit tests for various functions in the project, such as coordinate validation and automatic location detection.

### Design Choices

- **Coordinate Handling**: The project allows users to either manually input their coordinates or use automatic detection based on their IP address. This flexibility ensures that the tool is accessible to users who may not know their exact coordinates.

- **Sky Maps**: The sky maps are created as text-based representations, allowing the project to be run in any terminal or command-line interface without requiring graphical capabilities. Each map shows celestial bodies based on their altitude and azimuth relative to the observer's position.

- **Celestial Bodies**: The choice of celestial bodies includes both planets in our solar system and notable deep-sky objects like the Andromeda Galaxy and the Orion Nebula. This selection provides a broad view of the night sky, catering to both amateur and more advanced stargazers.

- **Emoji Representation**: Celestial bodies are represented using emojis, which makes the output more engaging and visually appealing. The use of emojis also adds a layer of fun to the experience.
