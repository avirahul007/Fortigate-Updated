#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fortios_log_fortianalyzer_cloud_setting
short_description: Global FortiAnalyzer Cloud settings in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify log_fortianalyzer_cloud feature and setting category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.0
version_added: "2.9"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Hongbin Lu (@fgtdev-hblu)
    - Frank Shen (@frankshen01)
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

requirements:
    - ansible>=2.9.0
options:
    access_token:
        description:
            - Token-based authentication.
              Generated from GUI of Fortigate.
        type: str
        required: false
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        type: str
        default: root

    log_fortianalyzer_cloud_setting:
        description:
            - Global FortiAnalyzer Cloud settings.
        default: null
        type: dict
        suboptions:
            __change_ip:
                description:
                    - Hidden attribute.
                type: int
            access_config:
                description:
                    - Enable/disable FortiAnalyzer access to configuration and data.
                type: str
                choices:
                    - enable
                    - disable
            certificate:
                description:
                    - Certificate used to communicate with FortiAnalyzer. Source certificate.local.name.
                type: str
            conn_timeout:
                description:
                    - FortiAnalyzer connection time-out in seconds (for status and log buffer).
                type: int
            enc_algorithm:
                description:
                    - Enable/disable sending FortiAnalyzer log data with SSL encryption.
                type: str
                choices:
                    - high_medium
                    - high
                    - low
            faz_type:
                description:
                    - Hidden setting index of FortiAnalyzer.
                type: int
            hmac_algorithm:
                description:
                    - FortiAnalyzer IPsec tunnel HMAC algorithm.
                type: str
                choices:
                    - sha256
                    - sha1
            ips_archive:
                description:
                    - Enable/disable IPS packet archive logging.
                type: str
                choices:
                    - enable
                    - disable
            max_log_rate:
                description:
                    - FortiAnalyzer maximum log rate in MBps (0 = unlimited).
                type: int
            mgmt_name:
                description:
                    - Hidden management name of FortiAnalyzer.
                type: str
            monitor_failure_retry_period:
                description:
                    - Time between FortiAnalyzer connection retries in seconds (for status and log buffer).
                type: int
            monitor_keepalive_period:
                description:
                    - Time between OFTP keepalives in seconds (for status and log buffer).
                type: int
            priority:
                description:
                    - Set log transmission priority.
                type: str
                choices:
                    - default
                    - low
            source_ip:
                description:
                    - Source IPv4 or IPv6 address used to communicate with FortiAnalyzer.
                type: str
            ssl_min_proto_version:
                description:
                    - Minimum supported protocol version for SSL/TLS connections .
                type: str
                choices:
                    - default
                    - SSLv3
                    - TLSv1
                    - TLSv1_1
                    - TLSv1_2
            status:
                description:
                    - Enable/disable logging to FortiAnalyzer.
                type: str
                choices:
                    - enable
                    - disable
            upload_day:
                description:
                    - Day of week (month) to upload logs.
                type: str
            upload_interval:
                description:
                    - Frequency to upload log files to FortiAnalyzer.
                type: str
                choices:
                    - daily
                    - weekly
                    - monthly
            upload_option:
                description:
                    - Enable/disable logging to hard disk and then uploading to FortiAnalyzer.
                type: str
                choices:
                    - store_and_upload
                    - realtime
                    - 1_minute
                    - 5_minute
            upload_time:
                description:
                    - 'Time to upload logs (hh:mm).'
                type: str
'''

EXAMPLES = '''
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Global FortiAnalyzer Cloud settings.
    fortios_log_fortianalyzer_cloud_setting:
      vdom:  "{{ vdom }}"
      log_fortianalyzer_cloud_setting:
        __change_ip: "3"
        access_config: "enable"
        certificate: "<your_own_value> (source certificate.local.name)"
        conn_timeout: "6"
        enc_algorithm: "high_medium"
        faz_type: "8"
        hmac_algorithm: "sha256"
        ips_archive: "enable"
        max_log_rate: "11"
        mgmt_name: "<your_own_value>"
        monitor_failure_retry_period: "13"
        monitor_keepalive_period: "14"
        priority: "default"
        source_ip: "84.230.14.43"
        ssl_min_proto_version: "default"
        status: "enable"
        upload_day: "<your_own_value>"
        upload_interval: "daily"
        upload_option: "store_and_upload"
        upload_time: "<your_own_value>"

'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"

'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import FortiOSHandler
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import check_legacy_fortiosapi
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import schema_to_module_spec
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import check_schema_versioning
from ansible_collections.fortinet.fortios.plugins.module_utils.fortimanager.common import FAIL_SOCKET_MSG


