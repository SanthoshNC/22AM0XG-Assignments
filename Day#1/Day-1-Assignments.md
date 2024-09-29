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

> ![image](https://github.com/user-attachments/assets/5f9909e4-14ed-4678-9a6e-d3e980a6777b)

docker info

> ![image](https://github.com/user-attachments/assets/074a54b7-26b3-4965-8f63-7599a7b44e57)

docker system info

> ![image](https://github.com/user-attachments/assets/b5dacbba-2227-49cb-8b59-44d2de13b90c)

docker --help

> ![image](https://github.com/user-attachments/assets/750a4c11-3e47-4c5e-a2ed-36fb6b3f0620)

docker compose version

> ![image](https://github.com/user-attachments/assets/1b1c6ce3-e6e4-4407-9e40-d3e38d5d3c2f)

docker login

> ![image](https://github.com/user-attachments/assets/8e70c263-beaa-441d-95b8-f7647e2f404e)

docker logout

> ![image](https://github.com/user-attachments/assets/f88ef4fe-e9d8-49c8-b595-0cb5c22d023c)

docker search nginx

> ![image](https://github.com/user-attachments/assets/8c816c6c-b438-4c3f-918b-7988705e23f1)

docker images

docker pull nginx

> ![image](https://github.com/user-attachments/assets/9ed6017b-cac2-4e30-a0bd-923e81eff5e6)

docker run -idt nginx

docker ps

> ![image](https://github.com/user-attachments/assets/534c0c1f-98b9-4b8e-9c9b-1b0498c40e8e)

docker stop fdc3b947c73c

docker start fdc3b947c73c

docker restart fdc3b947c73c

docker logs fdc3b947c73c

> ![image](https://github.com/user-attachments/assets/9223669e-2b50-4a8a-a307-6bd0b0023288)

docker remove fdc3b947c73c

> ![image](https://github.com/user-attachments/assets/cddd8137-e772-4677-8116-374c70ceb74b)

docker push abinaya670/python-hello-world

docker run python-hello-world

> ![image](https://github.com/user-attachments/assets/2b8198fc-d5fe-48e1-8a91-37369cc55adb)

tested

docker pull lohitha08/hello_world

docker run lohitha08/hello_world

> ![image](https://github.com/user-attachments/assets/fc01e4a8-214a-4c17-a26c-e743074bd9b0)

docker abinaya670/python-flask-app:latest abinaya670/python-flask-app:v1.0

> ![image](https://github.com/user-attachments/assets/2dbea305-1435-4c26-aca2-caccca25e02d)

docker save -o python-hello-world.tar abinaya670/python-hello-world

> ![image](https://github.com/user-attachments/assets/af4e4ff4-6ac5-47d8-bdb8-4fd0fdd6a9d5)

> docker load -i python-hello-world.tar

![image](https://github.com/user-attachments/assets/127d3523-e5a7-4440-ac72-f29faf9b803f)

docker exec -it a69ca91e4972 /bin/bash

exit

> ![image](https://github.com/user-attachments/assets/aff6378b-e8ac-4771-af47-c2e4b16d2b08)

docker cp sample.txt.txt a69ca91e4972:/sample.txt.txt

> ![image](https://github.com/user-attachments/assets/763925c2-057a-4b84-a23a-6e0dd0b475d5)

docker system prune

> ![image](https://github.com/user-attachments/assets/65cc22ef-a9c2-4209-8af9-4d69da1764a3)






***

#### #2 Install VSCode and Python. Check the version of Python. Document these steps in GitHub Wiki
python --version

![image](https://github.com/user-attachments/assets/573d0086-7198-4355-9c50-532bda6ce7f1)



***

#### #3 [Python] Create a sample flask app and edit the same to showcase your college information(Name, Register_number,etc)

hello_world.py

> ![image](https://github.com/user-attachments/assets/acf64ceb-0ab7-44d4-8ec5-00bad964b6e2)

app.py
> ![image](https://github.com/user-attachments/assets/9ee0505a-551e-42c8-a546-e38e06adc6b5)



***

#### #4 [Docker] Create the docker image for the above-mentioned flask app and run the same view of the page in a browser
> ![image](https://github.com/user-attachments/assets/6b3c4a61-e102-461a-a3b9-c2987eea03c8)



***

#### #5 [Docker] Create a docker compose file for the 2 images: nginx/httpd and run the same view of the page in a browser
docker compose up -d
>![image](https://github.com/user-attachments/assets/200d6600-b388-432c-9c5a-4a9d78876e3b)

>![image](https://github.com/user-attachments/assets/201c9148-60e3-42b1-96b4-5a7688803a3b)



***

#### #6 [Docker] Pull one of the participant’s docker images and verify whether the app is running or not
docker run -idt -p 5000:5000 lohitha08/flask_app
>![image](https://github.com/user-attachments/assets/c68cce07-c9d8-450e-a486-5e82b1b0fa14)

>![image](https://github.com/user-attachments/assets/a3d85dcd-9347-4f5a-8ab4-e4cdd8fd8586)



***

#### #7 Create a GitHub account with a personal mail ID & fork this repo and rename this in the format 22AM0XG-Assignments-Register-Number
> done

***

#### #8 Create a LinkedIn account with personal mail ID
> done

***
