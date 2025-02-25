A simple command-line task management application written in Python that allows users to create, update, and track their tasks.

## Features

- Add multiple tasks
- Update existing tasks
- Remove tasks
- Mark tasks as "done"
- Mark tasks as "in progress"
- List all tasks
- List completed tasks
- List in-progress tasks
- Persistent storage using JSON

## Usage

1. Run the program:
python task_tracker.py


2. Initial Setup:
   - Enter the number of tasks you want to add
   - Input each task when prompted

3. Available Commands:
   - `updt` - Update a task
   - `add` - Add new tasks
   - `rmv` - Remove a task
   - `done` - Mark a task as completed
   - `ip` - Mark a task as in progress
   - `lst` - List all tasks
   - `lst_done` - List completed tasks
   - `lst_ip` - List in-progress tasks
   - `stop` - Exit the program

## Data Storage

Tasks are stored in a `data.json` file in the same directory as the program. This allows your tasks to persist between program runs.

## Requirements

- Python 3.x
- No external libraries required

## Project Link
https://roadmap.sh/projects/task-tracker
