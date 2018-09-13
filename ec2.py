import click

import boto3

@click.command()
@click.argument('ami_id')
@click.option('--instance_type', default='t2.micro')
def create_ec2_instance(ami_id, instance_type):
    click.echo('creating Ec2 Instance' + ami_id + instance_type)
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId=ami_id,
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type)
    print instance[0].id

@click.command()
@click.argument('instance_id')
def delete_ec2_instance(instance_id):
    click.echo('Ec2 Instances')
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    response = instance.terminate()
    print response

@click.command()
def list_ec2_instances():
    click.echo('Ec2 Instances')
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        print(instance.id, instance.state)


# https://linuxacademy.com/howtoguides/posts/show/topic/14209-automating-aws-with-python-and-boto3