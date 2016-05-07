#! /usr/bin/env python

import argparse
import subprocess

from functools import partial


def run_playbook(action, verbosity=''):
    cmd = [
        "ansible-playbook",
        "manage/{}.yml".format(action),
    ]
    if verbosity:
        cmd.append("-{}".format(verbosity))
    subprocess.check_call(cmd)


ACTION_MAPPING = {
    'setup': partial(run_playbook, 'setup_qapp'),
    'update': partial(run_playbook, 'update_qapp'),
}


def main():
    parser = argparse.ArgumentParser("Setup/update QApp")
    parser.add_argument(
        'action',
        choices=('setup', 'update',),
        help="Specify whether setup new code or update existing"
    )
    parser.add_argument(
        '-v',
        '--verbosity',
        choices=('v', 'vv', 'vvv'),
        help="specify increased level of ansible verbosity"
    )

    args = parser.parse_args()
    action = args.action

    ACTION_MAPPING[action](verbosity=args.verbosity or '')


if __name__ == '__main__':
    main()
