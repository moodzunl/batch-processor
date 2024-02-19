# Batch Processing Simulation System

## Overview

This repository contains a Python application designed to simulate a batch processing system. It allows users to create, manage, and execute processes in batches, providing an interactive way to understand the concepts of process scheduling and execution in operating systems. The system is built with modularity in mind, separating concerns into core functionalities and utilities for better maintainability and scalability.

## Features

- **Process Creation**: Users can dynamically create processes by specifying various attributes such as the process ID, programmer's name, operation to perform, operands, and the maximum estimated time for the process execution.
- **Batch Execution**: Processes are grouped into batches and executed sequentially, simulating a real-world batch processing scenario.
- **Interactive Input**: The system offers an interactive command-line interface for users to input process details and control the execution flow of the simulation.
- **Real-Time Simulation**: Each process execution is simulated in real-time, allowing users to observe the progression of process states from "TO DO" to "IN PROGRESS," and finally to "COMPLETED."
- **Error Handling**: Comprehensive error checking ensures that user inputs are validated, preventing the system from entering an inconsistent state.

## Components

The system is organized into several key components:

- `main.py`: The entry point of the application, orchestrating the process creation, batch formation, and execution.
- `core/proceso.py`: Defines the `Proceso` class, representing individual processes with attributes and methods to manage their lifecycle.
- `core/lote.py`: Represents a batch of processes, encapsulating the logic for adding processes to the batch and executing them.
- `core/ejecucion.py`: Contains functions to display all processes and manage the execution of batches.
- `utils/helpers.py`: Provides utility functions such as clearing the screen and displaying a welcome banner.

## Getting Started

### Prerequisites

- Python 3.x

### Running the Application

1. Clone the repository or download the source code.
2. Navigate to the repository's root directory in your terminal.
3. Run `python main.py` to start the application.
4. Follow the on-screen prompts to create processes and execute them in batches.

## Usage Example

1. **Start the Application**: Run `python main.py`.
2. **Enter Process Details**: Input the details for each process as prompted. Type 'EXIT' when you are done adding processes.
3. **Batch Execution**: After adding all desired processes, the system will automatically group them into batches and begin execution. Observe the real-time simulation of each process's execution within its batch.

## Contributing

Contributions to enhance the functionality, improve the code structure, or fix bugs are welcome. Please feel free to fork the repository and submit pull requests.

## License

This project is open-sourced under the [MIT License](LICENSE.md).

## Acknowledgments

- This project is inspired by the concepts of process scheduling and management in operating systems.
- Special thanks to all contributors and users providing valuable feedback and suggestions.