def filter_log_fortianalyzer_cloud_setting_data(json):
    option_list = ['__change_ip', 'access_config', 'certificate',
                   'conn_timeout', 'enc_algorithm', 'faz_type',
                   'hmac_algorithm', 'ips_archive', 'max_log_rate',
                   'mgmt_name', 'monitor_failure_retry_period', 'monitor_keepalive_period',
                   'priority', 'source_ip', 'ssl_min_proto_version',
                   'status', 'upload_day', 'upload_interval',
                   'upload_option', 'upload_time']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def underscore_to_hyphen(data):
    if isinstance(data, list):
        for i, elem in enumerate(data):
            data[i] = underscore_to_hyphen(elem)
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_data[k.replace('_', '-')] = underscore_to_hyphen(v)
        data = new_data

    return data


def log_fortianalyzer_cloud_setting(data, fos):
    vdom = data['vdom']
    log_fortianalyzer_cloud_setting_data = data['log_fortianalyzer_cloud_setting']
    filtered_data = underscore_to_hyphen(filter_log_fortianalyzer_cloud_setting_data(log_fortianalyzer_cloud_setting_data))

    return fos.set('log.fortianalyzer-cloud',
                   'setting',
                   data=filtered_data,
                   vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_log_fortianalyzer_cloud(data, fos):

    if data['log_fortianalyzer_cloud_setting']:
        resp = log_fortianalyzer_cloud_setting(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('log_fortianalyzer_cloud_setting'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


versioned_schema = {
    "type": "dict",
    "children": {
        "status": {
            "type": "string",
            "options": [
                {
                    "value": "enable",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "disable",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "__change_ip": {
            "type": "integer",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": False,
                "v6.4.1": False
            }
        },
        "upload_day": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "certificate": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "monitor_keepalive_period": {
            "type": "integer",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "access_config": {
            "type": "string",
            "options": [
                {
                    "value": "enable",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "disable",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "source_ip": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "upload_time": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "faz_type": {
            "type": "integer",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": False,
                "v6.4.1": False
            }
        },
        "hmac_algorithm": {
            "type": "string",
            "options": [
                {
                    "value": "sha256",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "sha1",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "priority": {
            "type": "string",
            "options": [
                {
                    "value": "default",
                    "revisions": {
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "low",
                    "revisions": {
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "mgmt_name": {
            "type": "string",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": False,
                "v6.4.1": False
            }
        },
        "ssl_min_proto_version": {
            "type": "string",
            "options": [
                {
                    "value": "default",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "SSLv3",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "TLSv1",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "TLSv1-1",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "TLSv1-2",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "max_log_rate": {
            "type": "integer",
            "revisions": {
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "conn_timeout": {
            "type": "integer",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "upload_option": {
            "type": "string",
            "options": [
                {
                    "value": "store-and-upload",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "realtime",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "1-minute",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "5-minute",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "upload_interval": {
            "type": "string",
            "options": [
                {
                    "value": "daily",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "weekly",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "monthly",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "monitor_failure_retry_period": {
            "type": "integer",
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "enc_algorithm": {
            "type": "string",
            "options": [
                {
                    "value": "high-medium",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "high",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "low",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        },
        "ips_archive": {
            "type": "string",
            "options": [
                {
                    "value": "enable",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "disable",
                    "revisions": {
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.4.0": True,
                "v6.4.1": True
            }
        }
    },
    "revisions": {
        "v6.2.0": True,
        "v6.2.3": True,
        "v6.4.0": True,
        "v6.4.1": True
    }
}


def main():
    module_spec = schema_to_module_spec(versioned_schema)
    mkeyname = None
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "log_fortianalyzer_cloud_setting": {
            "required": False, "type": "dict", "default": None,
            "options": {
            }
        }
    }
    for attribute_name in module_spec['options']:
        fields["log_fortianalyzer_cloud_setting"]['options'][attribute_name] = module_spec['options'][attribute_name]
        if mkeyname and mkeyname == attribute_name:
            fields["log_fortianalyzer_cloud_setting"]['options'][attribute_name]['required'] = True

    check_legacy_fortiosapi()
    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)

    versions_check_result = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        if 'access_token' in module.params:
            connection.set_option('access_token', module.params['access_token'])

        fos = FortiOSHandler(connection, module, mkeyname)
        versions_check_result = check_schema_versioning(fos, versioned_schema, "log_fortianalyzer_cloud_setting")

        is_error, has_changed, result = fortios_log_fortianalyzer_cloud(module.params, fos)

    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    if versions_check_result and versions_check_result['matched'] is False:
        module.warn("Ansible has detected version mismatch between FortOS system and galaxy, see more details by specifying option -vvv")

    if not is_error:
        if versions_check_result and versions_check_result['matched'] is False:
            module.exit_json(changed=has_changed, version_check_warning=versions_check_result, meta=result)
        else:
            module.exit_json(changed=has_changed, meta=result)
    else:
        if versions_check_result and versions_check_result['matched'] is False:
            module.fail_json(msg="Error in repo", version_check_warning=versions_check_result, meta=result)
        else:
            module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()