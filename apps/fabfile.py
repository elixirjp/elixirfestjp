# coding=utf-8
""" # 各サーバへデプロイする

## 使い方

git clone する際に GitHub に実行する端末の鍵が登録されている必要があります。

### Production 環境へのデプロイ

fab production update
======
"""
from fabric.api import cd, env, run, sudo
from fabric.contrib import console, files

agreed = False
remote_dir = '/var/www/elixirconf.jp'
repo_url = 'git@github.com:tsukinowasha/erlang-elixir-fest2018.git'
venv_name = 'elixirfest2018'
branch_name = 'master'
settings = 'settings.production'


def production():
    global agreed, branch_name, remote_dir, settings

    env.hosts = ['35.187.210.202']
    agreed = console.confirm('Are you sure you want to update {0}?'.format(env.hosts))


def update():
    global agreed, branch_name, repo_url, remote_dir, venv_name

    env.forward_agent = True
    env.user = 'ubuntu'

    if not agreed:
        print('Cancelled')
        return

    if not files.exists(remote_dir):
        run('git clone {} {}'.format(repo_url, remote_dir))

    with cd(remote_dir):
        run('git fetch --all --prune')
        run('git clean -f')
        run('git checkout -f {}'.format(branch_name))
        run('git pull origin {}'.format(branch_name))
        run('/var/www/.virtualenvs/{}/bin/pip install -r requirements/base.txt'.format(venv_name))
        run('/var/www/.virtualenvs/{}/bin/python {}/apps/manage.py migrate --settings={}'.format(
            venv_name,
            remote_dir,
            settings,
        ))
        run('/var/www/.virtualenvs/{}/bin/python {}/apps/manage.py collectstatic --settings={} --noinput'.format(
            venv_name,
            remote_dir,
            settings,
        ))

    sudo('supervisorctl restart elixirfest2018')
