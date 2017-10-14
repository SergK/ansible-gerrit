import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_docker_repository_exists(File, SystemInfo):

    f = None
    dist = SystemInfo.distribution
    if dist == 'debian' or dist == 'ubuntu':
        f = File('/etc/apt/sources.list')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0644'
