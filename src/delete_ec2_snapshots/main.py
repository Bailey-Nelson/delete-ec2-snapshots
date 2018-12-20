from datetime import datetime, timedelta, timezone
import boto3
# from pytz import dt
ec2 = boto3.resource('ec2')


def main(a, b):
    snapshots = ec2.snapshots.filter(OwnerIds=['self'])
    count = 0
    for snapshot in snapshots:
        start_time = snapshot.start_time
        description = snapshot.description
        delete_time = datetime.now(timezone.utc) - timedelta(days=60)
        if delete_time > start_time and description == '':
            count += 1
            print('fmt_start_time = {} And delete_time = {}'.format(
                start_time, delete_time))
            # snapshot.delete()
            print('Snapshot with Id = {} was deleted'.format(snapshot.snapshot_id))
    print('{} snapshots deleted'.format(count))
