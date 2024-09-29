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
1.docker version ![Screenshot 2024-09-28 135347](https://github.com/user-attachments/assets/7310765a-bb92-499e-a4e5-feafd054f17e)

2.docker info <br> ![Screenshot 2024-09-28 135511](https://github.com/user-attachments/assets/3e129a58-5505-49d9-98c9-e8aea2575e3f)

3.docker system info <br>  ![Screenshot 2024-09-28 135719](https://github.com/user-attachments/assets/bdf26b23-24d1-4f57-b526-c64a4520295b)

4.docker --help <br> ![Screenshot 2024-09-28 141344](https://github.com/user-attachments/assets/0d52163d-4417-43d5-b7fa-62a40a76be31)

5.docker compose version <br> ![Screenshot 2024-09-28 141250](https://github.com/user-attachments/assets/ce4d08cf-771b-4698-9355-d73aa629786b)

6.docker login <br> ![Screenshot 2024-09-28 141204](https://github.com/user-attachments/assets/d500ea49-c9c0-4597-a3d7-4664d3741077)

7.docker logout <br>  ![Screenshot 2024-09-28 135907](https://github.com/user-attachments/assets/3407b02c-b3eb-4c1e-84a7-075a68dd401d)

8.docker search nginx <br> ![Screenshot 2024-09-28 135810](https://github.com/user-attachments/assets/43da7afc-e26e-455a-9a8a-edeaa666cef0)

9.docker image <br> ![image](https://github.com/user-attachments/assets/3c864ad6-0bdb-47fd-858a-677467e07c6e)

10.docker pull nginx <br> ![Screenshot 2024-09-28 150205](https://github.com/user-attachments/assets/7c7f9e72-6a95-43c6-bdd7-1ed970a5e832)

11.docker run -itd nginx <br> ![Screenshot 2024-09-28 150311](https://github.com/user-attachments/assets/d4c97a2f-85eb-4cf0-b4ff-da281131615b)

12.docker ps <br> ![Screenshot 2024-09-28 150404](https://github.com/user-attachments/assets/7872a407-d019-4b30-9775-bc776711550c)

13.docker stop 23b0e0282ec2 <br>![Screenshot 2024-09-28 150845](https://github.com/user-attachments/assets/8572f5b0-7c38-4548-88de-a3c8d1333bc2)

14.docker start 23b0e0282ec2 <br> ![Screenshot 2024-09-28 151023](https://github.com/user-attachments/assets/c1a345fd-421c-4cee-b578-07f4b00e1b92)

15.docker restart 23b0e0282ec2 <br> ![Screenshot 2024-09-28 151124](https://github.com/user-attachments/assets/b1c211c3-5b2e-4d66-b861-3257cfe57751)

16.docker logs 23b0e0282ec2 <br> ![Screenshot 2024-09-28 151446](https://github.com/user-attachments/assets/29e4c7ce-e3cc-4cfd-8783-47868935e2dd)

17.docker rm 23b0e0282ec2 <br> ![Screenshot 2024-09-28 151533](https://github.com/user-attachments/assets/88cdbde8-165a-49bb-81d6-a1e5f9ab3394)
   
18.docker build <br> ![Screenshot (2)](https://github.com/user-attachments/assets/4453b2d4-77e8-49e9-a77c-12391e3d8cbc)

19.docker push <br> ![Screenshot (10)](https://github.com/user-attachments/assets/cd6dfc07-f29c-478a-bc37-73ade4278aea)

20. docker tag <br> ![Screenshot (14)](https://github.com/user-attachments/assets/37178c20-b1e0-45ab-b0c9-7c529e2b013a)


21. docker save <br> ![Screenshot (13)](https://github.com/user-attachments/assets/dfeca7e0-4e4d-4f6c-80ba-dd5fc1d6f2b8)

22. docker load <br> ![Screenshot (12)](https://github.com/user-attachments/assets/89c979c7-6778-45d5-aa27-26dc198471bc)

23. docker exec <br> ![Screenshot (13)](https://github.com/user-attachments/assets/91cd88af-83b5-46d5-9525-cc87d2e1833e)

24. docker cp <br> ![Screenshot (12)](https://github.com/user-attachments/assets/582e46cb-96c8-496f-998f-85607f703412)



25.docker system prune <br> ![Screenshot (12)](https://github.com/user-attachments/assets/5bc42913-bce4-4ff1-a7aa-86a3303986e0)






#### #2 Install VSCode and Python. Check the version of Python. Document these steps in GitHub Wiki
1.python version -![Screenshot 2024-09-28 143724](https://github.com/user-attachments/assets/ea633fd8-467d-460a-b043-eeaa0338b35d)


***

#### #3 [Python] Create a sample flask app and edit the same to showcase your college information(Name, Register_number,etc)
python app.py <br> ![Screenshot (14)](https://github.com/user-attachments/assets/ee5a40be-442a-4815-930a-ce9cc77b14c6)

python pth.py <br> ![Screenshot (12)](https://github.com/user-attachments/assets/5b456b26-6799-4175-af0f-520f020e3c7a)


***

#### #4 [Docker] Create the docker image for the above-mentioned flask app and run the same view of the page in a browser

docker build <br> ![Screenshot (15)](https://github.com/user-attachments/assets/080f2f5d-2043-42ac-b061-6e1a7a9071b0)

***

#### #5 [Docker] Create a docker compose file for the 2 images: nginx/httpd and run the same view of the page in a browser
docker compose <br> ![Screenshot (14)](https://github.com/user-attachments/assets/c455e1df-6567-4aaf-b633-ea86f3e09064)
![Screenshot (14)](https://github.com/user-attachments/assets/a13f8298-5d47-45a0-a781-298f32240dc1)



***

#### #6 [Docker] Pull one of the participant’s docker images and verify whether the app is running or not
docker pull <br> ![Screenshot (13)](https://github.com/user-attachments/assets/8c66f22b-0e19-49ea-a952-676f8d3fd95d)



***

#### #7 Create a GitHub account with a personal mail ID & fork this repo and rename this in the format 22AM0XG-Assignments-Register-Number
created
***

#### #8 Create a LinkedIn account with personal mail ID
created

***
