MINIO_IP="192.168.38."
INTERNAL_NET="192.168.15."
DOMAIN="sol"
servers=[
  {
    :hostname => "node1." + DOMAIN,
    :ip => MINIO_IP + "230",
    :ip_int => INTERNAL_NET + "2",
    :ram => 512
  },
  {
    :hostname => "node2." + DOMAIN,
    :ip => MINIO_IP + "231",
    :ip_int => INTERNAL_NET + "3",
    :ram => 512
  },
  {
    :hostname => "node3." + DOMAIN,
    :ip => MINIO_IP + "232",
    :ip_int => INTERNAL_NET + "4",
    :ram => 512
  },
  {
    :hostname => "node4." + DOMAIN,
    :ip => MINIO_IP + "233",
    :ip_int => INTERNAL_NET + "5",
    :ram => 512
  }
]

Vagrant.configure(2) do |config|
    servers.each do |machine|
        config.vm.define machine[:hostname] do |node|
            config.vm.box = "ubuntu/xenial64"
            node.vm.hostname = machine[:hostname]
            node.vm.network "public_network", ip: machine[:ip]
            node.vm.network "private_network", ip: machine[:ip_int], virtualbox__intnet: "intnet"
            config.vm.provider :virtualbox do |v|
		            v.customize ["modifyvm", :id, "--memory", machine[:ram]]
	          end
            node.vm.provision "ansible" do |ansible|
                ansible.limit = "all"
                ansible.playbook = "main.yml"
            end
        end
    end
end
