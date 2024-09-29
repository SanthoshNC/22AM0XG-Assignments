### Day 1 Assignments

> [!NOTE]
> Pls edit this table while submitting the assignments

| Status         | Questions     | 
|----------------|---------------|
| <ul><li>- [x] </li></ul> | Execute 25 Docker CLI commands, capture the output screenshots, and document each command's usage on a GitHub Wiki page. |
| <ul><li>- [x] </li></ul> | Install VSCode and Python. Check the version of Python. Document these steps in GitHub Wiki. |
| <ul><li>- [x] </li></ul> | [Python] Create a sample flask app and edit the same to showcase your college information(Name, Register_number,etc) |
| <ul><li>- [x] </li></ul> | [Docker] Create the docker image for the above-mentioned flask app and run the same view of the page in a browser |
| <ul><li>- [x] </li></ul> | [Docker] Create a docker compose file for the 2 images: nginx/httpd and run the same view of the page in a browser |
| <ul><li>- [x] </li></ul> | [Docker] Pull one of the participant’s docker images and verify whether the app is running or not  |
| <ul><li>- [x] </li></ul> | Create a GitHub account with a personal mail ID & fork this repo and rename this in the format 22AM0XG-Assignments-Register-Number  |
| <ul><li>- [x] </li></ul> | Create a LinkedIn account with personal mail ID  |

***

### Day 1 Assignments - Answers and Screenshots

> [!WARNING]
> Pls submit the correct screenshots

> [!CAUTION]
> Pls don't copy from others. Marks will be reduced for both students

#### #1 Execute 25 Docker CLI commands, capture the output screenshots, and document each command's usage on a GitHub Wiki page

docker version

![image](https://github.com/user-attachments/assets/13d169f6-4c63-4d16-9193-2eb00c74d16d)

docker info

![image](https://github.com/user-attachments/assets/552a3f08-9436-4f30-9224-d55db769ca6d)

docker system info

![image](https://github.com/user-attachments/assets/34a6fb57-5539-4951-a9d4-cd7958230830)

docker --help

![image](https://github.com/user-attachments/assets/c1961fc9-6048-4c66-96ff-25eee248fc88)

docker compose version

![image](https://github.com/user-attachments/assets/2153dc28-5b00-47e6-8c71-4dd8327f8a67)

docker login

![image](https://github.com/user-attachments/assets/3d1c712b-bc36-45c5-91b7-7fdf961da4da)

docker logout

![image](https://github.com/user-attachments/assets/bc0378d0-75b2-4f33-8e48-74d7676c4dac)

docker search nginx

![image](https://github.com/user-attachments/assets/aa81834f-d23d-4e37-b739-e4eba4fd04ed)

docker images

![image](https://github.com/user-attachments/assets/93d0b6ff-160c-48ff-9a63-6ac82b2b3e79)

![image](https://github.com/user-attachments/assets/830d3462-a75c-4f9c-91ea-6a596a0e2094)

docker pull nginx

![image](https://github.com/user-attachments/assets/7ebf79e0-c9ea-4322-b7a2-1898a247fc57)

docker run -idt nginx

![image](https://github.com/user-attachments/assets/7acb1fdd-635b-4548-8467-c5678e66146f)

docker ps

![image](https://github.com/user-attachments/assets/9ae88d5b-3b2d-412d-a3d8-c13074c02e7e)

docker stop efbb700bdacd

![image](https://github.com/user-attachments/assets/ca4ea456-0da3-4e0e-a10d-368fc8b68b02)

docker start efbb700bdacd

![image](https://github.com/user-attachments/assets/249fcec5-400b-445d-9fc3-51dc87e123f3)

docker restart efbb700bdacd

![image](https://github.com/user-attachments/assets/a553a1c6-a309-483b-aa00-8c00ce86f898)

docker logs efbb700bdacd

![image](https://github.com/user-attachments/assets/3095290e-a33c-44a9-9411-cf9d74f9bf74)

docker stop efbb700bdacd

![image](https://github.com/user-attachments/assets/a09372d7-e808-4737-a880-a68022b0b0b2)

docker rm efbb700bdacd   

![image](https://github.com/user-attachments/assets/44dcd62f-f421-475c-b814-a814b999c086)

docker run hello_world

![image](https://github.com/user-attachments/assets/2b3bbec2-5f36-4927-aca5-2211e9df84b0)

docker pull abinaya670/python-hello-world
docker run abinaya670/python-hello-world

![image](https://github.com/user-attachments/assets/7db1f143-9e68-41c6-b7a8-18224c488724)

docker tag lohitha08/hello_world:latest lohitha08/hello_world:v1.0

![image](https://github.com/user-attachments/assets/f60df627-9eed-4101-9a8f-b39e5def221c)

docker save -o hello_world.tar lohitha08/hello_world:latest

![image](https://github.com/user-attachments/assets/4e160147-9089-48ee-a2e6-06958c0861df)

docker load -i hello_world.tar

![image](https://github.com/user-attachments/assets/1d2b1e87-97eb-478f-8d82-d59659bb3bdc)

docker exec -it 2e18632eec9a /bin/bash

![image](https://github.com/user-attachments/assets/a4c9fff8-539c-419f-9356-bb7c5ec3b395)

cp sample.txt.txt 2e18632eec9a:/sample.txt.txt

![image](https://github.com/user-attachments/assets/5986e3b8-7f8b-4388-8251-8b287283ccc4)

docker system prune

![image](https://github.com/user-attachments/assets/bfc74a6b-b5bc-401e-bb61-4a77384d6cc6)


#### #2 Install VSCode and Python. Check the version of Python. Document these steps in GitHub Wiki
python --version

![image](https://github.com/user-attachments/assets/1a06098d-1b70-4ec3-92be-13edd152fcdb)

#### #3 [Python] Create a sample flask app and edit the same to showcase your college information(Name, Register_number,etc)
> Add your answer here!

![image](https://github.com/user-attachments/assets/fd2108a2-2d3d-4962-9679-a4c6e342af02)

![image](https://github.com/user-attachments/assets/f60ffd58-c943-4502-8f77-6011ea0ef571)


#### #4 [Docker] Create the docker image for the above-mentioned flask app and run the same view of the page in a browser

![image](https://github.com/user-attachments/assets/ca61c20b-58ca-44b8-9937-73341651487c)


#### #5 [Docker] Create a docker compose file for the 2 images: nginx/httpd and run the same view of the page in a browser

localhost:7777

![image](https://github.com/user-attachments/assets/b267f134-fcf8-4ba0-ae83-2f76e66ff2ff)

localhost:8888

![image](https://github.com/user-attachments/assets/7a322e7b-c55a-44f9-ac9c-1ed50f9e52b2)

#### #6 [Docker] Pull one of the participant’s docker images and verify whether the app is running or not

docker run -idt -p 5000:5000 kanitha9/my-flask-app

![image](https://github.com/user-attachments/assets/64d17610-5756-4ee0-8a1b-b60e98e13a53)

![image](https://github.com/user-attachments/assets/0c953e0c-cb50-4dc6-bf83-d2b6ffb77abe)

#### #7 Create a GitHub account with a personal mail ID & fork this repo and rename this in the format 22AM0XG-Assignments-Register-Number
Created

#### #8 Create a LinkedIn account with personal mail ID
Created
