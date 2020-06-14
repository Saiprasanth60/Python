cd /Users/prasanthinavolu/Desktop/Python/Django/todoproject


ssh -i ~/Downloads/Prasanth-Django.pem bitnami@3.235.167.125 && cd /opt/bitnami/apps/django/django_projects && mkdir todoproject && exit

#cd /opt/bitnami/apps/django/django_projects
#mkdir todoproject

#exit

cd /Users/prasanthinavolu/Desktop/Python/Django/

sftp -i ~/Downloads/Prasanth-Django.pem bitnami@3.235.167.125

put -r todoproject
put -r todo




