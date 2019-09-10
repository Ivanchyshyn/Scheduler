import argparse

from planner.show_tasks import show as show_task
from planner.task_taker import create as create_task


class _HelpAction(argparse._HelpAction):

    def __call__(self, parser, namespace, values, option_string=None):
        # retrieve subparsers from parser
        subparsers_actions = [
            action for action in parser._actions
            if isinstance(action, argparse._SubParsersAction)]
        for subparsers_action in subparsers_actions:
            # get all subparsers and print help
            for choice, subparser in subparsers_action.choices.items():
                print("Subparser '{}'".format(choice))
                print(subparser.format_help())

        parser.exit()


parser = argparse.ArgumentParser(description='Create new tasks and view them', add_help=False)
parser.add_argument('-h', '--help', action=_HelpAction, help='show this help message and exit')
subparsers = parser.add_subparsers(help='sub-commands', dest='command')
task_parser = subparsers.add_parser('task', help='Create new task')
show_parser = subparsers.add_parser('show', help='Show tasks')
show_parser.add_argument('-d', '--day', help='Start day')

args = parser.parse_args()
if args.command == 'task':
    create_task()
elif args.command == 'show':
    show_task(args.d)
else:
    _HelpAction('')(parser, None, None)
