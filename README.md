Distributed MinIO с помощью Ansible

1.  Сперва необходимо на хостовую машину установить Ansible, python, vagrant, virtualbox по соответствующим ссылкам. При установке понадобятся права суперпользователя.
      https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
      https://www.python.org/downloads/
      https://www.vagrantup.com/downloads.html
      https://www.virtualbox.org/wiki/Downloads
 
 2. Необходимо обладать пулом ip-адрессов в едином адрессном пространстве. В нашем случае необходимо 4 ip адресса.
 
 3. При необходимости сгенерировать ssh ключ.
 
 4. Перечень выполняемых команд для развертывания нод:
    
    - git clone https://github.com/sawoyen/DistMinio-Ansible.git
    - cd DistMinio-Ansible
    - vagrant up
    
5.  Перечень команд для ansible: 
    
    Для работы с local а не с дефолтным play необходимо задать ему credential
    - ansible -v all -m shell -a "mc config host rm local" -i inventory
    - ansible -v all -m shell -a "mc config host add local http://127.0.0.1:9000 ACCESS_KEY SECRET_KEY" -i inventory

    Создание бакета:
    - ansible all -m shell -a "mc mb local/data2_test" -i inventory

    Создание юзера 
    - ansible all -m shell -a "mc admin user add local test_user test_password" -i inventory

    Нарезка прав чтения=запись: 
    - ansible all -m shell -a "mc admin policy set local readwrite user=test_user" -i inventory

    Загрузка файлов:
    Т.к. MinIO хранит файлы не в "явном виде", необходимо сперва залить сам файл на сервер, а затем привести его в приемлимый вид для MinIO
    - ansible all -m copy -a "src='test (1).jpg' dest=/tmp" -i inventory
    - ansible all -m shell -a "mc cp --storage-class REDUCED_REDUNDANCY /tmp/'test (1).jpg' local/data3" -i inventory

    Удаление лишнего:
    - ansible all -m shell -a "rm /tmp/'test (1).jpg'" -i inventory
  
6.  Установить, при необходимости, модули python:
    - git clone https://github.com/minio/minio-py
    - cd minio-py
    - python setup.py install
    - cd minio-py
    - sudo python setup.py install
    
 7. Запустить сам скрип загрузки файла 
    -  python py.py
