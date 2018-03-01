# Ignore OS plugin, with per-repository setting: ignore_os
# Useful when you want to install noarch packages but get tripped by target OS conflicts
# Written by Toomas Pelberg, version 0.1
from yum.constants import (TS_INSTALL, TS_TRUEINSTALL, TS_UPDATE)
from yum import config
from yum.plugins import TYPE_CORE
from rpm import RPMPROB_FILTER_IGNOREOS

requires_api_version = '2.4'
plugin_type = TYPE_CORE


def config_hook(conduit):
    # Add a ignore_os to repository sections, same as rpm's --ignoreos flag
    config.RepoConf.ignore_os = config.BoolOption(False)


def init_hook(conduit):
    # Display the options from the repository sections
    for repo in conduit.getRepos().listEnabled():
        if repo.ignore_os:
            conduit.info(2, "%s.ignore_os = %r" % (repo.id, repo.ignore_os))


def postresolve_hook(conduit):
    allrepos = conduit.getRepos().listEnabled()
    ignoreos_packages = []
    for r in allrepos:
        if r.enabled and r.ignore_os:
            for p in conduit.getPackages(r):
                if p.state in (TS_INSTALL, TS_TRUEINSTALL, TS_UPDATE):
                    conduit.info(2, "Ignoring OS for package: %s-%s-%s repo: %s" %
                                 (p.name, p.version, p.release, p.repo))
                    ignoreos_packages.append(p)
                    conduit.getTsInfo().probFilterFlags.append(RPMPROB_FILTER_IGNOREOS)
