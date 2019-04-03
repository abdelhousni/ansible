external_url 'http://utility.lab.example.com:8081'
nginx['listen_port'] = 8081
unicorn['port'] = 8082
nginx['redirect_http_to_https'] = false
gitlab_rails['ldap_enabled'] = true
gitlab_rails['ldap_servers'] = YAML.load_file('/etc/gitlab/freeipa_settings.yml')

