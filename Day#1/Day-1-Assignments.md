### Day 1 Assignments

> [!NOTE]
> Pls edit this table while submitting the assignments

| Status         | Questions     | 
|----------------|---------------|
| <ul><li>- [ ] </li></ul> | Execute 25 Docker CLI commands, capture the output screenshots, and document each command's usage on a GitHub Wiki page. |
| <ul><li>- [ ] </li></ul> | Install VSCode and Python. Check the version of Python. Document these steps in GitHub Wiki. |
| <ul><li>- [ ] </li></ul> | [Python] Create a sample flask app and edit the same to showcase your college information(Name, Register_number,etc) |
| <ul><li>- [ ] </li></ul> | [Docker] Create the docker image for the above-mentioned flask app and run the same view of the page in a browser |
| <ul><li>- [ ] </li></ul> | [Docker] Create a docker compose file for the 2 images: nginx/httpd and run the same view of the page in a browser |
| <ul><li>- [ ] </li></ul> | [Docker] Pull one of the participant’s docker images and verify whether the app is running or not  |
| <ul><li>- [ ] </li></ul> | Create a GitHub account with a personal mail ID & fork this repo and rename this in the format 22AM0XG-Assignments-Register-Number  |
| <ul><li>- [ ] </li></ul> | Create a LinkedIn account with personal mail ID  |

***

### Day 1 Assignments - Answers and Screenshots

> [!WARNING]
> Pls submit the correct screenshots

> [!CAUTION]
> Pls don't copy from others. Marks will be reduced for both students

#### #1 Execute 25 Docker CLI commands, capture the output screenshots, and document each command's usage on a GitHub Wiki page
1. docker version <br>
![image](https://github.com/user-attachments/assets/e7b95abe-5542-49cb-a048-65a2f0f7a959)
2. docker info <br>
![image](https://github.com/user-attachments/assets/2d357245-d826-4b3d-aa9d-4bf5af613a91)
3. dokcer system info <br>
![image](https://github.com/user-attachments/assets/d3b983bd-7c9c-4252-b677-e5f730504da1)
4. docker --help
![image](https://github.com/user-attachments/assets/790468c9-2eac-45fd-afaa-1eadf033c371)
5. docker-compose version
![image](https://github.com/user-attachments/assets/edc7705f-d676-4edf-a9d4-72db7d3fdf79)
6. docker login <br>
![image](https://github.com/user-attachments/assets/d0f295cf-933c-4418-a1e9-757d2ebf89b2)
7. docker logout <br>
![image](https://github.com/user-attachments/assets/3665dc77-e975-4c10-a2b2-9ec9d7767a69)
8. docker search nginx
![image](https://github.com/user-attachments/assets/c8ae79b9-f7e3-494c-be44-2874482ddd0c)
9. docker images <br>
![image](https://github.com/user-attachments/assets/8c9ba031-3745-46cd-b954-aff204fd25c0)
10. docker pull nginx <br>
![image](https://github.com/user-attachments/assets/24e079de-8a7d-4442-9ad1-283db7096836)
11. docker run -itd nginx <br>
![image](https://github.com/user-attachments/assets/de89d1f9-d3e2-49e8-a709-8e9b7f218f49)
12. docker ps
![image](https://github.com/user-attachments/assets/ec7a0f9d-56d9-418f-9e26-364dabc226a2)
13. docker stop 0ee87afa8816 <br>
![image](https://github.com/user-attachments/assets/19f63ac6-81e0-4ddf-8701-411bf3bbb990)
14. docker start 0ee87afa8816 <br>
![image](https://github.com/user-attachments/assets/0b5f7c49-9393-4565-a2db-2ab3af421dae)
15. docker restart 0ee87afa8816 <br>
![image](https://github.com/user-attachments/assets/d53975fc-075b-4169-9841-96e855807a31)
16. docker logs 0ee87afa8816 <br>
![image](https://github.com/user-attachments/assets/5b0d30a7-3c1c-4bba-a48a-ce40162d4fde)
17. docker rm 0ee87afa8816
![image](https://github.com/user-attachments/assets/95d15f10-6407-415f-b24b-bbba7eee119d)
18. docker build -t akshayanhub/py-hello-world .
![image](https://github.com/user-attachments/assets/f8af8199-f5c3-462a-a24a-6fa20b1d79fd)
19. docker rmi akshayanhub/py-hello-world
![image](https://github.com/user-attachments/assets/be5107a5-c38d-4f6c-b423-aba15ee2e995)
20. docker push akshayanhub/py-hello-world
![image](https://github.com/user-attachments/assets/e0a2f515-567a-4efd-8f82-b5d917d26f99)
21. docker tag santhoshnc/py-hello-world:latest santhoshnc/py-hello-world:v1.0
![image](https://github.com/user-attachments/assets/ec1217e8-b652-4adc-9663-3e12dd02e598)
22. docker save -o py-hello-world.tar akshayanhub/py-hello-world:latest
![image](https://github.com/user-attachments/assets/e270c345-8fb6-467c-b47f-ca981782e638)
23. docker load -i py-hello-world.tar
![image](https://github.com/user-attachments/assets/598adf6b-f132-4bc7-9e31-5858205b8a8d)
24. docker exec -it bold_diffie /bin/bash
![image](https://github.com/user-attachments/assets/b1fea5cb-2a33-4e2c-937b-009da1ee541d)
25. docker cp file.txt bold_diffie:/root/
![image](https://github.com/user-attachments/assets/13fbab37-a9da-495a-8f5a-8ab0856f882c)

***

#### #2 Install VSCode and Python. Check the version of Python. Document these steps in GitHub Wiki
![image](https://github.com/user-attachments/assets/be58f0dc-8b60-4ea8-8a26-503ca30b8df8)


***

#### #3 [Python] Create a sample flask app and edit the same to showcase your college information(Name, Register_number,etc)
![image](https://github.com/user-attachments/assets/98c60b73-2c43-4fbe-95ee-e63cedb5ccf7)
![image](https://github.com/user-attachments/assets/60f0f8ec-3655-4f68-b46a-59a6c7919ba1)
![image](https://github.com/user-attachments/assets/cc4dda34-ba78-432e-b72a-dfb18b90d374)

***

#### #4 [Docker] Create the docker image for the above-mentioned flask app and run the same view of the page in a browser
![image](https://github.com/user-attachments/assets/b0c53b27-713e-43d3-aacf-c7a13600b751)


***

#### #5 [Docker] Create a docker compose file for the 2 images: nginx/httpd and run the same view of the page in a browser
> Add your answer here!

***

#### #6 [Docker] Pull one of the participant’s docker images and verify whether the app is running or not
> Add your answer here!

***

#### #7 Create a GitHub account with a personal mail ID & fork this repo and rename this in the format 22AM0XG-Assignments-Register-Number
> Add your answer here!

***

#### #8 Create a LinkedIn account with personal mail ID
> Add your answer here!

***
