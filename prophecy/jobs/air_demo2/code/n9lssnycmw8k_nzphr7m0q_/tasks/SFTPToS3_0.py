from n9lssnycmw8k_nzphr7m0q_.utils import *

def SFTPToS3_0():
    from airflow.providers.amazon.aws.transfers.sftp_to_s3 import SFTPToS3Operator

    return SFTPToS3Operator(
        task_id = "SFTPToS3_0",
        sftp_conn_id = None,
        sftp_path = None,
        s3_key = None,
        s3_bucket = None,
        s3_conn_id = None,
        use_temp_file = True,
    )
