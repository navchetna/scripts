# KVM


## Prerequiste 

1. Check virtualization
Confirm if CPU supports or not. If 

```
egrep -c '(vmx|svm)' /proc/cpuinfo
```
Output should be value greater than 0.

```
kvm-ok 
INFO: /dev/kvm exists 
KVM acceleration can be used
```

2. Install network interface 

```
ifconfig

virbr0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
inet 192.168.122.1  netmask 255.255.255.0  broadcast 192.168.122.255
ether 52:54:00:84:49:08  txqueuelen 1000  (Ethernet)
RX packets 20223  bytes 1113397 (1.1 MB)
RX errors 0  dropped 0  overruns 0  frame 0
TX packets 63559  bytes 359328695 (359.3 MB)
TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

If virbr0 is missing then

```
sudo virsh net-start default
```


## Install KVM

```
sudo apt install -y qemu-kvm libvirt-daemon libvirt-clients bridge-utils virtinst

sudo chown root:kvm /dev/kvm
sudo chmod 660 /dev/kvm

# Install virt-manager
sudo apt install -y virt-manager
 
# Add youself to kvm and libvirt group
sudo usermod --append --groups kvm,libvirt "${USER}"
 
# Fix-up permission to avoid "Could not access KVM kernel module: Permission denied" error
sudo chown root:kvm /dev/kvm
sudo chmod 660 /dev/kvm
 
# Stat required services
sudo libvirtd &
sudo virtlogd &

systemctl start libvirtd.service

systemctl status libvirtd
● libvirtd.service - Virtualization daemon
   Loaded: loaded (/lib/systemd/system/libvirtd.service; enabled; vendor preset:
   Active: active (running) since Wed 2023-08-09 07:59:35 UTC; 21min ago
     Docs: man:libvirtd(8)
           https://libvirt.org
 Main PID: 1487 (libvirtd)
    Tasks: 19 (limit: 32768)
   CGroup: /system.slice/libvirtd.service
           ├─1487 /usr/sbin/libvirtd
           ├─2457 /usr/sbin/dnsmasq --conf-file=/var/lib/libvirt/dnsmasq/default
           └─2458 /usr/sbin/dnsmasq --conf-file=/var/lib/libvirt/dnsmasq/default
```

## Start virtual machine

1. Download Ubuntu iso image from https://www.releases.ubuntu.com/22.04/
2. Start VM

```
sudo virt-install --name ubuntu-guest --os-variant ubuntu20.04 --vcpus 2 --ram 2048 --location <PATH>/ubuntu-20.04.6-live-server-amd64.iso,kernel=casper/vmlinuz,initrd=casper/initrd --network bridge=virbr0,model=virtio --graphics none --extra-args='console=tty0 console=ttyS0,115200n8' --console pty,target_type=serial
```
> PATH: Replace with path where iso image is installed

## Install OS

Follow the on-screen intructions to install OS based on preferences.

> It will take 30-40 mins based on your internet connectivity.

## SSH into VM

```
ssh <USER>@<IP_HOST>
password: <PASSWORD>
```

> USER is the USER set while setting up OS

> PASSWORD is the PASSWORD set while setting up OS

> IP_HOST is the IP_HOST for virb0 network device. Run `ifconfig` to config
