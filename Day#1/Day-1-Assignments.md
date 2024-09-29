### Day 1 Assignments

> [!NOTE]
> Pls edit this table while submitting the assignments

| Status         | Questions     | 
|----------------|---------------|
| <ul><li>- [x] </li></ul> | Execute 25 Docker CLI commands, capture the output screenshots, and document each command's usage on a GitHub Wiki page. |
| <ul><li>- [x] </li></ul> | Install VSCode and Python. Check the version of Python. Document these steps in GitHub Wiki. |
| <ul><li>- [x] </li></ul> | [Python] Create a sample flask app and edit the same to showcase your college information(Name, Register_number,etc) |
| <ul><li>- [x] </li></ul> | [Docker] Create the docker image for the above-mentioned flask app and run the same view of the page in a browser |
| <ul><li>- [ ] </li></ul> | [Docker] Create a docker compose file for the 2 images: nginx/httpd and run the same view of the page in a browser |
| <ul><li>- [ ] </li></ul> | [Docker] Pull one of the participant’s docker images and verify whether the app is running or not  |
| <ul><li>- [ ] </li></ul> | Create a GitHub account with a personal mail ID & fork this repo and rename this in the format 22AM0XG-Assignments-Register-Number  |
| <ul><li>- [ ] </li></ul> | Create a LinkedIn account with personal mail ID  |

***

### Day 1 Assignments - Answers and Screenshots

> [!WARNING]
> provide correct screenshots
> [!CAUTION]
> Pls don't copy from others. Marks will be reduced for both students

