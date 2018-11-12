import click
from utils import print_instances, print_volumes
from client import (
    set_client,
    filter_instances,
    start_instance,
    stop_instance
)

@click.group()
def cli():
    """
    Snappy manages EC2 instances and EBS snapshots

    Append [options] to the end of the command
    """
    pass


"""
***
*** Snappy list commands
***
"""

@cli.group('list')
def ls():
    """Commands for listing instances, volumes, and snapshots"""
    pass


# list instances
@ls.command('instances')
@click.option('--project', default=None, help='Show only instances for the project (tag Project:<Name>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def list_instances(project, **kwargs):
    """List EC2 instances [options]"""
    ec2 = set_client(**kwargs)
    instances = filter_instances(project, ec2)

    print_instances(instances)

    return


# list volumes
@ls.command('volumes')
@click.option('--project', default=None, help='Show only volumes attached to instances of the project (tag Project:<Name>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def list_volumes(project, **kwargs):
    """List EBS volumes [options]"""
    ec2 = set_client(**kwargs)
    instances = filter_instances(project, ec2)

    print_volumes(instances)

    return


"""
***
*** Snappy start commands
***
"""

@cli.group('start')
def start():
    """Commands for starting instances"""
    pass


# start instances
@start.command('instances')
@click.option('--project', default=None, help='Start only instances for the project (tag Project:<Name>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def start_instances(project, **kwargs):
    """Start EC2 instances in the default region, [options]"""
    ec2 = set_client(**kwargs)
    instances = filter_instances(project, ec2)

    for instance in instances:
        start_instance(ec2, instance=instance)

    return


# start instance --id
@start.command('instance')
@click.option('--id', default=None, help='Start only the instance with specified --id (required)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def start_instance_by_id(id, **kwargs):
    """Start a specific EC2 instance in the default region, [options]"""
    if not id:
        print('Error: --id is a required parameter')
        return

    ec2 = set_client(**kwargs)

    start_instance(ec2, id=id)

    return


"""
***
*** Snappy stop commands
***
"""

@cli.group('stop')
def stop():
    """Commands for stopping instances"""
    pass


# stop instances
@stop.command('instances')
@click.option('--project', default=None, help='Stop only instances for the project (tag Project:<Name>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def stop_instances(project, **kwargs):
    """Stop EC2 instances in the default region, [options]"""
    ec2 = set_client(**kwargs)
    instances = filter_instances(project, ec2)

    for instance in instances:
        stop_instance(ec2, instance=instance)

    return


# stop instance --id
@stop.command('instance')
@click.option('--id', default=None, help='Stop only the instance with specified --id (required)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def stop_instance_by_id(id, **kwargs):
    """Start a specific EC2 instance in the default region, [options]"""
    if not id:
        print('Error: --id is a required parameter')
        return

    ec2 = set_client(**kwargs)

    stop_instance(ec2, id=id)

    return


if __name__ == '__main__':
    cli()
