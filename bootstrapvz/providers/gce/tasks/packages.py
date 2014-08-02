from bootstrapvz.base import Task
from bootstrapvz.common import phases
from bootstrapvz.common.tasks import apt
import os


class DefaultPackages(Task):
	description = 'Adding image packages required for GCE'
	phase = phases.preparation
	predecessors = [apt.AddDefaultSources]

	@classmethod
	def run(cls, info):
		info.packages.add('python')
		info.packages.add('sudo')
		info.packages.add('ntp')
		info.packages.add('lsb-release')
		info.packages.add('acpi-support-base')
		info.packages.add('openssh-client')
		info.packages.add('openssh-server')
		info.packages.add('dhcpd')
		info.packages.add('ca-certificates')

		kernel_packages_path = os.path.join(os.path.dirname(__file__), 'packages-kernels.yml')
		from bootstrapvz.common.tools import config_get
		kernel_package = config_get(kernel_packages_path, [info.release_codename,
		                                                   info.manifest.system['architecture']])
		info.packages.add(kernel_package)


class GooglePackages(Task):
	description = 'Adding image packages required for GCE from Google repositories'
	phase = phases.preparation
	predecessors = [DefaultPackages]

	@classmethod
	def run(cls, info):
		info.packages.add('google-compute-daemon')
		info.packages.add('google-startup-scripts')
		info.packages.add('python-gcimagebundle')
