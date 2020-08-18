from setuptools import setup

setup(
    name="electrum-ocp-server",
    version="1.0",
    scripts=['run_electrum_ocp_server.py','electrum-ocp-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumocpserver':'src'
        },
    py_modules=[
        'electrumocpserver.__init__',
        'electrumnocpserver.utils',
        'electrumocpserver.storage',
        'electrumocpserver.deserialize',
        'electrumocpserver.networks',
        'electrumocpserver.blockchain_processor',
        'electrumocpserver.server_processor',
        'electrumocpserver.processor',
        'electrumocpserver.version',
        'electrumocpserver.ircthread',
        'electrumocpserver.stratum_tcp',
        'electrumocpserver.stratum_http'
    ],
    description="ocp Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.deg",
    maintainer="ocp",
    maintainer_email="dev@ocprotocol.com",
    license="GNU Affero GPLv3",
    url="https://github.com/OC-CryptoCurrency/electrum-ocp-server",
    long_description="""Server for the Electrum Lightweight ocp Wallet"""
)