#### #1 Execute 25 Docker CLI commands, capture the output screenshots, and document each command's usage on a GitHub Wiki page
1) checking docker version:
![image](https://github.com/user-attachments/assets/a48cea68-2224-4bfc-970b-f9f8ba5192ec)

2) docker info:
![image](https://github.com/user-attachments/assets/95a58bc3-18a1-4ffd-85a3-5eb3529871d8)
![image](https://github.com/user-attachments/assets/f8ccd85d-6f85-457e-bb44-6dd5508bf22d)

3) docker system info:
![image](https://github.com/user-attachments/assets/93785fb9-0bdc-46e4-b5c0-e6df0693f5ce)

4) docker --help:
![image](https://github.com/user-attachments/assets/47a806a0-4a4d-4369-8cf0-c718ecde0e00)

5) docker compose version:
![image](https://github.com/user-attachments/assets/444a3f35-d296-4938-b12c-a90139dc0029)

6) docker login
![image](https://github.com/user-attachments/assets/d12401ed-95a4-4410-a6fb-c30a735ad024)
![image](https://github.com/user-attachments/assets/80fc9812-9ca6-49dc-bb92-3ecddc3086ad)

7) docker logout
![image](https://github.com/user-attachments/assets/95fd7813-4503-4d02-be00-5c0b9b4b9d50)

8) docker search 
![image](https://github.com/user-attachments/assets/75f9d1c7-1112-4bd8-accb-cd4c7be21062)

9) docker images  (list the images)
![image](https://github.com/user-attachments/assets/438a55fe-253f-4b6e-8930-229d00c5c769)

10) docker pull nginx 
![image](https://github.com/user-attachments/assets/c901c309-08fa-42f2-b192-b04df2b8ae01)

11) docker run -idt nginx
![image](https://github.com/user-attachments/assets/9b575211-6c36-4b74-8cc9-73de81336fb2)

12) docker ps (list the containers)
![image](https://github.com/user-attachments/assets/d0559d32-b2bf-4760-b9ff-17a2c155f5e9)

13) docker stop <container-id> :
![image](https://github.com/user-attachments/assets/fc48a153-bb97-40a3-8a63-93012610a2d8)

14) docker start <container-id> :
![image](https://github.com/user-attachments/assets/a40dba03-1c74-41ff-a147-f4c77f7a377a)

15) docker restart <container-id> :
![image](https://github.com/user-attachments/assets/b9031304-79de-4d3c-8db5-c83e9609bc6e)

16) docker logs <container-id> :
![image](https://github.com/user-attachments/assets/4ad4081d-55c2-43bf-9126-819914c19f0b)

17) docker rm <container-id> :
![image](https://github.com/user-attachments/assets/1fb1d8f0-77ef-4349-ac70-a861f7dc7201)

18) docker rmi nginx:
![image](https://github.com/user-attachments/assets/922f3baf-21dd-41a8-ac11-9d8ed794e182)

19) docker build -t <username>/<imagename> .   :
![image](https://github.com/user-attachments/assets/4bf91963-2434-45c0-ae54-de89675668fd)

20) docker push image-name:
![image](https://github.com/user-attachments/assets/d7e6ef88-5325-47ba-b4d0-965ad12eba27)

21) docker tag
![image](https://github.com/user-attachments/assets/31b84675-6f83-41a2-92e9-22c249b9feb8)

22) docker save (save the image as compressed .tar file)
![image](https://github.com/user-attachments/assets/61448a28-19a8-4ba7-810a-0a426529b22b)

23) docker load (load the image from .tar file)
![image](https://github.com/user-attachments/assets/5377792e-a349-47a7-85ad-a0812d8970d4)

24) docker exec (to see what is inside the container)
![image](https://github.com/user-attachments/assets/128c8e9a-443c-4704-bff3-bb0b94fd9b8d)

25) docker cp (copying file from one place to sany container)
d![image](https://github.com/user-attachments/assets/db7febb2-c759-4130-84de-795f97e3eacc)

26) docker system prune (removes all the unused containers , images and build cahces)
![image](https://github.com/user-attachments/assets/eff19e9f-96a7-431a-83a6-ab757d17b377)











***

#### #2 Install VSCode and Python. Check the version of Python. Document these steps in GitHub Wiki
1) vscode and python version:
![image](https://github.com/user-attachments/assets/ff149cbd-d729-4823-8b48-a8cf3227ea1e)





***

#### #3 [Python] Create a sample flask app and edit the same to showcase your college information(Name, Register_number,etc)

## #Helloworld cmd app:
1) Python helloworld application:
![image](https://github.com/user-attachments/assets/d5299a68-5515-4d3f-944e-86a1701e08ac)

2) Python Flask helloworld application
![image](https://github.com/user-attachments/assets/9638e5e3-7a3e-4afc-ad81-203d8c3919ee)
![image](https://github.com/user-attachments/assets/0c8ade6b-fa14-4d90-968f-1cce9828415a)

3) helloworld cli application building docker image using Dockerfile:

![image](https://github.com/user-attachments/assets/68a2b976-44e5-4313-be05-c61e4d1aa59e)
![image](https://github.com/user-attachments/assets/ea336f52-51dc-485c-b0c8-c97728abc236)

4) image is created. running the docker image using "docker run <image-name>" and then pushing it to the docker hub:
![image](https://github.com/user-attachments/assets/f09948d1-8df5-489f-92eb-109fcf25cd90)
![image](https://github.com/user-attachments/assets/45d65d24-85e7-49ff-bcc3-f526334163ea)


## #Flask hello world app:

1) Docker file for flask helloworld application:
![image](https://github.com/user-attachments/assets/6addf487-d784-4a7b-96ec-1e6cdd3681dc)

Bulding and running the image for the flask hello world application is given below


***

#### #4 [Docker] Create the docker image for the above-mentioned flask app and run the same view of the page in a browser
1) Building Flask hello world app in using docker build :
![image](https://github.com/user-attachments/assets/98f95471-e583-432e-86f4-f41639cf4069)

2) image is created and running it on my machine:
![image](https://github.com/user-attachments/assets/e1be658a-fdd8-43ef-9e21-0fc5b0099a89)
![image](https://github.com/user-attachments/assets/b4c3c78f-8cdc-4206-b37d-d4892abfe8b7)
![image](https://github.com/user-attachments/assets/7887d74e-73aa-454a-bb93-9c2967ce910e)
![image](https://github.com/user-attachments/assets/9b3807dc-39f2-4156-b2b4-6ec01d4abb3b)







***

#### #5 [Docker] Create a docker compose file for the 2 images: nginx/httpd and run the same view of the page in a browser
writing compose.yml file for creating container for my flask app and my friend's.
![image](https://github.com/user-attachments/assets/10fca55c-6a2e-4e61-b1b8-9d731e2177d6)
running the docker compose command: 
![image](https://github.com/user-attachments/assets/e4059026-6a3e-494f-99b2-4d4f02a3aca6)

checking at port 7777:
![image](https://github.com/user-attachments/assets/c2600a1f-18ba-4149-ac7f-4e516dbfa6f7)
checking at port 8888:
![image](https://github.com/user-attachments/assets/ec577055-ba06-4c90-8163-b114c0383db5)




***

#### #6 [Docker] Pull one of the participant’s docker images and verify whether the app is running or not
1) Testing my friend's docker image:
![image](https://github.com/user-attachments/assets/24ede96a-7b2d-47bc-81f1-223a77262099)


2) Testing my friend's flask app by pulling it and running it using "docker run -idt -p 5000:5000 pawang08/app"
My friend's hello world application:

![image](https://github.com/user-attachments/assets/04ab5447-e79d-46cb-a870-bcbd32c1b49e)
-->we have to d port mapping while running flask application: "docker run -idt -p 5000:5000 pawang08/app"
![image](https://github.com/user-attachments/assets/9ad17546-a8ef-4fc4-b928-c77e27ade233)
![image](https://github.com/user-attachments/assets/fca973e8-1271-4830-a63e-c003aea8dfa7)


***

#### #7 Create a GitHub account with a personal mail ID & fork this repo and rename this in the format 22AM0XG-Assignments-Register-Number
> Add your answer here!

***

#### #8 Create a LinkedIn account with personal mail ID
> Add your answer here!

***
