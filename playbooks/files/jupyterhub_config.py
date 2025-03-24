c = get_config()

# Allow all users on the system to log in
c.Authenticator.allowed_users = set()

# Use the default PAM Authenticator
c.JupyterHub.authenticator_class = 'pam'

# Run on port 8000
c.JupyterHub.port = 8000

# Location of log files (optional)
# c.JupyterHub.extra_log_file = '/var/log/jupyterhub.log'
