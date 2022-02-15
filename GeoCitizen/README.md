# Geo_Citizen 

![Main image](img/geo.jpg?raw=true)

___build  and deploy project on ubuntu remote server with db on CentOS remote server ___


## Soft that was used to build and deploy the project with links how to istall:

1) [Oracle VM VirtualBox](https://www.youtube.com/watch?v=8mns5yqMfZk)    *(youtube guide)*
2) [Ubuntu 20.04 LTS](https://www.youtube.com/watch?v=fAHpGshMCgQ&t=792s)   *(youtube guide)*
3) [CentOS 7](https://prowebmastering.ru/ustanovka-centos-7-v-virtualbox.html)
4) [SSH in Ubuntu 20.04](https://linuxize.com/post/how-to-enable-ssh-on-ubuntu-20-04/) 
5) [SSH in CentOS 7](https://phoenixnap.com/kb/how-to-enable-ssh-centos-7)
6) [Git in Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-20-04-ru)
7) [Tomcat 9.0.58 in Ubuntu 20.04](https://infoit.com.ua/linux/kak-ustanovit-apache-tomcat-v-ubuntu-20-04-lts)
8) [Java 11; open jdk 11](https://losst.ru/ustanovka-java-v-ubuntu-18-04#1_%D0%9A%D0%B0%D0%BA_%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%82%D1%8C_OpenJDK_11_%D0%B2_Ubuntu_2004)
9) [PostgreSQL on CentOS 7](https://linuxize.com/post/how-to-install-postgresql-on-centos-7/)
10) [ApacheMaven 3.8.4 in Ubuntu](https://linuxize.com/post/how-to-install-apache-maven-on-ubuntu-18-04/)


## Introduction

```
Primarely i had host on Windows11 where i have installed Oracle VirtualBox, which I used as virtual remote server for Ubuntu and CentOS. 
In Ubuntu 20.04 was installed and setup ssh, git, TomCat 9.0.58, Java11 and jdk-11, ApacheMaven 3.8.4, PostgreSQL 
In CentOS 7 was installed and setup ssh, PostgreSQL server.
```

## Build and deploy
After installation and setup all necessery tools that are described above. You have to:

1. Clone a repository `git clone https://github.com/mentorchita/Geocit134.git; cd Geocit134`
2. Start to build project with command: 
   
    ```mvn install```

   there are some errors that have to be fixed. 
---
   First we need to fix this file: *~Geocit134/pom.xml*
---
   
  * need to add *javax* like (<artifactId>javax.servlet-api</artifactId>)
   
         <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>servlet-api</artifactId>
            <version>${servlet-api.version}</version>
            <scope>provided</scope>
        </dependency>

* need to change url *http: to https:* in repo below:
```
        <repository>
            <id>org.springframework.maven.milestone</id>
            <name>Spring Maven Milestone Repository</name>
            <url>http://repo.spring.io/milestone</url>
        </repository>
    
    
            <repository>
            <id>spring-milestone</id>
            <name>Spring Maven MILESTONE Repository</name>
            <url>http://repo.spring.io/libs-milestone</url>
        </repository>
  ```
 * need to comment below lines:
   ```
        <distributionManagement>
          <repository>
            <id>nexus</id>
            <name>Releases</name>
            <url>http://35.188.29.52:8081/repository/maven-releases</url>
          </repository>
          <snapshotRepository>
            <id>nexus</id>
            <name>Snapshot</name>
            <url>http://35.188.29.52:8081/repository/maven-snapshots</url>
          </snapshotRepository>
        </distributionManagement>
    ```
---

Second we need to fix this file: *~Geocit134/src/main/resources/application.properties*
---
|#|need to change|how to change|
  |--|--|--|
  |1.|front.url=http://**localhost**:8080/citizen/#|front.url=http://**IP Ubuntu server**:8080/citizen/#  
  |2.|front-end.url=http://**localhost**:8080/citizen/|front-end.url=http://**IP Ubuntu server**:8080/citizen/
  |3.|all "postgresql://**localhost**:5432/ss_demo_1"|postgresql://**IP CentOS server**/ss_demo_1  
  |4.|url=jdbc:postgresql://35.204.28.238:5432/ss_demo_1|url=jdbc:postgresql://**IP CentOS server**/ss_demo_1  
  |8.|email.username=ssgeocitizen@gmail.com|email.username=`<put created new email>`
  |9.|email.password=softserve|email.password=`<password fpr created new email>`

>If you create your email on gmail you have to give access for third-part devices in you google account!

Create  on CentOS new DB as ss_demo_1, with db.username &&  db.password 'postgres'. (in other case have to change necessery lines in application.properties)
---
Next step:

      
   
    ~mvn install
    move our citizen.war to tomcat
    ~sudo mv target/citizen.war /opt/tomcat/latest/webapps/** 
    start tomcat service
    ~sudo sh /opt/tomcat/latest/bin/startup.sh

 
 Then open http://**IP Ubuntu server**:8080/citizen/

> P.S. It possible to fix most of problems manually or using bash script below

 Bash script -> [*geofix.sh*](./geofix.sh) (in script have to change: serverip, databaseip,email,emailpassword )
 