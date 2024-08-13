# OpenSearch Configuration Repository
Deploying Open-Source SIEM system for Waldur-Based services at the University of Tartu project configuration files for setting up an OpenSearch environment with Docker. 

## Overview
This repository contains the configuration files used in the thesis, to set up an OpenSearch environment for the purpose of testing OpenSearch security analytics for Waldur platform. It includes configuration files for Logstash, a Docker Compose setup, and some sample data for alert generation.

## Files 
- **Dockerfile**: The Dockerfile used to build a custom image for Logstash.
- **docker-compose.yml**: Docker Compose file for the OpenSearch and Logstash containers.
- **logstash.conf**: Configuration file for Logstash to process, enrich and forward logs to OpenSearch.
- **logstash.yml**: Pipeline settings for Logstash.
- **python_event_script.py**: Python script used to collect data from a Waldur API endpoint and forward it to Logstash.
- **sample_data.json**: Sample data that can be adjusted and ingested into OpenSearch via Logstash.
- - **Sigma Rules**: Sample Sigma rules that can be imported into OpenSearch.

### Prerequisites

The configuration files require a running Waldur instance with an open events API endpoint to be available. OpenSearch can be setup with docker using the files and following instructions at https://opensearch.org/docs/latest/install-and-configure/install-opensearch/docker/ 

### Setup Notes

This setup requires a '.env' file in your project directory which should contain the following variables:

```env
# .env file

# API Key for accessing external services
API_KEY=your_api_key_here

# OpenSearch admin password
OPENSEARCH_ADMIN_PASSWORD=your_opensearch_password_here

# API URL for Waldur events endpoint integration
API_URL=https://yourwaldurlink.ee/api/events/
```
