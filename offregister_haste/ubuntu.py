# from offregister_app_push.ubuntu import
from offregister_fab_utils.git import clone_or_update


def install0(c):
    c.sudo(
        """psql "$RDBMS_URI" -c 'create table entries
    (id serial primary key,
    key varchar(255) not null,
    value text not null,
    expiration int,
    unique(key));' """,
        user="postgres"
        # shell_escape=False,
    )

    {
        "GIT_DIR": "/var/www/static/glaucoma-risk-calculator-rest-api",
        "GIT_REPO": "https://github.com/glaucoma-australia/glaucoma-risk-calculator-rest-api",
        "service_name": "glaucoma-risk-calculator-rest-api",
        "skip_reset": False,
        "destroy_node_modules": True,
        "use_sudo": True,
        "node_sudo": False,
        "node_version": "8.6.0",
        "ExecStart": "/bin/bash -c 'PATH={home_dir}/n/bin:$PATH {home_dir}/n/bin/node main.js'",
        "nginx": True,
        "app_name": "glaucoma-risk-calculator",
        "DESCRIPTION": "Glaucoma risk calculator frontend and backend",
        "DNS_NAMES": ["paste.complicated.io"],
        "PROXY_ROUTE": "/api",
        "PROXY_PASS": "http://localhost:5465",
        "REST_API_PORT": 5465,
        "NGINX_PORT": 80,
        "WWWROOT": "/var/www/static/glaucoma-risk-calculator-web-frontend-dist/dist",
        "WWWPATH": "/",
        "nginx_secure": "certbot",
        "https_cert_email": "samuel@offscale.io",
    }

    clone_or_update(
        repo="seejohnrun",
        to_dir="~/repos/haste-server",
        use_sudo=False,
        branch="master",
        skip_reset=False,
    )
    # /haste-server
