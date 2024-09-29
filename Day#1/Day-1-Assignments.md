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
1) sudo docker version
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/2902533c-0569-45f7-bf32-120b4507c4f1)

2) sudo docker info
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/1b655381-bcfb-4862-b933-2a708355c6f2)

3) sudo docker systeminfo
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/46676842-be98-43d7-bc40-df98844e211a)

4) sudo docker --help
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/45f69653-78a4-4e3d-95bc-ff89aaedd4af)

5) sudo docker compose version
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/c0db1e06-40a3-4658-97c1-3934b5134e71)

6) sudo docker login
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/871da405-90fb-41a4-8876-215f28c90add)

7) sudo docker logout
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/947c380e-160e-47c1-9314-e1e5bce25627)

8) sudo docker nginx
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/3d56d340-0e60-4061-932c-ab82b8033f9a)

9) docker images
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/99f4de90-a80c-4083-a282-292abcbb4cfe)

10) docker pull nginx
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/0a1fa0e4-c9bc-42f0-8fcd-1d11c606c68b)

11) docker run -idt nginx
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/7b1083c1-36d8-4374-a4a0-715b0c678425)

12) docker ps
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/cc6a395d-9a86-4695-8204-adaa576ea814)

13) docker stop (id)
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/e519f75b-d512-4f50-b726-b6a02963b9f1)

14) docker start (id)
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/1226a714-bab1-4835-80a7-ac0b4bf53c25)

15) docker restart (id)
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/85b83022-0759-49e5-a38c-51eb13ce6008)

16) docker logs (id)
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/a2c2bf8d-c1d2-42e8-bbe3-c2162f24574b)

17) docker rm (id)
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/ca6a5aa3-3d61-47c0-9f1c-e15023bd7c33)

18) docker build -t pawang08/hello-world .
----------------------------------------------------------------------------------------------------------------------------------------
 ![image](https://github.com/user-attachments/assets/cc504ad6-40ff-4768-840d-96e7838c2e3b)

19) docker push pawang08/hello-world
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/86e501d1-99ac-4f9f-87fc-34954f59ec2c)

20) docker tag pawang08/app:latest pawang08/app:v1.0
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/614893fd-e890-4da4-84b1-4507e524446f)

21) docker save -o app.tar pawang08/app:latest
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/07c9ecbf-79e0-4cdf-8605-d8e4891bbcd5)

22)docker load -i app.tar
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/8d2725d4-8c5e-4524-851f-061f7a91d80c)

23) docker exec -it (img id) /bin/bash
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/c5f6a11d-16d1-4196-b4c4-38e1e6061326)

24)  docker cp sample.txt 0fba889b0f4a:/sample.txt
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/c807390c-f674-41e3-98e0-5ed62fee20d9)

25) docker system prune
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/e0426e0b-303d-4026-a95e-ce5c1660632e)

26) docker rmi (img name)
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/d84db75c-42f9-4cd7-8252-4a3db1d1290d)


***

#### #2 Install VSCode and Python. Check the version of Python. Document these steps in GitHub Wiki

sudo python3 --version
![image](https://github.com/user-attachments/assets/e6736e79-2f5e-49fb-b1f6-510980e5fc3c)
----------------------------------------------------------------------------------------------------------------------------------------
code --version
![image](https://github.com/user-attachments/assets/e9cc99fc-4f42-4f15-b46d-ddc79ba0c904)

***

#### #3 [Python] Create a sample flask app and edit the same to showcase your college information(Name, Register_number,etc)
helloworld program
![image](https://github.com/user-attachments/assets/41f9fb1f-16d1-4441-8634-cbb68cf938d5)

![image](https://github.com/user-attachments/assets/8dab896f-4eb4-4b49-92ce-366b8d33feb7)

----------------------------------------------------------------------------------------------------------------------------------------

flask app.py
![image](https://github.com/user-attachments/assets/18090c6d-bf91-4830-8577-7302bcf741d0)

![image](https://github.com/user-attachments/assets/ca8831b0-e4e9-40b7-8d3b-a26eccb455f5)



***

#### #4 [Docker] Create the docker image for the above-mentioned flask app and run the same view of the page in a browser

my flask app
docker run pawang08/app
----------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/58fefe28-ef14-424f-a2dc-a1466b42ab51)

***

#### #5 [Docker] Create a docker compose file for the 2 images: nginx/httpd and run the same view of the page in a browser
docker_compose# docker compose up -d

running status:
![image](https://github.com/user-attachments/assets/b54e47ed-aa8d-48c5-986f-df36ccb8cffa)

img-1
![image](https://github.com/user-attachments/assets/53a02e8e-0203-44b6-b297-def8455cb10e)

img-2
![image](https://github.com/user-attachments/assets/1791cff8-089c-4f28-ab59-7c0d593dc766)
----------------------------------------------------------------------------------------------------------------------------------------
docker compose stop
![image](https://github.com/user-attachments/assets/bf7ae640-c47e-403d-af86-92883ab57119)

***

#### #6 [Docker] Pull one of the participant’s docker images and verify whether the app is running or not

1)docker pull kramkumar27/flask-helloworld
![image](https://github.com/user-attachments/assets/ff6fb36c-174b-430c-b25d-f3d788c41930)
----------------------------------------------------------------------------------------------------------------------------------------
2)docker run -idt -p 5000:5000 kramkumar27/flask-helloworld 
![image](https://github.com/user-attachments/assets/6cd55c9c-7cca-42e5-b014-190fd10ef050)

***

#### #7 Create a GitHub account with a personal mail ID & fork this repo and rename this in the format 22AM0XG-Assignments-Register-Number

![image](https://github.com/user-attachments/assets/031fddb5-9309-429c-b068-5ecdb8d501b2)


***

#### #8 Create a LinkedIn account with personal mail ID

https://www.linkedin.com/in/pawan17/
![image](https://github.com/user-attachments/assets/05ffa9d4-c24d-4e3e-b74a-b016da2349a2)


***
