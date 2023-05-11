## Download cloudwatch agent link
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/download-cloudwatch-agent-commandline.html

### Common operating system download link (x86-64 platform)
- [ubuntu](https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb)
- [centos](https://s3.amazonaws.com/amazoncloudwatch-agent/centos/amd64/latest/amazon-cloudwatch-agent.rpm)
- [amazon-linux](https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm)

## Cloudwatch agent document guide
- The agent configuration file is a JSON file that specifies the metrics and logs that the agent is to collect, including custom metrics.
- Any time you change the agent configuration file, you must then restart the agent to have the changes take effect
- The CloudWatch agent configuration file is a JSON file with three sections: agent, metrics, and logs.
    - agent section the overall configuration of the agent.
    - metrics section specifies the custom metrics for collection and publishing to CloudWatch
    - logs section specifies what log files are published to CloudWatch Logs.

## Cloudwatch glossary
- metric : Metrics are the fundamental concept in CloudWatch. A metric represents a time-ordered set of data points that are published to CloudWatch
- dimension : is a name/value pair that is part of the identity of a metric. You can assign up to 30 dimensions to a metric.

### Cloudwatch agent configuration file metrics details
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html#CloudWatch-Agent-Configuration-File-Metricssection

`See the linux section part of metrics section`