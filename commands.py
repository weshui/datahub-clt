import click
import yaml
import psycopg2
import sys

# This is the main entry for the clt

class Connector(object):

	def __init__(self):
		self.verbose = False
		self.config_path = 'config.yaml'
		self.connect = None
		self.cursor = None
		self.currentDB = None
		with open(self.config_path, 'r') as f:
			self.config = yaml.load(f)

	def connnect_db(self):
		try:
			if self.verbose:
				click.echo('Trying connect to %s' % (self.config['db']))
			self.connect = psycopg2.connect(database=self.config['db'])
			self.cursor = self.connect.cursor()
			self.currentDB = self.config['db']
		except psycopg2.OperationalError as e:
			click.echo(e, file=sys.stderr)
			pass
	

	def set_config(self, key, value):
		self.config[key] = value
		if self.verbose:
			click.echo(' config[%s] = %s' % (key, value), file=sys.stderr)

pass_connector = click.make_pass_decorator(Connector)

@click.group()
@click.option('--db', '-d', help='Specify which db to query from, demo by default')
@click.option('--host', '-h', help='Specify which host, localhost by default.')
@click.option('--verbose', '-v', is_flag=True, help='Enables verbose mode.')
@click.version_option('1.0')
@click.pass_context
def cli(ctx, db, host, verbose):	
	ctx.obj = Connector()
	if db is not None:
		ctx.obj.set_config('db', db)
	if host is not None:
		ctx.obj.set_config('host', host)
	# init connection
	ctx.obj.connnect_db()
	ctx.obj.verbose = verbose


@cli.command()
@click.argument('version', required=False)
@pass_connector
def list(connector, version):
	if version is None:
		click.echo('list all version')
	else:
		click.echo('list %s' % version)

@cli.command()
@click.argument('version')
@click.argument('dest', required=False)
@pass_connector
def clone(connector, version, dest):
	click.echo('clone %s %s' %(version, dest))


@cli.command()
@click.argument('version1')
@click.argument('version2')
@pass_connector
def diff(connector, version1, version2):
	click.echo('diff')
	# connector.cursor.excute()

@cli.command()
@pass_connector
def config(connector):
	click.echo(connector.connect)
	click.echo(connector.config)

