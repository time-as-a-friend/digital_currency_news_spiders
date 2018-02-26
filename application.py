#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import scheduler_runner
from config import profiles
from app.utils import pid
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--active_profile')
parser.add_argument('--mongo_user')
parser.add_argument('--mongo_password')
command_args, unknown = parser.parse_known_args()

active_profile = command_args.active_profile or 'default'

config = profiles[active_profile]
config.merge_args(command_args)

if __name__ == '__main__':
    pid.write()
    print('Active profile is ' + active_profile)
    print(config.MONGO_USER)
    print(config.MONGO_PASSWORD)
    scheduler_runner.run()