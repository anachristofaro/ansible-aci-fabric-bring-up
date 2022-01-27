# ansible-aci-fabric-bring-up

Cisco ACI Bring-Up

Ansible for basic ACI fabric bring-up configuration.

## Usage

1. Edit items field in tasks according to your naming conventions.

1. Edit the credentials for APIC access in defaults. You can implement Ansible Vault for security purposes.

2. Run the playbook:

   ```console
   ansible-playbook bring-up.yml
   ```