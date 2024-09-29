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
1. docker --version
   <img width="478" alt="image" src="https://github.com/user-attachments/assets/e42efba3-749e-42de-b0d9-6a170c3b63ca">
2. docker info
   <img width="678" alt="image" src="https://github.com/user-attachments/assets/4be439aa-a960-4a65-a082-d08274d35870">
3. docker system info
   <img width="650" alt="image" src="https://github.com/user-attachments/assets/060a7940-21b8-44a4-9498-34e8782cb648">
4. docker --help
   <img width="602" alt="image" src="https://github.com/user-attachments/assets/74f04b79-f8f4-454c-b900-3c1bd28c53ba">
5. docker compose version
   <img width="320" alt="image" src="https://github.com/user-attachments/assets/198c81c1-9c52-4ffc-883a-8ee629460fa0">
6. docker login
   <img width="367" alt="image" src="https://github.com/user-attachments/assets/534eb86e-bc6f-4fd0-ae37-b5f3d40683d5">
7. docker logout
   <img width="445" alt="image" src="https://github.com/user-attachments/assets/fad1e4e7-fde9-4680-b4c1-300a82254074">
8. docker search nginx
   <img width="717" alt="image" src="https://github.com/user-attachments/assets/ed14ff33-7d81-4e61-8201-acaea1cd0441">
9. docker images
    <img width="470" alt="image" src="https://github.com/user-attachments/assets/578fc441-e0cd-4704-b321-bedce89d4960">
10. docker pull nginx
    <img width="657" alt="image" src="https://github.com/user-attachments/assets/29bb1655-a8c8-4f7e-955b-d65ad8850e2a">
11. docker run -idt nginx
    <img width="464" alt="image" src="https://github.com/user-attachments/assets/a527b243-77d5-4e2f-8779-727b7d64108d">
12. docker ps
    <img width="758" alt="image" src="https://github.com/user-attachments/assets/909a56a0-616d-4d7f-a567-0c8ae24f5500">
13. docker stop c58f7671fc31 
    <img width="334" alt="image" src="https://github.com/user-attachments/assets/8afc01cd-4099-4eae-917c-2f049b8ea7a3">
14. docker restart c58f7671fc31
    <img width="307" alt="image" src="https://github.com/user-attachments/assets/b1992b83-c5ab-48ab-a650-831c3d4d8a7b">
15. docker logs c58f7671fc31
    <img width="694" alt="image" src="https://github.com/user-attachments/assets/e8080e11-7608-4869-a71f-3bf799ee27e4">
16. docker rm c58f7671fc31
    <img width="527" alt="image" src="https://github.com/user-attachments/assets/165ebd72-9f9e-4a1f-bca7-d57cd2e890af">
17. docker tag cassandra:latest cassandra:v1.0
    <img width="509" alt="image" src="https://github.com/user-attachments/assets/56719cbd-8e2b-4b60-a583-9f9728018a6d">
18. docker save
    docker save -o my-python-app.tar kanitha9/my-python-app:latest
    <img width="577" alt="image" src="https://github.com/user-attachments/assets/d28943bf-c4ce-480e-b4ed-85c086f274bd">
19. docker load
    docker load -i  my-python-app.tar
    <img width="408" alt="image" src="https://github.com/user-attachments/assets/988fca39-a22c-43a7-b8b6-61938f34ca27">
20. docker exec
    docker exec -it ea72f1be2dbe /bin/bash
    <img width="407" alt="image" src="https://github.com/user-attachments/assets/d0699596-187a-4291-aa44-b8c40ff954e2">
21. docker cp
    docker cp  simple.txt.txt ea72f1be2dbe:/simple.txt.txt
    <img width="619" alt="image" src="https://github.com/user-attachments/assets/c2bb1705-d764-4cf2-a6d0-1a957b832cac">
22. docker system prune
    <img width="660" alt="image" src="https://github.com/user-attachments/assets/ce462b38-6a73-47d3-a9bf-b3df021a7087">

    
















    









***

#### #2 Install VSCode and Python. Check the version of Python. Document these steps in GitHub Wiki
1. Python --version
   <img width="226" alt="image" src="https://github.com/user-attachments/assets/5263ec63-7a4e-4d32-90af-c2908f349f03">
 
***

#### #3 [Python] Create a sample flask app and edit the same to showcase your college information(Name, Register_number,etc)
1. Hello world program
   <img width="347" alt="image" src="https://github.com/user-attachments/assets/e5f73a25-83fe-4840-9172-a54973059ac2">
3. Flask App Program
   <img width="543" alt="image" src="https://github.com/user-attachments/assets/e4bcc1c0-e822-4ad9-9f13-74cd9f10b8e8">



***

#### #4 [Docker] Create the docker image for the above-mentioned flask app and run the same view of the page in a browser
1. heloworld
   <img width="443" alt="image" src="https://github.com/user-attachments/assets/da69ed02-b19c-488e-9666-0400e4c6921e">
2.  flask
    <img width="616" alt="image" src="https://github.com/user-attachments/assets/8635e904-b670-4eea-9cba-dc4916628c8c">
3. flask local host
   <img width="959" alt="image" src="https://github.com/user-attachments/assets/99d1fca0-57d7-4f5e-9c47-10cc35130498">



***

#### #5 [Docker] Create a docker compose file for the 2 images: nginx/httpd and run the same view of the page in a browser
<img width="959" alt="image" src="https://github.com/user-attachments/assets/ce065eb2-506b-407a-9ae1-1814e2b77bbe">


***

#### #6 [Docker] Pull one of the participant’s docker images and verify whether the app is running or not
1. Pulled Random participant's Image: 
<img width="959" alt="image" src="https://github.com/user-attachments/assets/c75138f6-17a6-4c1d-aec2-55a8f49cc927">


***

#### #7 Create a GitHub account with a personal mail ID & fork this repo and rename this in the format 22AM0XG-Assignments-Register-Number
1. My GitHub Personal Id:
   https://github.com/AgniKanitha

***

#### #8 Create a LinkedIn account with personal mail ID
1. My personal LinkedId
   https://www.linkedin.com/in/kanitha0903/

***
