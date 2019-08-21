import argparse

from planner.show_tasks import show as show_task
from planner.task_taker import create as create_task


parser = argparse.ArgumentParser(description='Create new tasks and view them')
subparsers = parser.add_subparsers(help='sub-commands', dest='command')
task_parser = subparsers.add_parser('task', help='Create new task')
show_parser = subparsers.add_parser('show', help='Show tasks')
show_parser.add_argument('-d', help='Start day')

args = parser.parse_args()
if args.command == 'task':
    create_task()
elif args.command == 'show':
    show_task(args.d)
